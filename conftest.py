import pytest
import urls
from selenium import webdriver
from pages.main_page import MainPage

@pytest.fixture
def driver_firefox_scooter():
    # Создадим драйвер для браузера Firefox
    driver = webdriver.Firefox()
    # Перейдём на страницу ЯндексСамокат
    driver.get(urls.MAIN_PAGE_SCOOTER_SERVICES)
    # Создадим объект класса страницы ЯндексСамокат
    main_page = MainPage(driver)
    yield {"driver": driver, "main_page": main_page} # Возвращает драйвер и объект класса страницы ЯндексСамокат
    # Закроем браузер
    driver.quit()
