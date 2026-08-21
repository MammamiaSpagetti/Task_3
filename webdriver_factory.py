from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class WebDriverFactory:
    @staticmethod
    def create_driver(browser_name, headless=True):
        if browser_name == 'chrome':
            options = ChromeOptions()
            options.page_load_strategy = 'eager'
            if headless:
                options.add_argument('--headless=new')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            options = FirefoxOptions()
            options.page_load_strategy = 'eager'
            if headless:
                options.add_argument('-headless')
            driver = webdriver.Firefox(options=options)
            driver.set_window_size(1920, 1080)
        else:
            raise ValueError(f'Неподдерживаемый браузер: {browser_name}')

        driver.set_page_load_timeout(30)
        return driver
