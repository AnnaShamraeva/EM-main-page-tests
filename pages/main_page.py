import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import Url


class MainPage(BasePage):

    @allure.step("Открыть главную страницу Effective Mobile")
    def open_main_page(self):
        self.open_page(Url.main_page)  

    @allure.step("Нажать на логотип EM")
    def click_on_logo(self):
        self.click_on_element(MainPageLocators.LOGO_EM)    

    @allure.step("Прокручиваем страницу до футера")
    def scroll_to_element_about_us(self):
        self.scroll_to_element(MainPageLocators.ABOUT_US) 
   
    @allure.step("Нажать на элемент 'Компания: О нас'")
    def click_about_us(self):
        self.wait_element_to_be_clickable(MainPageLocators.ABOUT_US) 
        self.click_on_element(MainPageLocators.ABOUT_US)  
   
    @allure.step("Нажать на элемент 'Компания: Вакансии'")
    def click_vacansii(self):
        self.click_on_element(MainPageLocators.VACANSII) 

    @allure.step("Нажать на элемент 'Компания: Отзывы'")
    def click_review(self):
        self.click_on_element(MainPageLocators.REVIEW) 
   
    @allure.step("Нажать на элемент 'Компания: Контакты'")
    def click_contact(self):
        self.click_on_element(MainPageLocators.CONTACT)
 
    @allure.step("Нажать на элемент 'Услуги: Аутстафф'")
    def click_outstaff(self):
        self.wait_element(MainPageLocators.OUTSTAFF)
        self.click_on_element(MainPageLocators.OUTSTAFF)

    @allure.step("Нажать на элемент 'Услуги: Трудоустройство'")
    def click_employment(self):
        self.click_on_element(MainPageLocators.EMPLOYMENT)

    @allure.step("Нажать на элемент 'Услуги: Консультация'")
    def click_consultation(self):
        self.click_on_element(MainPageLocators.CONSULTATION)
    
    @allure.step("Нажать на элемент 'Контакты: email'")
    def click_outstaff(self):
        self.wait_element(MainPageLocators.EMAIL_ADRESS)
        self.click_on_element(MainPageLocators.EMAIL_ADRESS)

    @allure.step("Нажать на элемент 'Контакты: telegram'")
    def click_employment(self):
        self.click_on_element(MainPageLocators.TELEGRAM)

    @allure.step("Нажать на элемент 'Политика конфиденциальности'")
    def click_privacy_policy(self):
        self.wait_element(MainPageLocators.PRIVACY_POLICY)
        self.click_on_element(MainPageLocators.PRIVACY_POLICY)

    @allure.step("Нажать на элемент 'Условия использования'")
    def click_terms_of_use(self):
        self.wait_element_to_be_clickable(MainPageLocators.TERMS_OF_USE)  
        self.click_on_element(MainPageLocators.TERMS_OF_USE)   

    @allure.step("Есть элемент 'Email'") # Проверяет наличие ссылки на email
    def is_email_present(self):
        self.find_element(MainPageLocators.EMAIL_ADRESS)

    @allure.step("Есть текст элемента 'Email'") # Возвращает текст ссылки на email
    def get_email_text(self) -> str: 
        return self.get_text(MainPageLocators.EMAIL_ADRESS)

    @allure.step("Есть элемент 'ссылка на Telegram'") # Проверяет наличие ссылки на Telegram
    def is_telegram_present(self):  
        self.find_element(MainPageLocators.TELEGRAM)
 
    @allure.step("Есть текст элемента 'ссылка на Telegram'") # Возвращает текст ссылки на Telegram
    def get_telegram_text(self) -> str:      
        return self.get_text(MainPageLocators.TELEGRAM)      
    
