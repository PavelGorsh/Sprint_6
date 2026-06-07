from selenium import webdriver
from pages.base_page import BasePageScooter
from pages.order_page import OrderPageScooter
import locators.order_page_locators as OPL
from urls import UrlsScooter
from data_for_tests.data_lists_for_tests import DataListsForTests as Data
import pytest


class TestOrderPage:
    driver = None
    data = Data().data_for_order()

    @classmethod
    def setup_class(cls):
        # Создадим драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        # Перейдём на страницу ЯндексСамокат
        cls.driver.get(UrlsScooter().MAIN_PAGE)
        # Создадим объект класса страницы ЯндексСамокат
        cls.base_page = BasePageScooter(cls.driver)
        cls.order_page = OrderPageScooter(cls.driver)

    @pytest.mark.parametrize('button, name, surname, address, metro, phone, date, period, color, comment', data)
    def test_order(self, button, name, surname, address, metro, phone, date, period, color, comment):
        # Добавь явное ожидание для загрузки базовой страницы
        self.base_page.wait_for_load_base_page()
        # Нажать кнопку «Заказать»
        self.base_page.click_order_button(button)
        # Добавь явное ожидание для загрузки страницы заказа
        self.order_page.wait_for_load(OPL.NAME)
        # Заполнить поля заказа «Для кого самокат»
        self.order_page.fill_order_for(name, surname, address, metro, phone)
        # Нажать кнопку «Далее»
        self.order_page.click_order_next()
        # Заполнить поля заказа «Про аренду»
        self.order_page.fill_order_about(date, period, color, comment)
        # Нажать кнопку «Заказать»
        self.order_page.click_order_button()
        # Добавить явное ожидание для загрузки страницы подтверждения заказа
        self.order_page.wait_for_load(OPL.ORDER_CONFIRM)
        # Нажать кнопку «Да»
        self.order_page.click_order_window_button()
        # Добавить явное ожидание для загрузки страницы сообщения об успешном создании заказа
        self.order_page.wait_for_load(OPL.ORDER_SUCCESS)
        # Проверка создания заказа
        self.order_page.check_order()
        # Возврат на главную страницу
        self.order_page.return_base_page()

    @classmethod
    def teardown_class(cls):
        # Закроем браузер
        cls.driver.quit()
