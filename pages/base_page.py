
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        
    # Открыть страницу
    def open_page(self, url):
        self.driver.get(url)

    # Получить url текущей страницы
    def get_current_url(self):
        return self.driver.current_url
    
    # Ссылка работает - осуществляется переход
    def cross_url(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(url))   
    
    # Найти элемент
    def find_element(self, locator):
        self.driver.find_element(*locator)

    # Подождать элемент
    def wait_element(self, locator):
       WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    # Подождать кликабельности элемента
    def wait_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click() 

    # Нажать на элемент
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator)).click() 

    # Получить текст
    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    # Передать значения
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    # Переключить активное окно
    def tab_switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    # Прокрутка
    def scroll_to_element(self, locator):
        element=self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)

        







