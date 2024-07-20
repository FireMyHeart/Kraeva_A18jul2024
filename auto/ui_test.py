from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage
import allure


cookie = {
    'name': 'CID',
    'value': 'afe4e648fd7118e098d1d1d7c0bedf55'
}

@allure.id("SKYPRO-4")
@allure.epic("Алтайвита. UI")
@allure.story("Поиск товара")
@allure.feature("Find")
@allure.title("Поиск товара по фразе")
@allure.severity("blocker")
@allure.suite("UI тесты на поиск товара")
def test_find_book():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    phrase = 'эликсир'
    items = main_page.enter_values(phrase)
    with allure.step("Создать список, внести в него названия товаров из поисковой выдачи и посчитать те, в которых содержится {phrase}"):
        names = []
        counter = 0
        for i in range(2, len(items), 4):
            names.append(items[i].text)
            if phrase.lower() in items[i].text.lower():
                counter += 1
    driver.close
    with allure.step("Проверить, что товары из поисковой выдачи соответствуют введенному значению {phrase} в строку поиска"):
        assert counter == len(names)

@allure.id("SKYPRO-5")
@allure.epic("Алтайвита. UI")
@allure.story("Добавление товара в корзину")
@allure.feature("Add")
@allure.title("Добавление 1 товара из поисковой выдачи в корзину")
@allure.severity("blocker")
@allure.suite("UI тесты на работу с корзиной")
def test_add_to_cart():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.cookies(cookie)
    phrase = 'сашера-мед'
    items = main_page.enter_values(phrase)
    result = main_page.add_to_cart(items)
    main_page.go_to_cart()
    result1 = main_page.check_item()
    main_page.delete_item()
    driver.close
    with allure.step("Проверить, что название и цена добавленного товара в корзине совпадают с названием и ценой товара в корзине"):
        assert result1['title'] == result['title']
        assert result1['price'] == result['price']
        assert result1['price'] == result1['t_price']
        assert result1['quantity'] == '1'

@allure.id("SKYPRO-6")
@allure.epic("Алтайвита. UI")
@allure.story("Изменение единиц одного товара")
@allure.feature("Update")
@allure.title("Увеличение количества единиц одного товара в корзине")
@allure.severity("blocker")
@allure.suite("UI тесты на работу с корзиной")
def test_change_qnnt():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.cookies(cookie)
    phrase = 'кедровый орех'
    items = main_page.enter_values(phrase)
    main_page.add_to_cart(items)
    main_page.go_to_cart()
    result = main_page.check_item()
    q = 3
    main_page.change_quantity(q)
    result1 = main_page.check_item()
    main_page.delete_item()
    driver.close
    with allure.step("Проверить, что суммарная стоимость покупки соответствует цене за {q} единиц товара"):
        assert int(result1['t_price']) == int(result['price']) * q
        assert int(result1['quantity']) == q

@allure.id("SKYPRO-7")
@allure.epic("Алтайвита. UI")
@allure.story("Удаление товара")
@allure.feature("Delete")
@allure.title("Удаление товара из корзины")
@allure.severity("blocker")
@allure.suite("UI тесты на работу с корзиной")
def test_delete_from_cart():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.cookies(cookie)
    phrase = 'крем'
    items = main_page.enter_values(phrase)
    main_page.add_to_cart(items)
    main_page.go_to_cart()
    result = main_page.check_item()
    result1 = main_page.delete_item()
    driver.close
    with allure.step("Проверить, что суммарная стоимость покупки после удаления равна нулю"):
        assert int(result['t_price']) > int(result1)
        assert int(result1) == 0