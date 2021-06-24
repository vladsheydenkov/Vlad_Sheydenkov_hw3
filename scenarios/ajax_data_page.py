"""
This module provides functions for working with AJAX Data scenario
"""


import allure


from base_page import BasePage
from selenium.webdriver.common.by import By


class SearchLocators():
    AJAX_BUTTON = (By.ID, 'ajaxButton')
    APPEARED_TEXT = (By.CLASS_NAME, 'bg-success')


@allure.feature('Ajax with delay')
class WaitForAjaxHelper(BasePage):

    @allure.step('click on ajax button')
    def click_on_the_ajax_button(self):
        return self.find_element(SearchLocators.AJAX_BUTTON, time=2).click()

    @allure.step('waiting until element loads')
    def wait_until_text_is_appeared(self):
        return self.find_element(SearchLocators.APPEARED_TEXT, time=20).text
