import allure

from Test.api_tests.api_test_base import ApiTestBase


@allure.feature('Test petstore')
class TestPetStore(ApiTestBase):

    @allure.title('Actions with user')
    def test_api_actions_with_user(self):
        # because for https://petstore.swagger.io/# don't need access token
        self.APP.settings.Authorization = False
        username = "jdoe"
        password = "secureP@ss123"
        # create user
        response = self.APP.api_actions_in_user.post_create_user({"id": 101, "username": username, "firstName": "John",
                                                       "lastName": "Doe", "email": "jdoe@example.com",
                                                       "password": password, "phone": "+1234567890",
                                                       "userStatus": 1})
        # log in from user
        access_token = self.APP.api_actions_in_user.log_in({"username": username, "password": password})

        # Checks
        assert response['code'] == 200
        assert access_token['code'] == 200
        assert 'logged in user session:' in access_token['message']

