from PIL import Image

def hide_image_in_image(secret_image_path, cover_image_path, output_image_path):
    secret_image = Image.open(secret_image_path)
    cover_image = Image.open(cover_image_path)
    secret_image = secret_image.resize(cover_image.size)
    secret_image = secret_image.convert("RGB")
    cover_image = cover_image.convert("RGB")
    secret_pixels = secret_image.load()
    cover_pixels = cover_image.load()
    stego_image = Image.new("RGB", cover_image.size)
    stego_pixels = stego_image.load()

    for i in range(cover_image.width):
        for j in range(cover_image.height):
            cover_r, cover_g, cover_b = cover_pixels[i, j]

            secret_r, secret_g, secret_b = secret_pixels[i, j]
            stego_r = (cover_r & 0xF0) | ((secret_r & 0xF0) >> 4)
            stego_g = (cover_g & 0xF0) | ((secret_g & 0xF0) >> 4)
            stego_b = (cover_b & 0xF0) | ((secret_b & 0xF0) >> 4)

            stego_pixels[i, j] = (stego_r, stego_g, stego_b)

    stego_image.save(output_image_path)


def extract_image_from_image(stego_image_path, output_image_path):
    stego_image = Image.open(stego_image_path)
    stego_image = stego_image.convert("RGB")
    stego_pixels = stego_image.load()

    secret_image = Image.new("RGB", stego_image.size)
    secret_pixels = secret_image.load()

    for i in range(stego_image.width):
        for j in range(stego_image.height):
            stego_r, stego_g, stego_b = stego_pixels[i, j]

            secret_r = (stego_r & 0x0F) << 4
            secret_g = (stego_g & 0x0F) << 4
            secret_b = (stego_b & 0x0F) << 4
            secret_pixels[i, j] = (secret_r, secret_g, secret_b)

    secret_image.save(output_image_path)

#hide_image_in_image("aux_enc.png", "imagine_decriptata_out.png", "finalimgenc.png")
# # Usage example
# secret_image_path = "koga.jpg"
# cover_image_path = "outputframe.png"
# output_image_path = "outputframeimage.png"
#
# #hide_image_in_image(secret_image_path, cover_image_path, output_image_path)
# extract_image_from_image("douaimagini2dezarhivat.png", "testdezarhivat.png")

# output_image_path = "arbore_in_fuzzer.png"
# extract_image_from_image("arbore_in_fuzzer.png", "test_extragere_fuzzer.png")