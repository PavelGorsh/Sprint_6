from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def wait_for_load(self, driver, element):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((element)))

    def wait_for_load_2_windows(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.number_of_windows_to_be(2))

    def wait_for_load_window_title(self, driver, comment):
        WebDriverWait(driver, 5).until(expected_conditions.title_is(comment))

    def click_button(self, driver, element):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((element)))
        driver.find_element(*element).click()

    def scroll_page(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*element))

    def send_keys(self, driver, element, comment):
        driver.find_element(*element).send_keys(comment)

    def get_text_attribute(self, driver, element):
        return driver.find_element(*element).text
    
    def get_current_url(self, driver):
        return driver.current_url

    def get_window_current_handle(self, driver):
        return driver.current_window_handle

    def get_window_handles(self, driver):
        return driver.window_handles
    
    def switch_window(self, driver, handle):
        driver.switch_to.window(handle)
