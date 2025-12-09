import allure
from curl import Url
from pages.main_page import MainPage
# from pages.dzen_page import DzenPage

class TestClickOnFooter:
 
    @allure.title("Тест: при нажатии на элемент 'Компания: о нас' был совершен переход на https://www.effective-mobile.ru/#about")
    def test_click_about_us(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.scroll_to_element_about_us()
        main_page.click_about_us()
        expected_url ='https://www.effective-mobile.ru/#about'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"
       

    @allure.title("Тест: при нажатии на элемент 'Компания: Вакансии' был совершен переход на https://www.effective-mobile.ru/#specializations")
    def test_click_vacansii(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.click_vacansii()
        expected_url ='https://www.effective-mobile.ru/#specializations'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"
        
    @allure.title("Тест: при нажатии на элемент 'Компания: Отзывы' был совершен переход на https://www.effective-mobile.ru/#testimonials")
    def test_click_review(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.click_review()
        expected_url ='https://www.effective-mobile.ru/#testimonials'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"

    @allure.title("Тест: при нажатии на элемент 'Компания: Контакты' был совершен переход на https://www.effective-mobile.ru/#contact")
    def test_click_contact(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.click_contact()
        expected_url ='https://www.effective-mobile.ru/#contact'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"    

    @allure.title("Тест: при нажатии на элемент 'Услуги: Аутстафф' был совершен переход на https://www.effective-mobile.ru/#services")
    def test_click_outstaff(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.click_outstaff()
        expected_url ='https://www.effective-mobile.ru/#services'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"    

    @allure.title("Тест: при нажатии на элемент 'Услуги: Трудоустройство' был совершен переход на https://www.effective-mobile.ru/#services")
    def test_click_employment(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.click_employment()
        expected_url ='https://www.effective-mobile.ru/#services'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}" 
    
    @allure.title("Тест: при нажатии на элемент 'Услуги: Консультация' был совершен переход на https://www.effective-mobile.ru/#contact")
    def test_click_consultation(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.click_consultation()
        expected_url ='https://www.effective-mobile.ru/#contact'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"
    
    @allure.title("Тест: при нажатии на элемент 'Политика конфиденциальности' был совершен переход на https://www.effective-mobile.ru/#")
    def test_click_consultation(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.click_privacy_policy()
        expected_url ='https://www.effective-mobile.ru/#'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"   
   
    @allure.title("Тест: при нажатии на элемент 'Условия использования' был совершен переход на https://www.effective-mobile.ru/#")
    def test_click_consultation(self, driver):
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
         # Act
        main_page.click_terms_of_use()
        expected_url ='https://www.effective-mobile.ru/#'
        actual_url = main_page.get_current_url()
        # Assert
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"  
    
    @allure.title("Тест: наличие и корректность текста ссылки на email в футере")
    def test_email_address_in_footer(self, driver): 
        # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
        # Act
        main_page.scroll_to_element_about_us()
        # Assert
        assert main_page.is_email_present(), "Ссылка на email не найдена в футере."
        assert main_page.get_email_text() == "hrdepartment@effmobile.ru", \
            f"Некорректный текст email. Ожидался 'hrdepartment@effmobile.ru', получен '{main_page.get_email_text()}'."
        
    @allure.title("Тест: наличие и корректность текста ссылки на Telegram в футере")
    def test_telegram_link_in_footer(self, driver): 
         # Arrange
        main_page = MainPage(driver) 
        main_page.open_main_page()
        # Act
        main_page.scroll_to_element_about_us()
        # Assert
        assert main_page.is_telegram_present(), "Ссылка на Telegram не найдена в футере."
        assert main_page.get_telegram_text() == "@assistant_em", \
            f"Некорректный текст Telegram. Ожидался '@assistant_em', получен '{main_page.get_telegram_text()}'."

