import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from Class.Calculator import CalcPage

@allure.id("Calculator")
@allure.epic("калькулятор")
@allure.severity("blocker")
@allure.suite("Тесты на работу с калькулятором")
@allure.story("Выполнение математических операций на калькуляторе")
@allure.title("Сложение чисел на калькуляторе")
@allure.feature("CREATE")
def test_form_calculator():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экзампляр класса CalculatorPage"):
        calculator_page = CalcPage(driver)

    calculator_page.delay()
    calculator_page.sum_of_the_numbers()
    calculator_page.get_result()
    result = calculator_page.get_result()
    with allure.step("Проверка результата сложения"):
        assert result == "15", f"Результат сложения неверен! Получено: {result}"
    calculator_page.close_driver()