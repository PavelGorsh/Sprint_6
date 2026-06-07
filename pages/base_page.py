from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators.base_page_locators as BPL
import urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_base_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((BPL.ORDER_BTN_HEADER)))

    def wait_for_open_drop_down_list(self, answer):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((answer)))

    def scroll_base_page(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))

    def scroll_base_page_header(self):
        self.driver.execute_script("window.scrollBy(0, -2000);")
    
    def click_question(self, question):
        self.driver.find_element(*question).click()

    def check_drop_down_list(self, answer, expected_answer):
        assert expected_answer == self.driver.find_element(*answer).text

    def click_order_button(self, button):
        self.scroll_base_page(button)
        self.driver.find_element(*button).click()

    def click_scooter_logo_button(self):
        self.driver.find_element(*BPL.LOGO_SCOOTER).click()

    def click_yandex_logo_button(self):
        self.driver.find_element(*BPL.LOGO_YANDEX).click()

    def check_scooter_logo_button_where_transition(self):
        assert urls.MAIN_PAGE_SCOOTER_SERVICES == self.driver.current_url

    def wait_for_load_yandex_page(self):
        wait = WebDriverWait(self.driver, 5)
        original_window_handle = self.driver.current_window_handle
        wait.until(expected_conditions.number_of_windows_to_be(2))
        new_window_handle = (set(self.driver.window_handles) - {original_window_handle}).pop()
        self.driver.switch_to.window(new_window_handle)
        wait.until(expected_conditions.title_is("Яндекс — быстрый поиск в интернете"))
        
    def check_yandex_logo_button_where_transition(self):
        assert urls.MAIN_PAGE_YANDEX_SHORT in self.driver.current_url
