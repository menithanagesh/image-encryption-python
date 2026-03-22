from PIL import Image

# Encrypt Image
def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Apply encryption formula
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print("Encrypted image saved as", output_image)


# Decrypt Image
def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Apply decryption formula
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print("Decrypted image saved as", output_image)


# Main Program
print("Image Encryption Tool")

key = int(input("Enter encryption key: "))

encrypt_image("input.jpeg", "encrypted.jpg", key)
decrypt_image("encrypted.jpg", "decrypted.jpg", key)