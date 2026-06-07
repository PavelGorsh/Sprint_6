from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators.order_page_locators as OPL


class OrderPageScooter:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((element)))

    def fill_name(self, name):
        self.driver.find_element(*OPL.NAME).send_keys(name)
    
    def fill_surname(self, surname):
        self.driver.find_element(*OPL.SURNAME).send_keys(surname)

    def fill_address(self, address):
        self.driver.find_element(*OPL.ADDRESS).send_keys(address)

    def fill_metro(self, metro):
        self.driver.find_element(*OPL.METRO).click()
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*metro))
        self.driver.find_element(*metro).click()

    def fill_phone(self, phone):
        self.driver.find_element(*OPL.PHONE).send_keys(phone)

    def fill_order_for(self, name, surname, address, metro, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.fill_metro(metro)
        self.fill_phone(phone)

    def click_order_next(self):
        self.driver.find_element(*OPL.NEXT).click()

    def fill_date(self, date):
        self.driver.find_element(*OPL.DATE).click()
        self.wait_for_load(OPL.DATEPICKER)
        self.driver.find_element(*date).click()

    def fill_period(self, period):
        self.driver.find_element(*OPL.PERIOD).click()
        self.driver.find_element(*period).click()

    def fill_color(self, color):
        self.driver.find_element(*color).click()

    def fill_comment(self, comment):
        self.driver.find_element(*OPL.COMMENT).send_keys(comment)

    def fill_order_about(self, date, period, color, comment):
        self.fill_date(date)        
        self.fill_period(period)
        self.fill_color(color)
        self.fill_comment(comment)

    def click_order_button(self):
        self.driver.find_element(*OPL.ORDER_BUTTON).click()

    def click_order_window_button(self):
        self.driver.find_element(*OPL.ORDER_CONFIRM_BUTTON).click()

    def check_order(self):
        assert "Заказ оформлен" in self.driver.find_element(*OPL.ORDER_SUCCESS).text

    def return_base_page(self):
        self.driver.find_element(*OPL.BUTTON_SHOW_STATUS).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((OPL.STATUS)))
        self.driver.find_element(*OPL.BASE_PAGE_BUTTON).click()
        