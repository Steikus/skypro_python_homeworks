from CompanyApi import CompanyApi
from faker import Faker


api = CompanyApi("https://x-clients-be.onrender.com/")
fake = Faker()


def test_get_empty_employee_list():
    name = "Random for employee"
    descr = "Test"
    result = api.create_company(name, descr)
    new_id = result["id"]
    empl = api.get_employee_list(new_id)
    assert empl == []


def test_add_employee():
    name = fake.company()
    descr = fake.sentence()
    result = api.create_company(name, descr)
    new_id = result["id"]
    full_data = {
        "id": 0,
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "middleName": fake.prefix(),
        "companyId": new_id,
        "email": fake.email(),
        "url": fake.url(),
        "phone": fake.phone_number(),
        "birthdate": "2024-06-08T14:50:09.906Z",
        "isActive": True
        }
    empl = api.create_employee(full_data)
    print(empl)
    assert empl["id"] > 0


def test_add_and_get_employee():
    name = fake.company()
    descr = fake.sentence()
    result = api.create_company(name, descr)
    new_id = result["id"]
    full_data = {
        "id": 0,
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "middleName": fake.prefix(),
        "companyId": new_id,
        "email": fake.free_email(),
        "url": fake.url(),
        "phone": fake.phone_number(),
        "birthdate": "2024-06-08T14:50:09.906Z",
        "isActive": True
        }
    api.create_employee(full_data)
    api.create_employee(full_data)
    api.create_employee(full_data)
    list = api.get_employee_list(new_id)
    print(list)
    assert list[0]["companyId"] == new_id
    assert list[1]["companyId"] == new_id
    assert list[2]["companyId"] == new_id


def test_get_this_employee():
    name = fake.company()
    descr = fake.sentence()
    result = api.create_company(name, descr)
    new_id = result["id"]
    full_data = {
        "id": 0,
        "firstName": "Vasya",
        "lastName": fake.last_name(),
        "middleName": fake.prefix(),
        "companyId": new_id,
        "email": fake.free_email(),
        "url": fake.url(),
        "phone": fake.phone_number(),
        "birthdate": "2024-06-08T14:50:09.906Z",
        "isActive": True
        }
    empl = api.create_employee(full_data)
    info = api.get_one_employee(empl["id"])
    assert info["firstName"] == "Vasya"


def test_editin_employee():
    name = fake.company()
    descr = fake.sentence()
    result = api.create_company(name, descr)
    new_id = result["id"]
    full_data = {
        "id": 0,
        "firstName": "Vasya",
        "lastName": fake.last_name(),
        "middleName": fake.prefix(),
        "companyId": new_id,
        "email": fake.email(),
        "url": fake.url(),
        "phone": fake.phone_number(),
        "birthdate": "2024-06-08T14:50:09.906Z",
        "isActive": True
        }
    empl = api.create_employee(full_data)
    print(empl)
    info = api.get_one_employee(empl["id"])
    print(info)
    new_data = {
        "lastName": "Fedya",
        "email": "random@email.ru",
        "url": fake.url(),
        "phone": "+78805553535",
        "isActive": True
        }
    api.edit_employee(empl["id"], new_data)
    new_info = api.get_one_employee(empl["id"])
    print(new_info)
    assert info["lastName"] != new_info["lastName"]
    assert info["email"] != new_info["email"]
    assert info["avatar_url"] != new_info["avatar_url"]
