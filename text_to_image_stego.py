from PIL import Image

def text_to_bin(message):
    bin_message = []

    for i in message:
        bin_message.append(format(ord(i), '08b'))
    return bin_message

def LSB_text(pix, message_list):
    #datalist = text_to_bin(data)
    lendata = len(message_list)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]

        # Pixel value should be made odd for 1 and even for 0
        for j in range(0, 8):
            if message_list[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1

            elif message_list[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1

        # Eighth pixel of every set tells whether to stop ot read further.
        # 0 means keep reading; 1 means the message is over.
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def hide_text_to_image(normal_image, message, output_image, criptare = "Nu"):
    image = Image.open(normal_image, 'r')
    stego_image = image.copy()

    width = stego_image.size[0]
    (x, y) = (0, 0)
    num_pixels = stego_image.size[0] * stego_image.size[1]

    if criptare == "Nu":
        max_message_length = num_pixels * 3 // 8
        message += "STOP"

        if len(message) == 0:
            raise ValueError("Mesajul nu poate fi nul.")
        if len(message) * 8 > max_message_length:
            raise ValueError("Mesajul este prea lung pentru imaginea data. Alege o imagine mai mare sau un mesaj mai scurt.")

        for pixel in LSB_text(stego_image.getdata(), text_to_bin(message)):
            stego_image.putpixel((x, y), pixel)
            if x == width - 1:
                x = 0
                y += 1
            else:
                x += 1
        stego_image.save(output_image)

    elif criptare == "Da":
        max_message_length = len(message)

def extract_text_from_image(stego_image):
    image = Image.open(stego_image, 'r')

    cleartext = ''
    imgdata = iter(image.getdata())

    stop_sign = "STOP"

    while True:
        pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]

        binstr = ''
        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'
        if cleartext[-len(stop_sign):] == stop_sign:
            break
        cleartext += chr(int(binstr, 2))

    return cleartext[:-4]


if __name__ == '__main__':
    source_image = "lion.png"
    message = "11001110001001101101000110100001011000001101100000001001000000000111111111001110011101010101100100010100110011110011110100010001101100000110011000110010001101101110110010100100110001100101101011001110011011110011101001101101001001111001100011010111110010101110011010001111011010000000100111101100100110110010000011101110100101110111011101100010000001011110011101100111111100000111110111110101110001100111000000111110011000011100010011001011100100101011101010011000000001110011111100010000011101101001011010100011"
    print(len(message))
    destination_image = "testes.png"

    a = int(input("1. Encode\n2. Decode\n"))
    if a == 1:
        hide_text_to_image(source_image, message, destination_image)
    elif a == 2:
        print(extract_text_from_image(destination_image))

