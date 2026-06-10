import pytest
import allure
from pages.order_page import OrderPage
from data_for_tests.data_lists_for_tests import DataListsForTests as Data


class TestOrderPage:
    data = Data().data_for_order()

    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize('button, name, surname, address, metro, phone, date, period, color, comment', data)
    def test_order(self, driver_firefox_scooter, button, name, surname, address, metro, phone, date, period, color, comment):
        # Создадим объект класса ЯндексСамокат - главная страница
        order_page = OrderPage(driver_firefox_scooter)
        # Добавь явное ожидание для загрузки главной страницы
        order_page.wait_for_load_main_page()
        # Нажать кнопку «Заказать» на главной странице
        order_page.click_order_button_on_main_page(button)
        # Добавь явное ожидание для загрузки страницы заказа «Для кого самокат»
        order_page.wait_for_load_order_page_for_which_person()
        # Заполнить поля страницы заказа «Для кого самокат»
        order_page.fill_order_for(name, surname, address, metro, phone)
        # Нажать кнопку «Далее» на странице заказа
        order_page.click_order_next()
        # Добавь явное ожидание для загрузки страницы заказа «Про аренду»
        order_page.wait_for_load_order_page_about_rent()
        # Заполнить поля страницы заказа «Про аренду»
        order_page.fill_order_about(date, period, color, comment)
        # Нажать кнопку «Заказать» на странице заказа
        order_page.click_order_button_on_order_page()
        # Добавить явное ожидание для загрузки страницы подтверждения заказа
        order_page.wait_for_load_order_page_confirm()
        # Нажать кнопку «Да»
        order_page.click_order_confirm_button()
        # Добавить явное ожидание для загрузки страницы сообщения об успешном создании заказа
        order_page.wait_for_load_order_page_success()
        # Проверка создания заказа
        order_page.check_order(name, surname, address, metro, phone)
