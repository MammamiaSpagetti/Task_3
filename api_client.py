import requests

from data import REQUEST_TIMEOUT
from urls import REGISTER_USER_API_URL, USER_API_URL


class UserApi:
    @staticmethod
    def create_user(user_data):
        return requests.post(
            REGISTER_USER_API_URL,
            json=user_data,
            timeout=REQUEST_TIMEOUT,
        )

    @staticmethod
    def delete_user(access_token):
        return requests.delete(
            USER_API_URL,
            headers={'Authorization': access_token},
            timeout=REQUEST_TIMEOUT,
        )
