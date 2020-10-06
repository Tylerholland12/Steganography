from PIL import Image

def decode_image(file_location):
    encoded_image = Image.open(file_location)
    channel = encoded_image.split()[0]

    height_size = encoded_image.size[0]
    length_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(height_size):
        for j in range(length_size):
            if bin(channel.getpixel((i, j)))[-1] != '1':
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)
    decoded_image.save("decoded_image.png")

decode_image("dog.png")