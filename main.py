import tkinter as tk
from tkinter import filedialog
from PIL import UnidentifiedImageError
from encryption_aes import generate_random_key, encrypt_message, decrypt_message, encrypt_image, decrypt_image
from text_to_image_stego import hide_text_to_image, extract_text_from_image
from image_to_image_stego import hide_image_in_image, extract_image_from_image
from video_stego import extract_frame_from_video

def place_random_key():
    secret_key_entry_hide.delete(0, tk.END)
    secret_key_entry_hide.insert(tk.END, generate_random_key())


def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(tk.END, file_path)


def check_valid_key(string):
    if len(string) != 32:
        return False
    for char in string:
        if char not in "0123456789abcdefghijklmnopqrstuvwxyz":
            return False
    return True


def apply_method():
    if current_menu_choice == "hide":

        hide_type_value = hide_type.get()
        cover_type_value = hiding_type.get()
        source_path = file_entry.get()
        cover_path = cover_entry.get()
        encryption_option_value = encryption_option_hide.get()
        secret_key = secret_key_entry_hide.get()
        final_path = final_entry.get()

        # Check the values and perform the hide operation
        if hide_type_value == "Text":
            if cover_type_value == "Image":
                if encryption_option_value == "Da":
                    # TEXT -> IMAGINE cu CRIPTARE
                    if check_valid_key(secret_key):
                        # Cheie buna
                        error_label_hide_invalid_key.config(text="")
                        try:
                            process_label.config(text="Se proceseaza...")
                            with open(source_path, "r") as file:
                                message = file.read()
                            error_label_hide_invalid_file.config(text="")

                            # Criptare mesaj cu cheie
                            message = encrypt_message(bytes.fromhex(secret_key), message)
                            message = str(message)

                            hide_text_to_image(cover_path, message, final_path)
                            process_label.config(text="Gata!")
                        except FileNotFoundError:
                            print("Fișierul nu a fost găsit.")
                            error_label_hide_invalid_file.config(text="Fișierul nu a fost găsit.")
                        except IOError:
                            print("Eroare input.")
                            error_label_hide_invalid_file.config(text="Eroare input.")
                        except ValueError as e:
                            print(str(e))
                            error_label_hide_invalid_file.config(text=str(e))

                    else:
                        # Eroare, cheie incorecta
                        error_label_hide_invalid_key.config(text="Cheie invalidă")
                else:
                    # TEXT -> IMAGINE FARA criptare
                    try:
                        process_label.config(text="Se proceseaza...")
                        with open(source_path, "r") as file:
                            message = file.read()
                        error_label_hide_invalid_file.config(text="")

                        hide_text_to_image(cover_path, message, final_path)
                        process_label.config(text="Gata!")
                    except FileNotFoundError:
                        print("Fișierul nu a fost găsit.")
                        error_label_hide_invalid_file.config(text="Fișierul nu a fost găsit.")
                    except IOError:
                        print("Eroare input.")
                        error_label_hide_invalid_file.config(text="Eroare input.")
                    except ValueError as e:
                        print(str(e))
                        error_label_hide_invalid_file.config(text=str(e))
            else:
                if encryption_option_value == "Da":
                    print("Perform text hiding in video logic with encryption")
                    # Perform text hiding in video logic with encryption
                    if check_valid_key(secret_key):
                        ## Cheie corecta
                        error_label_hide_invalid_key.config(text="")

                        pass
                    else:
                        # Eroare, cheie incorecta
                        error_label_hide_invalid_key.config(text="Cheie invalidă")
                else:
                    # Text -> Video FARA criptare

                    try:
                        process_label.config(text="Se proceseaza...")
                        with open(source_path, "r") as file:
                            message = file.read()
                        error_label_hide_invalid_file.config(text="")

                        hide_text_to_image(cover_path, message, final_path)
                        process_label.config(text="Gata!")
                    except FileNotFoundError:
                        print("Fișierul nu a fost găsit.")
                        error_label_hide_invalid_file.config(text="Fișierul nu a fost găsit.")
                    except IOError:
                        print("Eroare input.")
                        error_label_hide_invalid_file.config(text="Eroare input.")
                    except ValueError as e:
                        print(str(e))
                        error_label_hide_invalid_file.config(text=str(e))

                    pass
        elif hide_type_value == "Image":
            # Perform image hiding logic
            if cover_type_value == "Image":
                if encryption_option_value == "Da":
                    # Ascunde Imagine -> Imagine cu criptare
                    if check_valid_key(secret_key):
                        # Cheie corecta
                        error_label_hide_invalid_key.config(text="")
                        process_label.config(text="Se proceseaza...")
                        # Criptare imagine
                        encrypted_image, enc_img_path = encrypt_image(source_path, bytes.fromhex(secret_key), final_path)
                        #hide_image_in_image(enc_img_path, cover_path, final_path)

                        process_label.config(text="Gata!")
                    else:
                        # Eroare, cheie incorecta
                        error_label_hide_invalid_key.config(text="Cheie invalidă")

                else:
                    # Ascunde Imagine -> Imagine fara criptare
                    try:
                        process_label.config(text="Se proceseaza...")
                        hide_image_in_image(source_path, cover_path, final_path)
                        process_label.config(text="Gata!")

                    except FileNotFoundError:
                        print("Fișierul nu a fost găsit.")
                        error_label_hide_invalid_file.config(text="Fișierul nu a fost găsit.")
                    except UnidentifiedImageError:
                        print("Imaginea este invalidă.")
                        error_label_hide_invalid_file.config(text="Imaginea este invalidă.")
                    except IOError:
                        print("Eroare input.")
                        error_label_hide_invalid_file.config(text="Eroare input.")
                    except ValueError as e:
                        print(str(e))
                        error_label_hide_invalid_file.config(text=str(e))

            elif cover_type_value == "Video":
                if encryption_option_value == "Da":
                    print("Imagine -> video cu criptare")
                    if check_valid_key(secret_key):
                        # Cheie corecta
                        error_label_hide_invalid_key.config(text="")

                        ### Stego proces

                        pass
                    else:
                        # Eroare, cheie incorecta
                        error_label_hide_invalid_key.config(text="Cheie invalidă")

                else:
                    print("Imagine -> video fara criptare")

    elif current_menu_choice == "extract":
        # Extract
        file_path = file_extract_browse_1.get()
        extract_from_type_value = extract_type.get() # Din ce extragi
        extract_what_type_value = extract_what_type.get() # Ce extragi
        final_path = file_extract_destination.get()
        encryption_option_value = encryption_option.get()
        secret_key = secret_key_entry.get()

        if extract_from_type_value == "Imagine":
            if extract_what_type_value == "Imagine":
                if encryption_option_value == "Da":
                    # Exrage Imagine -> Imagine CU criptare
                    if check_valid_key(secret_key):
                        decrypt_image(file_path, bytes.fromhex(secret_key), final_path)
                    else:
                        error_label_hide_invalid_key.config(text="Cheie invalidă")
                else:
                    # Extrage Imagine -> Imagine fara criptare
                    process_label.config(text="Se proceseaza...")
                    extract_image_from_image(file_path, final_path)
                    process_label.config(text="Gata!")
            else:
                if encryption_option_value == "Da":
                    # Extrage Imagine -> Text cu criptare
                    process_label.config(text="Se proceseaza...")
                    ciphertext = extract_text_from_image(file_path)
                    cleartext = decrypt_message(bytes.fromhex(secret_key), eval(ciphertext))

                    with open(final_path, 'w') as file:
                        file.write(cleartext)
                        file.close()
                    process_label.config(text="Gata!")
                else:
                    # extrage imagine -> text fara criptare
                    process_label.config(text="Se proceseaza...")
                    message = extract_text_from_image(file_path)
                    with open(final_path, 'w') as file:
                        file.write(message)
                    process_label.config(text="Gata!")

        elif extract_from_type_value == "Video": #############
            if extract_what_type_value == "Imagine":
                if encryption_option_value == "Da":
                    # Video -> Imagine CU criptare
                    img = extract_frame_from_video(file_path, 0)
                    extract_image_from_image(img, final_path)
                else:
                    # Video -> imagine FARA criptare
                    img = extract_frame_from_video(file_path, 0)
                    extract_image_from_image(img, final_path)

            elif extract_what_type_value == "Text":
                if encryption_option_value == "Da":
                    # Video -> Text CU criptare
                    img = extract_frame_from_video(file_path, 0)
                    with open(final_path, 'w') as file:
                        file.write(extract_text_from_image(img))
                        file.close()
                else:
                    # Video -> Text fara criptare
                    img = extract_frame_from_video(file_path, 0)
                    with open(final_path, 'w') as file:
                        file.write(extract_text_from_image(img))
                        file.close()

current_menu_choice = "hide"

def switch_menu(menu_choice):
    global current_menu_choice
    current_menu_choice = menu_choice

    if menu_choice == "hide":
        hide_buttons_frame.pack()
        extract_buttons_frame.pack_forget()
        decryption_frame.pack_forget()
        apply_button.pack(side=tk.BOTTOM)
    elif menu_choice == "extract":
        hide_buttons_frame.pack_forget()
        extract_buttons_frame.pack()
        decryption_frame.pack()
        apply_button.pack(side=tk.BOTTOM)


def toggle_secret_key_entry(*args):
    if encryption_option.get() == "Da":
        secret_key_entry.config(state="normal")
    else:
        secret_key_entry.config(state="disabled")


def toggle_secret_key_entry_hide(*args):
    if encryption_option_hide.get() == "Da":
        secret_key_entry_hide.config(state="normal")
        generate_key_button_hide.config(state="normal")
    else:
        secret_key_entry_hide.config(state="disabled")
        generate_key_button_hide.config(state="disabled")


root = tk.Tk()
root.title("StegOS")
#root.geometry("500x670")

# Create a frame for the menu choice
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

# Add buttons for the menu choice
hide_button = tk.Button(menu_frame, text="Ascunde", command=lambda: switch_menu("hide"))
hide_button.pack(side=tk.LEFT, padx=5)
discover_button = tk.Button(menu_frame, text="Extrage", command=lambda: switch_menu("extract"))
discover_button.pack(side=tk.LEFT, padx=5)

# Create a frame for the hide buttons section
hide_buttons_frame = tk.Frame(root)

# Add buttons for the hide buttons section
section1_frame = tk.LabelFrame(hide_buttons_frame, text="Ce tip de fișier ascunzi?")
section1_frame.pack(pady=10, padx=10, fill="both", expand=True)

hide_type = tk.StringVar(value="Text")  # Set the default option to "Text"
text_radio = tk.Radiobutton(section1_frame, text="Text", variable=hide_type, value="Text")
text_radio.pack(pady=5, side=tk.LEFT)
image_radio = tk.Radiobutton(section1_frame, text="Imagine", variable=hide_type, value="Image")
image_radio.pack(pady=5, side=tk.LEFT)

# stil
#text_radio.config(font=("Arial", 12), fg="blue", bg="lightgray")
# background
# root.configure(bg="lightblue")
# section1_frame.configure(bg="lightblue")

section2_frame = tk.LabelFrame(hide_buttons_frame, text="În ce tip de fișier ascunzi?")
section2_frame.pack(pady=10, padx=10, fill="both", expand=True)

hiding_type = tk.StringVar(value="Image")
image_radio = tk.Radiobutton(section2_frame, text="Imagine", variable=hiding_type, value="Image")
image_radio.pack(pady=5, side=tk.LEFT)
video_radio = tk.Radiobutton(section2_frame, text="Videoclip (Beta)", variable=hiding_type, value="Video")
video_radio.config(state="disabled")
video_radio.pack(pady=5, side=tk.LEFT)

section3_frame = tk.LabelFrame(hide_buttons_frame, text="Alege fișierul de ascuns")
section3_frame.pack(pady=10, padx=10, fill="both", expand=True)

file_entry = tk.Entry(section3_frame, width=40)
file_entry.pack(pady=5, side=tk.LEFT)
browse_button = tk.Button(section3_frame, text="Alege", command=lambda: browse_file(file_entry))
browse_button.pack(pady=5, padx=5, side=tk.LEFT)

section4_frame = tk.LabelFrame(hide_buttons_frame, text="Fișier de acoperire")
section4_frame.pack(pady=10, padx=10, fill="both", expand=True)

cover_entry = tk.Entry(section4_frame, width=40)
cover_entry.pack(pady=5, side=tk.LEFT)
browse_button = tk.Button(section4_frame, text="Alege", command=lambda: browse_file(cover_entry))
browse_button.pack(pady=5, padx=5, side=tk.LEFT)

section5_frame = tk.LabelFrame(hide_buttons_frame, text="Criptare")
section5_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Create a variable to store the encryption option for Hide menu
encryption_option_hide = tk.StringVar(value="Nu")

# Create a frame for the secret key input in Hide menu
secret_key_frame_hide = tk.LabelFrame(section5_frame, text="Folosești criptare?")
secret_key_frame_hide.pack(pady=10, padx=10, fill="both", expand=True)

# Add radio buttons for Yes/No options in Hide menu
yes_radio_hide = tk.Radiobutton(secret_key_frame_hide, text="Da", variable=encryption_option_hide, value="Da")
yes_radio_hide.pack(pady=5, side=tk.LEFT)
no_radio_hide = tk.Radiobutton(secret_key_frame_hide, text="Nu", variable=encryption_option_hide, value="Nu")
no_radio_hide.pack(pady=5, side=tk.LEFT)

# Create a frame for the secret key input in Hide menu
secret_key_inner_frame_hide = tk.Frame(secret_key_frame_hide)
secret_key_inner_frame_hide.pack(pady=10, padx=10)

# Add a label for "Cheia secretă"
secret_key_label_hide = tk.Label(secret_key_inner_frame_hide, text="Cheia secretă:")
secret_key_label_hide.pack(side=tk.LEFT)

# Add a text field for the secret key in Hide menu
secret_key_entry_hide = tk.Entry(secret_key_inner_frame_hide, width=40, state="disabled")
secret_key_entry_hide.pack(pady=5, side=tk.LEFT)

generate_key_button_hide = tk.Button(secret_key_inner_frame_hide, text="Generează cheie", command=place_random_key)
generate_key_button_hide.pack(pady=5, padx=5, side=tk.LEFT)

# Bind the toggle_secret_key_entry_hide function to the encryption option variable in Hide menu
encryption_option_hide.trace("w", toggle_secret_key_entry_hide)

section6_frame = tk.LabelFrame(hide_buttons_frame, text="Fișier final")
section6_frame.pack(pady=10, padx=10, fill="both", expand=True)

final_entry = tk.Entry(section6_frame, width=40)
final_entry.pack(pady=5)


# Pack the hide buttons frame initially
hide_buttons_frame.pack()

# Create the Apply button
apply_button = tk.Button(root, text="Aplică", command=apply_method)
apply_button.pack(pady=10)

# Create a frame for the discover buttons section
extract_buttons_frame = tk.Frame(root)

# Add buttons for the discover buttons section
section6_frame = tk.LabelFrame(extract_buttons_frame, text="Din ce tip de fișier extragi?")
section6_frame.pack(pady=10, padx=10, fill="both", expand=True)

extract_type = tk.StringVar(value="Imagine")
text_radio = tk.Radiobutton(section6_frame, text="Imagine", variable=extract_type, value="Imagine")
text_radio.pack(pady=5, side=tk.LEFT)
image_radio = tk.Radiobutton(section6_frame, text="Videoclip (Beta)", variable=extract_type, value="Videoclip")
image_radio.config(state="disabled")
image_radio.pack(pady=5, side=tk.LEFT)


section_extra_frame = tk.LabelFrame(extract_buttons_frame, text="Ce extragi?")
section_extra_frame.pack(pady=10, padx=10, fill="both", expand=True)

extract_what_type = tk.StringVar(value="Text")
text_radio_extract_what = tk.Radiobutton(section_extra_frame, text="Text", variable=extract_what_type, value="Text")
text_radio_extract_what.pack(pady=5, side=tk.LEFT)
image_radio_extract_what = tk.Radiobutton(section_extra_frame, text="Imagine", variable=extract_what_type, value="Imagine")
image_radio_extract_what.pack(pady=5, side=tk.LEFT)


section7_frame = tk.LabelFrame(extract_buttons_frame, text="Alege fișierul din care extragi mesajul.")
section7_frame.pack(pady=10, padx=10, fill="both", expand=True)

file_extract_browse_1 = tk.Entry(section7_frame, width=40)
file_extract_browse_1.pack(pady=5, side=tk.LEFT)
browse_button_extract1 = tk.Button(section7_frame, text="Alege", command=lambda: browse_file(file_extract_browse_1))
browse_button_extract1.pack(pady=5, padx=5, side=tk.LEFT)

# DECRYPT
# Create a frame for the decryption section
decryption_frame = tk.LabelFrame(extract_buttons_frame, text="Decriptare")
decryption_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Add the encryption question label
decryption_label = tk.Label(decryption_frame, text="Mesajul ascuns este și criptat?")
decryption_label.pack(pady=5)

# Create a variable to store the encryption option
encryption_option = tk.StringVar(value="Nu")

# Add radio buttons for Yes/No options
yes_radio = tk.Radiobutton(decryption_frame, text="Da", variable=encryption_option, value="Da")
yes_radio.pack(pady=5, side=tk.LEFT)
no_radio = tk.Radiobutton(decryption_frame, text="Nu", variable=encryption_option, value="Nu")
no_radio.pack(pady=5, side=tk.LEFT)

# Create a frame for the secret key input
secret_key_frame = tk.LabelFrame(decryption_frame, text="Cheia secretă")
secret_key_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Add a text field for the secret key
secret_key_entry = tk.Entry(secret_key_frame, width=40, state="disabled")
secret_key_entry.pack(pady=5)


section7_frame = tk.LabelFrame(extract_buttons_frame, text="Fișierul în care extragi mesajul.")
section7_frame.pack(pady=10, padx=10, fill="both", expand=True)

file_extract_destination = tk.Entry(section7_frame, width=40)
file_extract_destination.pack(pady=5)

def toggle_secret_key_entry(*args):
    if encryption_option.get() == "Da":
        secret_key_entry.config(state="normal")
    else:
        secret_key_entry.config(state="disabled")


# Bind the toggle_secret_key_entry function to the encryption option variable
encryption_option.trace("w", toggle_secret_key_entry)

# Hide the discover buttons frame initially
extract_buttons_frame.pack_forget()

# Erori si mesaje de procesare
error_frame = tk.Frame(root)
error_frame.pack(pady=10)
error_label_hide_invalid_key = tk.Label(secret_key_inner_frame_hide, fg="red")
error_label_hide_invalid_key.pack(pady=5, padx=5, side=tk.LEFT)
error_label_hide_invalid_file = tk.Label(error_frame, text="", fg="red")
error_label_hide_invalid_file.pack()
process_label = tk.Label(error_frame, text="", fg="green")
process_label.pack()

root.update()
content_width = root.winfo_reqwidth()
content_height = root.winfo_reqheight()
window_width = content_width + 10
window_height = content_height + 10
root.geometry(f"{window_width}x{window_height}")

root.mainloop()
