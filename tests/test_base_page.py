from data_for_tests.data_lists_for_tests import DataListsForTests as Data
import locators.main_page_locators as MPL
import pytest


class TestBasePage:

    @pytest.mark.parametrize('question, answer, expected_answer', Data().locators_questions_answeres_list())
    def test_drop_down_list(self, question, answer, expected_answer, driver_firefox_scooter):
        # Распакуй параметры из словаря, который возвращает фикстура
        driver = driver_firefox_scooter["driver"]
        main_page = driver_firefox_scooter["main_page"]
        # Добавь явное ожидание для загрузки страницы
        main_page.wait_for_load(driver, MPL.ORDER_BTN_BASE_PAGE_HEADER)
        # Найди раздел "Вопросы о важном" и прокрути страницу к нему
        main_page.scroll_page(driver, MPL.QUESTIONS_BLOCK)
        # Нажми на один из вопросов попорядку
        main_page.click_question_on_base_page(question)
        # Добавь явное ожидание для открытия выпадающего списка
        main_page.wait_for_open_drop_down_list(answer)
        # Проверка текста выпадающего списка
        main_page.check_drop_down_list_on_base_page(answer, expected_answer)

    def test_scooter_logo_button_transition(self, driver_firefox_scooter):
        # Распакуй параметры из словаря, который возвращает фикстура
        driver = driver_firefox_scooter["driver"]
        main_page = driver_firefox_scooter["main_page"]
        # Добавь явное ожидание для загрузки страницы
        main_page.wait_for_load(driver, MPL.ORDER_BTN_BASE_PAGE_HEADER)
        # Найди логотип «Самоката» и прокрути страницу к нему
        main_page.scroll_page(driver, MPL.LOGO_SCOOTER)
        # Нажми на логотип «Самоката»
        main_page.click_scooter_logo_button()
        # Проверка перехода на главную страницу при нажатии на логотип «Самоката»
        main_page.check_scooter_logo_button_where_transition()

    def test_yandex_logo_button_transition(self, driver_firefox_scooter):
        # Распакуй параметры из словаря, который возвращает фикстура
        driver = driver_firefox_scooter["driver"]
        main_page = driver_firefox_scooter["main_page"]
        # Добавь явное ожидание для загрузки страницы
        main_page.wait_for_load(driver, MPL.ORDER_BTN_BASE_PAGE_HEADER)
        # Найди логотип «Яндекса» и прокрути страницу к нему
        main_page.scroll_page(driver, MPL.LOGO_YANDEX)
        # Нажми на логотип «Яндекса»
        main_page.click_yandex_logo_button()
        # Добавь явное ожидание для загрузки страницы
        main_page.wait_for_load_yandex_page()
        # Проверка перехода на главную страницу «Яндекса» при нажатии на логотип «Яндекса»
        main_page.check_yandex_logo_button_where_transition()
