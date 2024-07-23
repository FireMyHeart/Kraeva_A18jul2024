import requests
import allure


class ProductsApi:
    def __init__(self, url):
        self.url = url

    @allure.step("Найти товар {phrase}")
    def find_product(self, phrase, token):
        params_to_add = {
            'LANG_key': 'ru',
            'S_CID': token,
            'search_val': phrase
        }
        resp = requests.get(self.url+'ajax/search/ajax_search_product.php', params=params_to_add)
        return resp

    @allure.step("Добавить товар с id {id} в корзину")
    def add_to_cart(self, id, token):
        data = {
            'product_id': id,
            'S_wh': 1,
            'S_CID': token,
            'S_cur_code': 'rub',
            'quantity': 1
        }
        resp = requests.post(self.url+'cart/add_products_to_cart_from_preview.php', data=data)
        return resp

    @allure.step("Получить содержимое корзины")
    def get_cart(self, token):
        params_to_add = {
            'LANG_key': 'ru',
            'S_wh': 1,
            'S_CID': token,
            'S_cur_code': 'rub'
        }
        resp = requests.get(self.url+'cart/ajax_show_cart_preview.php', params=params_to_add)
        return resp

    @allure.step("Изменить количество единиц на {q} в корзине для товара с id {id}")
    def change_quantity(self, q, id, token):
        data = {
            'itemID': id,
            'quantity': q,
            'action': 'update_quantity',
            'LANG_key': 'ru',
            'S_wh': 1,
            'S_CID': token,
            'S_cur_code': 'rub'
        }
        resp = requests.post(self.url+'cart/action_with_basket_on_cart_page.php', data=data)
        return resp

    @allure.step("Удалить товар c id {id} из корзины")
    def delete_from_cart(self, id, token):
        data = {
            'product_id': id,
            'S_wh': 1,
            'S_CID': token,
            'S_cur_code': 'rub'
        }
        resp = requests.post(self.url+'cart/delete_products_from_cart_preview.php', data=data)
        return resp
