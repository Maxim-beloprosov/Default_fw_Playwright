import json
import allure
import base64

from json.decoder import JSONDecodeError
import jsonschema
import requests

from fw.fw_base import FWBase


class APIBase(FWBase):

    def get_base_url(self):
        return self.manager.settings.GLOBAL[self.manager.settings.branch]['API']['URL']

    def get_header(self, application_json=True, headers=None, accept=False):
        if headers is None:
            headers = {}
        else:
            return headers

        if self.manager.settings.Authorization:
            if self.manager.group_data.access_token == '':
                self.manager.api_actions_in_user.log_in()
            headers['Authorization'] = str(self.manager.group_data.token_type + ' ' + self.manager.group_data.access_token)

        if accept is True:
            headers['accept'] = 'application/json'

        if application_json:
            headers['Accept'] = 'application/json'
            headers['Content-Type'] = 'application/json'

        if self.manager.group_data.using_refresh_token:
            headers['Cookie'] = 'refresh-token=' + self.manager.group_data.refresh_token

        return headers

    def encode_in_base64(self, string):
        str_bytes = base64.b64encode(string.encode("UTF-8"))
        return str_bytes.decode("UTF-8")

    @allure.step('requests_GET')
    def requests_GET(self, get_URL, params=None):
        headers = self.get_header()

        response = requests.get(get_URL, headers=headers, params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        assert response.status_code < 500
        try:
            if response.status_code > 300:
                return response
            else:
                return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_POST')
    def requests_POST(self, get_URL, body, params=None):
        headers = self.get_header()

        response = requests.post(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        assert response.status_code < 500
        try:
            if response.status_code > 300:
                return response
            else:
                return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_PUT')
    def requests_PUT(self, get_URL, body, params=None):
        headers = self.get_header()

        response = requests.put(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        assert response.status_code < 500
        try:
            if response.status_code > 300:
                return response
            else:
                return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_DELETE')
    def requests_DELETE(self, get_URL, body=None, params=None):
        headers = self.get_header()

        response = requests.delete(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        assert response.status_code < 500
        try:
            if response.status_code > 300:
                return response
            else:
                return response.json()
        except JSONDecodeError:
            return response

    @allure.step('requests_PATCH')
    def requests_PATCH(self, get_URL, body, params=None):
        headers = self.get_header()

        response = requests.patch(get_URL, headers=headers, data=json.dumps(body), params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'
        assert response.status_code < 500
        try:
            if response.status_code > 300:
                return response
            else:
                return response.json()
        except JSONDecodeError:
            return response

    @allure.step('upload_file')
    def requests_upload_file(self, file_path, file_name, file_type, api_URL, body=None, params=None, metod_type='PATCH'):
        headers = self.get_header(accept=True, application_json=False)

        if body is None:
            files = {'files': (str(file_name), open(file_path, 'rb'), str(file_type))}
        else:
            files = {'files': (str(file_name), open(file_path, 'rb'), str(file_type), body)}

        if metod_type == 'POST':
            response = requests.post(api_URL, headers=headers, files=files, params=params)
        if metod_type == 'PATCH':
            response = requests.patch(api_URL, headers=headers, files=files, params=params)
        response.encoding = 'utf-8'

        assert response.status_code < 500
        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('Upload file')
    def upload_file(self, file_path, api_URL, body=None, metod_type='PATCH'):
        # Get file type
        file_type = self.manager.work_with_file.get_MIME_file_format(file_path)
        # Get file name
        file_name = self.manager.work_with_file.get_file_name_by_path(file_path)
        response = self.requests_upload_file(file_path, file_name, file_type, api_URL, body, metod_type=metod_type)
        return response


    def json_validate(self, json, schema):
        try:
            jsonschema.validate(instance=json, schema=schema)
            return True
        except Exception as e:
            raise e
