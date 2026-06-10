import locators.main_page_locators as MPL
import urls
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_main_page(self):
        self.wait_for_load(self.driver, MPL.ORDER_BTN_BASE_PAGE_HEADER)

    def wait_for_open_drop_down_list(self, answer):
        self.wait_for_load(self.driver, answer)

    def wait_for_load_yandex_page(self):
        original_window_handle = self.get_window_current_handle(self.driver)
        self.wait_for_load_2_windows(self.driver)
        new_window_handle = (set(self.get_window_handles(self.driver)) - {original_window_handle}).pop()
        self.switch_window(self.driver, new_window_handle)
        self.wait_for_load_window_title(self.driver, "Яндекс — быстрый поиск в интернете")
    
    @allure.step('Нажимаем на один из вопросов в разделе «Вопросы о важном»')
    def click_question_on_base_page(self, question):
        self.scroll_page(self.driver, MPL.QUESTIONS_BLOCK)
        self.click_button(self.driver, question)

    def click_order_button_on_base_page(self, button):
        self.scroll_page(self.driver, button)
        self.click_button(self.driver, button)

    @allure.step('Нажимаем на логотип «Самоката»')
    def click_scooter_logo_button(self):
        self.click_button(self.driver, MPL.LOGO_SCOOTER)

    @allure.step('Нажимаем на логотип «Яндекса»')
    def click_yandex_logo_button(self):
        self.click_button(self.driver, MPL.LOGO_YANDEX)

    @allure.step('Проверяем ответ на вопрос')
    def check_drop_down_list_on_base_page(self, answer, expected_answer):
        assert expected_answer == self.get_text_attribute(self.driver, answer)

    @allure.step('Проверяем что произошел переход на главную страницу «Самоката»')
    def check_scooter_logo_button_where_transition(self):
        assert urls.MAIN_PAGE_SCOOTER_SERVICES == self.get_current_url(self.driver)
    
    @allure.step('Проверяем что произошел переход на главную страницу «Яндекса»')
    def check_yandex_logo_button_where_transition(self):
        assert urls.MAIN_PAGE_YANDEX_SHORT in self.get_current_url(self.driver)
