import allure

from fw.api.petstore.user.api_user import ApiUser


class ApiActionsInUser(ApiUser):

    @allure.step('Create user')
    def create_user(self, request_mass={}):
        body = {
            "id": request_mass['id'],
            "username": request_mass['username'],
            "firstName": request_mass['firstName'],
            "lastName": request_mass['lastName'],
            "email": request_mass['email'],
            "password": request_mass['password'],
            "phone": request_mass['phone'],
            "userStatus": request_mass['userStatus']
        }

        return self.post_create_user(body)

    @allure.step('Log in')
    def log_in(self, request_mass={}):
        body = {
            "username": request_mass['username'],
            "password": request_mass['password']
        }

        return self.get_logs_user_into_the_system(body)
