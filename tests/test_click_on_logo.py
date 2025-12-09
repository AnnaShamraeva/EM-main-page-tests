import allure
from curl import Url
from pages.main_page import MainPage


class TestClickOnLogo:
    @allure.title("Тест: при нажатии на логотип Effective Mobile был совершен переход на главную страницу")
    def test_click_on_logo(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.open_main_page()
        # Act
        main_page.click_about_us()
        main_page.click_on_logo()
        # Assert
        assert main_page.get_current_url() == Url.main_page, 'Главная сраница не открылась'

