from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://altaivita.ru/")
        self._driver.implicitly_wait(15)
        driver.maximize_window()

    @allure.step("Добавить в кукис значение токена {cookie}")
    def cookies(self, cookie):
        self._driver.add_cookie(cookie)
        self._driver.refresh()

    @allure.step("Ввести название товара {key} в поисковую строку и выполнить поиск")
    def enter_values(self, key):
        self._driver.find_element(By.CSS_SELECTOR, 'input.searchpro__field-input.js-searchpro__field-input').send_keys(key, Keys.RETURN)
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.breadcrumbs'))
        )
        return self._driver.find_elements(By.CSS_SELECTOR, 'div.product__product-name a span')

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self, items):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product__add_2_0'))
        )
        title = items[2].text
        price = self._driver.find_element(By.CSS_SELECTOR, 'span.price').text.replace('₽', '').replace(' ', '')
        self._driver.find_element(By.CSS_SELECTOR, 'div.product__add_2_0 button').click()
        return {"title": title, "price": price}

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, 'a.header__basket-link.ga_link_to_cart.grid_container_mobile_menu.pdd_cart').click()
        self._driver.find_element(By.CSS_SELECTOR, 'a.dropdown-go-over.link-gray.ga_link_to_cart').click()

    @allure.step("Вернуть название и цену товара, который находится в корзине, а также общую стоимость покупки")
    def check_item(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.basket__name'))
        )
        title = self._driver.find_element(By.CSS_SELECTOR, 'a.basket__name').text
        price = self._driver.find_element(By.CSS_SELECTOR, 'span.js-item-total').text.replace(' ', '').replace('₽', '')
        t_price = self._driver.find_element(By.CSS_SELECTOR, 'span.js-cart_page_total_amount').text.replace('₽', '').replace(' ', '')
        quantity = self._driver.find_element(By.CSS_SELECTOR, 'span.num').text.replace(' ', '')
        return {'title': title, 'price': price, 't_price': t_price, 'quantity': quantity}

    @allure.step("Изменить количество экземпляров на {qntt} в товаре")
    def change_quantity(self, qntt):
        for i in range(qntt-1):
            self._driver.find_element(By.CSS_SELECTOR, 'button.more.js-plus').click()

    @allure.step("Удалить товар из корзины")
    def delete_item(self):
        self._driver.find_elements(By.CSS_SELECTOR, 'button i.fal.fa-times')[2].click()
        return self._driver.find_element(By.CSS_SELECTOR, 'span.js-cart_page_total_amount').text.replace('₽', '').replace(' ', '')
