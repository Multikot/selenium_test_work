from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


opt = webdriver.ChromeOptions()
# Запуск в полноэкранном режиме
opt.add_argument("start-maximized")
# Объявим константу с ссылкой. Возможно, она пригодится в других функциях.
URL: str = 'https://yandex.ru'
# Драйвер объявим в глобальной видимости по той же причине
driver = webdriver.Chrome(options=opt)


def go_to_yandex() -> None:
    """Переход по ссылке из URL"""
    driver.get(URL)
    driver.implicitly_wait(10)


def check_searcher_suggest() -> None:
    """ - Поиск input панели
        - Ввод текста
        - Поиск элементов подскази
        - Вывод списка рекомендаций в консоль
    """
    # Вариант поиска элемента через XPATH
    search = driver.find_element(By.XPATH, '//*[@id="text"]')
    search.send_keys('Тензор')
    # Проверяем таблицу с подсказками
    # Счетчик нужен для вывода данных в консоль
    counter: int = 0
    # Вариант поиска элемента через CLASS_NAME
    # Объявим suggest_list, которая будет ссылаться на список из подсказок
    suggests_list: list = driver.find_elements(By.CLASS_NAME,
                                               'mini-suggest__item')
    # Перебираем каждый элемент suggest и выводим data-text
    for check in suggests_list:
        counter += 1
        print(f'Ссылка {counter}', check.get_attribute('data-text'), sep=': ')
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)


def check_rezult_href() -> None:
    """Поиск адреса tensor.ru в результатах."""
    # Объявим лист с результатами поиска, ordering = 5
    result_list: list = driver.find_elements(
                        By.XPATH,
                        '//*[@id="search-result"]/li/div/div/div/div/a')[:5]
    # Для каждого поискового запроса проверяем наличие ссылки 'tensor.ru'
    driver.implicitly_wait(10)
    print('\n', 'Проверка ссылок в резултатах поиска', '\n', sep='')
    for chek in result_list:
        if 'tensor.ru' in chek.get_attribute('href'):
            print('Yes', chek.get_attribute('href'), sep=': ')
        else:
            print('No')


def main() -> None:
    """Главная функция, которая запустит скрипт."""
    go_to_yandex()
    check_searcher_suggest()
    check_rezult_href()
    driver.quit()


if __name__ == '__main__':
    main()
