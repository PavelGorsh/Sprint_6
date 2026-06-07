import locators.order_page_locators as OPL
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

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

    def fill_order_for(self, name, surname, address, metro, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.fill_metro(metro)
        self.fill_phone(phone)

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

    def fill_order_about(self, date, period, color, comment):
        self.fill_date(date)        
        self.fill_period(period)
        self.fill_color(color)
        self.fill_comment(comment)

    def click_order_button_on_order_page(self):
        self.click_button(self.driver, OPL.ORDER_BUTTON)

    def click_order_confirm_button(self):
        self.click_button(self.driver, OPL.ORDER_CONFIRM_BUTTON)

    def check_order(self):
        assert "Заказ оформлен" in self.get_text_attribute(self.driver, OPL.ORDER_SUCCESS)

    def return_base_page(self):
        self.wait_for_load(self.driver, OPL.BUTTON_SHOW_STATUS)
        self.click_button(self.driver, OPL.BUTTON_SHOW_STATUS)
        self.wait_for_load(self.driver, OPL.STATUS)
        self.click_button(self.driver, OPL.BASE_PAGE_BUTTON)
        