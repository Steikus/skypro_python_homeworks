import requests
from faker import Faker

fake = Faker()


class CompanyApi:

    def __init__(self, url):
        self.url = url

    def get_token(self, user = 'leonardo', password = 'leads'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'auth/login', json=creds)
        return resp.json()["userToken"]

    def create_company(self, name, description=''):
        company = {
            'name': name,
            'description': description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'company', json=company, headers=my_headers)
        return resp.json()

    def get_employee_list(self, id):
        resp = requests.get(self.url+'employee', params={"company": str(id)})
        return resp.json()

    def create_employee(self, information):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+"employee", headers=my_headers, json=information)
        return resp.json()

    def get_one_employee(self, id):
        resp = requests.get(self.url+'employee/'+str(id))
        print(resp)
        return resp.json()

    def edit_employee(self, id, information):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url+"employee/"+str(id), headers=my_headers, json=information)
        return resp.json()
