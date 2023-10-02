from PIL import Image

ASPECT_RATIO_CORRECTION = 0.55


def resize_image(image, new_width=200):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width) * ASPECT_RATIO_CORRECTION
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image


def grayify(image):
    return image.convert("L")


def pixels_to_ascii(image, ASCII_CHARS):
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str


def main(image_path, new_width=100, ASCII_DICT=None):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image, ASCII_DICT)
    img_width = image.width

    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)


if __name__ == '__main__':
    PATH = "test.jpeg"
    ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
    main(PATH, ASCII_DICT=ASCII_CHARS)
