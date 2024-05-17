import random
import time

import allure
import pytest
# from faker import Faker
from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Test {random.randint(1, 100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("Success")

    # @allure.title("Change profile lastname")
    # @allure.severity("Critical")
    # @pytest.mark.smoke
    # def test_change_profile_lastname(self):
    #     fake = Faker()
    #     lastname = fake.last_name_male()
    #     self.login_page.open()
    #     self.login_page.enter_login(self.data.LOGIN)
    #     self.login_page.enter_password(self.data.PASSWORD)
    #     self.login_page.click_submit_button()
    #     self.dashboard_page.is_opened()
    #     self.dashboard_page.click_my_info_link()
    #     self.personal_page.is_opened()
    #     self.personal_page.change_lastname(lastname)
    #     self.personal_page.save_changes()
    #     self.personal_page.is_lastname_saved()
    #     self.personal_page.make_screenshot("Success")
