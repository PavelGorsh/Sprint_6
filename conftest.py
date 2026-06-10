import pytest
import urls
from selenium import webdriver

@pytest.fixture
def driver_firefox_scooter():
    # Создадим драйвер для браузера Firefox
    driver = webdriver.Firefox()
    # Перейдём на страницу ЯндексСамокат
    driver.get(urls.MAIN_PAGE_SCOOTER_SERVICES)
    yield driver
    # Закроем браузер
    driver.quit()
