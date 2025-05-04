import allure

from fw.api.api_base import APIBase


class ApiUser(APIBase):

    @allure.step('Create user. POST user')
    def post_create_user(self, body):
        return self.requests_POST(self.get_base_url() + 'user', body)

    @allure.step('Logs user into the system. GET user/login')
    def get_logs_user_into_the_system(self, params=None):
        return self.requests_GET(self.get_base_url() + f'user/login', params)

    @allure.step('Updated user. PUT user/{username}')
    def put_updated_user(self, username, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'user/{username}', body, params)