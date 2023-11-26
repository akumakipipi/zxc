from PIL import Image

def red_filter(image):
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            if type(pixel) == int:
                r, g, b = pixel, pixel, pixel
            else:
                r, g, b, _ = pixel
            r = min(255, r + 100)
            image.putpixel((x, y), (r, g, b))
    image.show()
    save_image(image)

def green_filter(image):
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            if type(pixel) == int:
                r, g, b = pixel, pixel, pixel
            else:
                r, g, b, _ = pixel
            g = min(255, g + 100)
            image.putpixel((x, y), (r, g, b))
    image.show()
    save_image(image)

def blue_filter(image):
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            if type(pixel) == int:
                r, g, b = pixel, pixel, pixel
            else:
                r, g, b, _ = pixel
            b = min(255, b + 100)
            image.putpixel((x, y), (r, g, b))
    image.show()
    save_image(image)

def inversion(image):
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            r = 255 - r
            g = 255 - g
            b = 255 - b
            image.putpixel((x, y), (r, g, b))
    image.show()
    save_image(image)

def save_image(image):
    saving = input("Вы хотите сохранить измененное изображение? (да/нет) ").lower()
    if saving == "да":
        waysaving = input(r"Введите путь к папке, в которую нужно сохранить изображение, а также назовите файл и добавьте расширение (Пример: C:\Users\user\Desktop\image.png): ")
        if not waysaving.lower().endswith(('.png', '.jpg', '.jpeg')):
            print("Некорректное расширение файла. Поддерживаемые форматы: .png, .jpg, .jpeg.")
            save_image(image)
            return
        try:
            image.save(waysaving)
            print(f"Файл был успешно сохранен в {waysaving}")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")
    else:
        print("Изображение не будет сохранено.")
def main(image):
    choose_filter = input("Меню фильтров:\n"
          "1: Красный фильтр\n"
          "2: Синий фильтр\n"
          "3: Зелёный фильтр\n"
          "4: Инверсия\n"
          "0: Выход\n"
          "Выберите фильтр: \n")

    if choose_filter == '1':
        red_filter(image)
    elif choose_filter == '2':
        blue_filter(image)
    elif choose_filter == '3':
        green_filter(image)
    elif choose_filter == '4':
        inversion(image)
    elif choose_filter == '0':
        open_image()
    else:
        print("Некорректное значение для ввода.")
        main(image)

def open_image():
    way = input("Введите путь к файлу: ")
    try:
        image = Image.open(way)
        main(image)
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")
        open_image()

print("Добро пожаловать в консольный фоторедактор!")
open_image()