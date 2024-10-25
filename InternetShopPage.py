import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from Class.InternetShop import InternetShopPage

@allure.id("InternetShop")
@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.suite("Тесты на работу с интернет-магазином")
def test_form_internet_mag():
    # Открытие веб-страницы Chrome
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создание переменной, которая хранит экземпляр класса InternetShopPage"):
        internet_shop_page = InternetShopPage(driver)
    
    internet_shop_page.authorization("standard_user", "secret_sauce")
    to_be = internet_shop_page.add_products()
    internet_shop_page.go_to_cart()
    internet_shop_page.personal_data("Andrey", "Bryukhanov", "191194")
    
    as_is = internet_shop_page.total_cost()
    
    with allure.step("Проверить, что ожидаемая и фактическая стоимость равны"):
        assert as_is == to_be

    internet_shop_page.close()