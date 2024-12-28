from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __int__(self,driver,wait):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def get_visible_element_text(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.find_element(locator).text

    def get_url_page(self,url):
        self.driver.get(url)

    def visibility_element(self,locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def click_on_scrollbar(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", element)
        element.click()

    def switch_to_new_tab(self,index = 1):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def waiting_load_url(self,url):
        self.wait.until(EC.url_to_be(url))

    def scroll_to_down(self,position = 2500):
        self.driver.execute_script(f"window.scrollTo(0, {position})")