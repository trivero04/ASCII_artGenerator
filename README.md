# ASCII Image Generator

ASCII Image Generator is a Python application for converting any image into ASCII art. This tool manages the nuances of image processing, ensuring that the aspect ratio is maintained for optimal visualization. The output is a text file containing the ASCII characters representing the original image, providing a unique and text-based perspective of your images.

## Features:

- **Custom ASCII Characters**: Use a preset array of ASCII characters for image conversion.
- **Aspect Ratio Correction**: Ensures the output ASCII art maintains the image’s aspect ratio, avoiding any stretch.
- **Error Handling**: Gracefully handles issues, ensuring smooth image processing.
- **Flexible Width**: Option to specify the width of the output ASCII art.
- **File Output**: Automatically saves the ASCII output to a text file for easy viewing and sharing.

## Requirements:

- Python
- PIL library from Python (`pillow`)

## Installation:

To install the necessary library, run the following command:

```bash
pip install pillow
```

## Usage:

Run the script with the desired image path:

```python
if __name__ == '__main__':
    PATH = "path/to/your/image.jpeg"
    ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
    main(PATH, ASCII_DICT=ASCII_CHARS)
```

This will generate the ASCII art and save it to a file named `ascii_image.txt`.

## Customization:

You can customize the ASCII characters used for conversion and specify the width of the output ASCII art.

```python
    ASCII_CHARS = ["@", "#", "S", "&", "8", ":", "*", ".", " "]
    main(PATH, new_width=150, ASCII_DICT=ASCII_CHARS)
```

In the above example, the ASCII art will be generated with a new set of characters and a width of 150.

## Output:

The ASCII art will be written to `ascii_image.txt` in the same directory as the script.
