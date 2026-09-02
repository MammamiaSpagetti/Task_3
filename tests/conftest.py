import allure
import pytest

from api_client import UserApi
from data import generate_user_data
from pages.login_page import LoginPage
from webdriver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='all',
        choices=('all', 'chrome', 'firefox'),
        help='Браузер для запуска: all, chrome или firefox',
    )
    parser.addoption(
        '--headed',
        action='store_true',
        default=False,
        help='Запустить браузер с видимым окном',
    )


def pytest_generate_tests(metafunc):
    if 'browser_name' not in metafunc.fixturenames:
        return

    selected_browser = metafunc.config.getoption('--browser')
    browsers = (
        ['chrome', 'firefox']
        if selected_browser == 'all'
        else [selected_browser]
    )
    metafunc.parametrize('browser_name', browsers, scope='function')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f'rep_{report.when}', report)


@pytest.fixture
def driver(request, browser_name):
    headless = not request.config.getoption('--headed')
    browser_driver = WebDriverFactory.create_driver(browser_name, headless)
    allure.dynamic.parameter('browser', browser_name)

    yield browser_driver

    if getattr(request.node, 'rep_call', None) and request.node.rep_call.failed:
        allure.attach(
            browser_driver.get_screenshot_as_png(),
            name=f'Ошибка в {browser_name}',
            attachment_type=allure.attachment_type.PNG,
        )
    browser_driver.quit()


@pytest.fixture
def user():
    user_data = generate_user_data()
    response = UserApi.create_user(user_data)
    if response.status_code != 200:
        pytest.fail(
            f'Не удалось создать тестового пользователя: '
            f'{response.status_code} {response.text}'
        )

    access_token = response.json()['accessToken']
    user_context = {
        **user_data,
        'access_token': access_token,
    }

    yield user_context

    delete_response = UserApi.delete_user(access_token)
    if delete_response.status_code not in (200, 202):
        pytest.fail(
            f'Не удалось удалить тестового пользователя: '
            f'{delete_response.status_code} {delete_response.text}'
        )


@pytest.fixture
def authenticated_driver(driver, user):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(user['email'], user['password'])
    return driver
