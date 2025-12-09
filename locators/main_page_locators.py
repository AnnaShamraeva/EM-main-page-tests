from selenium.webdriver.common.by import By


class MainPageLocators:
    
    #Footer
    
    # Компания:
    ABOUT_US = (By.XPATH, "//a[@href='#about' and normalize-space(.)='О нас']") # Компания: О нас
    VACANSII = (By.XPATH, '//a[@href="#specializations"]') # Компания: Вакансии
    REVIEW = (By.XPATH, '//a[@href="#testimonials"]') # Компания: Отзывы
    CONTACT = (By.XPATH, '//a[@href="#contact" and text()="Контакты"]') # Компания: Контакты
    
    # Услуги
    OUTSTAFF = (By.XPATH, '//a[@href="#services" and text()="Аутстафф"]') # Услуги: Аутстафф
    EMPLOYMENT = (By.XPATH, '//a[@href="#services" and text()="Трудоустройство"]') # Услуги: Трудоустройство
    CONSULTATION = (By.XPATH, '//a[@href="#contact" and text()="Консультация"]')# Услуги: Консультация
    
    # Политика конфиденциальности
    PRIVACY_POLICY = (By.XPATH, '//a[@href="#" and text()="Политика конфиденциальности"]') 
    # Условия использования
    TERMS_OF_USE = (By.XPATH, '//a[@href="#" and text()="Условия использования"]') 


    LOGO_EM = (By.XPATH, "//*[local-name()='g' and contains(@clip-path, 'clipPath')]") # Локатор для логотипа
   
    # Контакты
    EMAIL_ADRESS = (By.XPATH, '//a[@href="mailto:hrdepartment@effmobile.ru" and text()="hrdepartment@effmobile.ru"]') 
    TELEGRAM = (By.XPATH, '//a[@href="tg://resolve?domain=assistant_em" and text()="@assistant_em"]') 
  
