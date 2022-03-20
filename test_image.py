from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By


opt = webdriver.ChromeOptions()
# Запуск в полноэкранном режиме
opt.add_argument("start-maximized")
# Объявим константу с ссылкой. Возможно, она пригодится в других функциях.
URL: str = 'https://yandex.ru'
# Драйвер объявим в глобальной видимости по той же причине
driver = webdriver.Chrome(options=opt)


def go_to_yandex(URL) -> Any:
    """Переход по ссылке из URL."""
    driver.get(URL)
    return driver.implicitly_wait(10)


def go_to_img_yandex() -> None:
    """Переход на страницу картинок."""
    # Объявим xpath внутри функции, чтобы уложиться в ограничения имволов 79
    xpath_im = '/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[4]/a'
    # Переход по картинке
    img_button: str = driver.find_element(By.XPATH, xpath_im)
    img_url: str = img_button.get_attribute('href')
    # Проверим, есть ли в ссылке yandex.ru/images
    if 'yandex.ru/images' in img_url:
        print('Yes, yandex.ru/images')
    else:
        raise('Мы попали куда-то не туда')
    return driver.get(img_url)


def click_to_image_group() -> None:
    """Клик по картинке"""
    # Сохраняем полный xpath
    img_xpath: str = '/html/body/div[3]/div[2]/div[1]/div/div/div[1]/a/div[1]'
    # Находим нужный элемент
    img_click: str = driver.find_element(By.XPATH, img_xpath)
    driver.implicitly_wait(10)
    # Кликаем
    return img_click.click()


def search_attrebute():
    # Находим класс
    class_attrebute = driver.find_element(By.CLASS_NAME, 'MMImage-Preview')
    # Извлекаем прямую ссылку на картинку
    src_attrebute = class_attrebute.get_attribute('src')
    return src_attrebute


def click_to_image():
    # Поиск первого элемента
    first_element: str = driver.find_element(By.CLASS_NAME, 'serp-item__link')
    # Сохраняем ссылку и переходим по ней
    attrebute_link: str = first_element.get_attribute('href')
    driver.get(attrebute_link)
    # полный xpath до правой кнопки
    btn_right = ('/html/body/div[12]/div[2]/div'
                 + '/div/div/div[3]/div/div[2]/div[1]/div[4]')
    # Находим правую кнопку
    driver.implicitly_wait(10)
    button_right = driver.find_element(By.XPATH, btn_right)
    # Находим атрибут src по классу
    attrebute_one = search_attrebute()
    # Кликаем по кнопке
    button_right.click()
    # Находим левую кнопку
    driver.implicitly_wait(10)
    btn_left = ('/html/body/div[12]/div[2]/div'
                + '/div/div/div[3]/div/div[2]/div[1]/div[1]')
    button_left = driver.find_element(By.XPATH, btn_left)
    # Кликаем
    button_left.click()
    # Находим атрибут src по классу после клика
    attrebute_two = search_attrebute()
    print(attrebute_one, attrebute_two)
    assert attrebute_one == attrebute_two, ('Изображения разные')


def main():
    """Запуск скрипта"""
    go_to_yandex(URL)
    go_to_img_yandex()
    click_to_image_group()
    click_to_image()
    driver.quit()


if __name__ == '__main__':
    main()
