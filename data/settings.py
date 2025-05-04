
class Settings:

    branch = 'Test'

    # API
    Authorization = True

    # WEB
    Browser = {
        'Name': 'chrome',
        'headless': False
    }

    GLOBAL = {
        'Test': {
            'URL': 'https://www.google.com/',
            'API': {
                'URL': 'https://petstore.swagger.io/v2/',
                'AUTH_URL': ""
            },
            'SQL_SERVER': {
                'TypeSQL': '',
                'SERVER': '',
                'PORT': '',
                'password': ''
            },
            # the main user for first connection and test data setup
            'USERS': {
                'SystemOperator': {
                    'Email': '',
                    'Password': ''
                },
            }
        }
    }
