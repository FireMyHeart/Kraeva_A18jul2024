from ProductsApi import ProductsApi
# import re
from bs4 import BeautifulSoup
import allure


api = ProductsApi('https://altaivita.ru/engine/')
token = 'afe4e648fd7118e098d1d1d7c0bedf55'


@allure.id("SKYPRO-1")
@allure.epic("Алтайвита. API")
@allure.story("Поиск товара")
@allure.feature("Find")
@allure.title("Поиск товара по фразе")
@allure.severity("blocker")
@allure.suite("API тесты на поиск товара")
def test_1():
    resp = api.find_product('шампунь', token)
    with allure.step("Распарсить ответ и найти теги"):
        soup = BeautifulSoup(resp.text, 'html.parser')
        divs_id = soup.findAll('div', class_='js-product')
        divs_text = soup.findAll('div', class_='searchpro__dropdown-entity_name')
    with allure.step("Обозначить пустой список и поместить в него значения атрибута data-product-id, которые являются id товаров"):
        product_ids = []
        for div in divs_id:
            product_ids.append(div.attrs['data-product-id'])
    with allure.step("Ввести пустой список и поместить в него наименования товаров из поисковой выдачи "):
        texts = []
        for item in divs_text:
            span = item.find('span', class_='searchpro-highlighted')
            if span:
                texts.append(span.text)
    with allure.step("Проверить, что товары из поисковой выдачи содержат введенное слово в строку поиска"):
        counter = 0
        for s in texts:
            if 'шампунь' in s.lower():
                counter += 1
    with allure.step("Проверить, что статус-код тела ответа — 200"):
        assert resp.status_code == 200
    with allure.step("Проверить, что в поисковой выдаче есть товары"):
        assert len(divs_id) > 0
    with allure.step("Проверить, что товары в поисковой выдаче соответствуют поисковому запросу"):
        assert counter == len(product_ids)


@allure.id("SKYPRO-2")
@allure.epic("Алтайвита. API")
@allure.story("Добавление товара в корзину")
@allure.feature("Add")
@allure.title("Добавление первого товара из поисковой выдачи в корзину")
@allure.severity("blocker")
@allure.suite("API тесты на работу с корзиной")
def test_2():
    resp = api.find_product('шампунь', token)
    with allure.step("Распарсить ответ и найти id первого товара"):
        soup = BeautifulSoup(resp.text, 'html.parser')
        id = soup.find('div', class_='js-product').attrs['data-product-id']
    result = api.add_to_cart(id, token)
    body = result.json()
    cart = api.get_cart(token)
    with allure.step("Распарсить ответ и найти id товара в корзине"):
        soup = BeautifulSoup(cart.text, 'html.parser')
        cart_items = soup.findAll('div', class_='dropdown-item')
        item_id = cart_items[0].attrs['data-item-product-id']
    with allure.step("Очистка тестового пространства"):
        api.delete_from_cart(id, token)
    with allure.step("Проверить, что статус-код ответа — 200"):
        assert result.status_code == 200
    with allure.step("Проверить, что статус в теле ответа — ok"):
        assert body['status'] == 'ok'
    with allure.step("Количество добавленных товаров в корзину — 1"):
        assert body['new_quantity'] == 1
        assert body['sum_quantity'] == '1'
    with allure.step("Проверить, что в корзине тот товар, который добавлялся в нее"):
        assert item_id == id


@allure.id("SKYPRO-3")
@allure.epic("Алтайвита. API")
@allure.story("Изменение количества товара в корзине")
@allure.feature("Update")
@allure.title("Изменение единиц одного товара в корзине")
@allure.severity("critical")
@allure.suite("API тесты на работу с корзиной")
def test_3():
    resp = api.find_product('шампунь', token)
    with allure.step("Распарсить ответ и найти id товара"):
        soup = BeautifulSoup(resp.text, 'html.parser')
        id = soup.find('div', class_='js-product').attrs['data-product-id']
    api.add_to_cart(id, token).json()
    cart = api.get_cart(token)
    with allure.step("Распарсить ответ и найти id товара в корзине"):
        soup = BeautifulSoup(cart.text, 'html.parser')
        cart_items = soup.findAll('div', class_='dropdown-item')
        cart_id = cart_items[0].attrs['data-item-id']
    q = 3
    result = api.change_quantity(q, cart_id, token)
    body = result.json()
    cart2 = api.get_cart(token)
    with allure.step("Распарсить ответ и найти количество товара в корзине и общую сумму"):
        soup = BeautifulSoup(cart2.text, 'html.parser')
        total_q = soup.find('div', class_='sum').text
        total_q = total_q.replace(' ', '').replace('\n', '').replace('шт.', '')
        total_sum = soup.find('span', class_='dropdown-total').text
        total_sum = total_sum.replace(' ', '').replace('\n', '').replace('₽', '')
    with allure.step("Очистка тестового пространства"):
        api.delete_from_cart(id, token)
    with allure.step("Проверить, что статус код изменения количества товара — 200"):
        assert result.status_code == 200
    with allure.step("Проверить, что в ответе на изменение количества единиц товара статус — ок, количество и общая сумма соответствуют количеству добавленных товаров"):
        assert body['status'] == 'ok'
        assert body['sum_quantity'] == str(q)
        assert body['total_quantity_items'] == str(q)
        assert q == int(total_q)
    with allure.step("Проверить, что итогова сумма в корзине соответствует итоговой сумме при изменении количества товаров"):
        assert body['total_cost_items'] == int(total_sum)
