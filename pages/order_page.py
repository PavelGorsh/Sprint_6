import locators.order_page_locators as OPL
import locators.main_page_locators as MPL
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_main_page(self):
        self.wait_for_load(self.driver, MPL.ORDER_BTN_BASE_PAGE_HEADER)

    def wait_for_load_order_page_for_which_person(self):
        self.wait_for_load(self.driver, OPL.NAME)

    def wait_for_load_order_page_about_rent(self):
        self.wait_for_load(self.driver, OPL.DATE)

    def wait_for_load_order_page_confirm(self):
        self.wait_for_load(self.driver, OPL.ORDER_CONFIRM)

    def wait_for_load_order_page_success(self):
        self.wait_for_load(self.driver, OPL.ORDER_SUCCESS)

    @allure.step('Нажимаем на одну из кнопок «Заказать» на главной странице')
    def click_order_button_on_main_page(self, button):
        self.scroll_page(self.driver, button)
        self.click_button(self.driver, button)

    def fill_name(self, name):
        self.send_keys(self.driver, OPL.NAME, name)
    
    def fill_surname(self, surname):
        self.send_keys(self.driver, OPL.SURNAME, surname)

    def fill_address(self, address):
        self.send_keys(self.driver, OPL.ADDRESS, address)

    def fill_metro(self, metro):
        self.click_button(self.driver, OPL.METRO)
        self.scroll_page(self.driver, metro)
        self.click_button(self.driver, metro)

    def fill_phone(self, phone):
        self.send_keys(self.driver, OPL.PHONE, phone)

    @allure.step('Заполняем поля страницы заказа «Для кого самокат»')
    def fill_order_for(self, name, surname, address, metro, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.fill_metro(metro)
        self.fill_phone(phone)

    @allure.step('Нажимаем кнопку «Далее»')
    def click_order_next(self):
        self.click_button(self.driver, OPL.NEXT)

    def fill_date(self, date):
        self.click_button(self.driver, OPL.DATE)
        self.wait_for_load(self.driver, OPL.DATEPICKER)
        self.click_button(self.driver, date)

    def fill_period(self, period):
        self.click_button(self.driver, OPL.PERIOD)
        self.click_button(self.driver, period)

    def fill_color(self, color):
        self.click_button(self.driver, color)

    def fill_comment(self, comment):
        self.send_keys(self.driver, OPL.COMMENT, comment)

    @allure.step('Заполняем поля страницы заказа «Про аренду»')
    def fill_order_about(self, date, period, color, comment):
        self.fill_date(date)        
        self.fill_period(period)
        self.fill_color(color)
        self.fill_comment(comment)

    @allure.step('Нажимаем кнопку «Заказать»')
    def click_order_button_on_order_page(self):
        self.click_button(self.driver, OPL.ORDER_BUTTON)

    @allure.step('Нажимаем кнопку «Да»')
    def click_order_confirm_button(self):
        self.click_button(self.driver, OPL.ORDER_CONFIRM_BUTTON)

    @allure.step('Проверяем успешность создания заказа самоката')
    def check_order(self, name, surname, address, metro, phone):
        success_title = self.get_text_attribute(self.driver, OPL.ORDER_SUCCESS)
        self.wait_for_load(self.driver, OPL.BUTTON_SHOW_STATUS)
        self.click_button(self.driver, OPL.BUTTON_SHOW_STATUS)
        self.wait_for_load(self.driver, OPL.ORDER_STATUS_NAME)
        assert {"Заказ оформлен" in success_title and name == OPL.ORDER_STATUS_NAME
                and surname == OPL.ORDER_STATUS_SURNAME and address == OPL.ORDER_STATUS_ADDRESS
                and metro == OPL.ORDER_STATUS_METRO and phone == OPL.ORDER_STATUS_PHONE}
        