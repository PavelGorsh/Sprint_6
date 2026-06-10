from data_for_tests.data_lists_for_tests import DataListsForTests as Data
from pages.main_page import MainPage
import pytest
import allure


class TestBasePage:

    @allure.title('Проверка выпадающего списока в разделе «Вопросы о важном»')
    @pytest.mark.parametrize('question, answer, expected_answer', Data().locators_questions_answeres_list())
    def test_drop_down_list(self, question, answer, expected_answer, driver_firefox_scooter):
        # Создадим объект класса ЯндексСамокат - главная страница
        main_page = MainPage(driver_firefox_scooter)
        # Добавь явное ожидание для загрузки главной страницы
        main_page.wait_for_load_main_page()
        # Найди раздел «Вопросы о важном», прокрути страницу к нему и нажми на один из вопросов попорядку
        main_page.click_question_on_base_page(question)
        # Добавь явное ожидание для открытия выпадающего списка
        main_page.wait_for_open_drop_down_list(answer)
        # Проверка текста выпадающего списка
        main_page.check_drop_down_list_on_base_page(answer, expected_answer)

    @allure.title('Проверка нажатия на логотип «Самоката»')
    def test_scooter_logo_button_transition(self, driver_firefox_scooter):
        # Создадим объект класса ЯндексСамокат - главная страница
        main_page = MainPage(driver_firefox_scooter)
        # Добавь явное ожидание для загрузки главной страницы
        main_page.wait_for_load_main_page()
        # Нажми на логотип «Самоката»
        main_page.click_scooter_logo_button()
        # Проверка перехода на главную страницу при нажатии на логотип «Самоката»
        main_page.check_scooter_logo_button_where_transition()

    @allure.title('Проверка нажатия на логотип «Яндекса»')
    def test_yandex_logo_button_transition(self, driver_firefox_scooter):
        # Создадим объект класса ЯндексСамокат - главная страница
        main_page = MainPage(driver_firefox_scooter)
        # Добавь явное ожидание для загрузки главной страницы
        main_page.wait_for_load_main_page()
        # Нажми на логотип «Яндекса»
        main_page.click_yandex_logo_button()
        # Добавь явное ожидание для загрузки страницы
        main_page.wait_for_load_yandex_page()
        # Проверка перехода на главную страницу «Яндекса» при нажатии на логотип «Яндекса»
        main_page.check_yandex_logo_button_where_transition()
