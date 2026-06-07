from selenium import webdriver
import pytest
import allure
from pages.order_page import OrderPage
import locators.order_page_locators as OPL
import locators.main_page_locators as MPL
import urls
from data_for_tests.data_lists_for_tests import DataListsForTests as Data


class TestOrderPage:
    data = Data().data_for_order()

    @classmethod
    def setup_class(cls):
        # Создадим драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        # Перейдём на страницу ЯндексСамокат
        cls.driver.get(urls.MAIN_PAGE_SCOOTER_SERVICES)
        # Создадим объект класса страницы ЯндексСамокат
        cls.order_page = OrderPage(cls.driver)

    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize('button, name, surname, address, metro, phone, date, period, color, comment', data)
    def test_order(self, button, name, surname, address, metro, phone, date, period, color, comment):
        # Добавь явное ожидание для загрузки главной страницы
        self.order_page.wait_for_load(self.driver, MPL.ORDER_BTN_BASE_PAGE_HEADER)
        # Нажать кнопку «Заказать» на главной странице
        self.order_page.click_order_button_on_main_page(button)
        # Добавь явное ожидание для загрузки страницы заказа «Для кого самокат»
        self.order_page.wait_for_load(self.driver, OPL.NAME)
        # Заполнить поля страницы заказа «Для кого самокат»
        self.order_page.fill_order_for(name, surname, address, metro, phone)
        # Нажать кнопку «Далее» на странице заказа
        self.order_page.click_order_next()
        # Добавь явное ожидание для загрузки страницы заказа «Про аренду»
        self.order_page.wait_for_load(self.driver, OPL.DATE)
        # Заполнить поля страницы заказа «Про аренду»
        self.order_page.fill_order_about(date, period, color, comment)
        # Нажать кнопку «Заказать» на странице заказа
        self.order_page.click_order_button_on_order_page()
        # Добавить явное ожидание для загрузки страницы подтверждения заказа
        self.order_page.wait_for_load(self.driver, OPL.ORDER_CONFIRM)
        # Нажать кнопку «Да»
        self.order_page.click_order_confirm_button()
        # Добавить явное ожидание для загрузки страницы сообщения об успешном создании заказа
        self.order_page.wait_for_load(self.driver, OPL.ORDER_SUCCESS)
        # Проверка создания заказа
        self.order_page.check_order()
        # Возврат на главную страницу
        self.order_page.return_base_page()

    @classmethod
    def teardown_class(cls):
        # Закроем браузер
        cls.driver.quit()
