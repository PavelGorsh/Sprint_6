from selenium import webdriver
from pages.base_page import BasePageScooter
from urls import UrlsScooter
from data_for_tests.data_lists_for_tests import DataListsForTests as Data
import locators.base_page_locators as BPL
import pytest


class TestBasePage:

    @classmethod
    def setup_class(cls):
        # Создадим драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        # Перейдём на страницу ЯндексСамокат
        cls.driver.get(UrlsScooter().MAIN_PAGE)
        # Создадим объект класса страницы ЯндексСамокат
        cls.base_page = BasePageScooter(cls.driver)

    @pytest.mark.parametrize('question, answer, expected_answer', Data().locators_questions_answeres_list())
    def test_drop_down_list(self, question, answer, expected_answer):
        # Добавь явное ожидание для загрузки страницы
        self.base_page.wait_for_load_base_page()
        # Найди раздел "Вопросы о важном" и прокрути страницу к нему
        self.base_page.scroll_base_page(BPL.QUESTIONS_BLOCK)
        # Нажми на один из вопросов попорядку
        self.base_page.click_question(question)
        # Добавь явное ожидание для открытия выпадающего списка
        self.base_page.wait_for_open_drop_down_list(answer)
        # Проверка текста выпадающего списка
        self.base_page.check_drop_down_list(answer, expected_answer)

    def test_scooter_logo_button_transition(self):
        # Добавь явное ожидание для загрузки страницы
        self.base_page.wait_for_load_base_page()
        # Найди логотип «Самоката» и прокрути страницу к нему
        self.base_page.scroll_base_page_header()
        # Нажми на логотип «Самоката»
        self.base_page.click_scooter_logo_button()
        # Проверка перехода на главную страницу при нажатии на логотип «Самоката»
        self.base_page.check_scooter_logo_button_where_transition()

    def test_yandex_logo_button_transition(self):
        # Добавь явное ожидание для загрузки страницы
        self.base_page.wait_for_load_base_page()
        # Нажми на логотип «Яндекса»
        self.base_page.click_yandex_logo_button()
        # Добавь явное ожидание для загрузки страницы
        self.base_page.wait_for_load_yandex_page()
        # Проверка перехода на главную страницу «Яндекса» при нажатии на логотип «Яндекса»
        self.base_page.check_yandex_logo_button_where_transition()

    @classmethod
    def teardown_class(cls):
        # Закроем браузер
        cls.driver.quit()
