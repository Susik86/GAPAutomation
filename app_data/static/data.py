import json
from faker import Faker

class TestData:
    @staticmethod
    def get_static_data():
        with open("data/static/sample_data.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_dynamic_data():
        fake = Faker()
        return {
            "email": fake.email(),
            "password": fake.password(),
        }
