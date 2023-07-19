import tkinter as tk
from tkinter import filedialog
from encryption_aes import generate_random_key


def place_random_key():
    secret_key_entry_hide.delete(0, tk.END)
    secret_key_entry_hide.insert(tk.END, generate_random_key())


def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(tk.END, file_path)


def apply_method():
    print("Current menu choice:", current_menu_choice)

    if current_menu_choice == "hide":

        hide_type_value = hide_type.get()
        hiding_type_value = hiding_type.get()
        file_path = file_entry.get()
        cover_path = cover_entry.get()
        encryption_option_value = encryption_option_hide.get()
        secret_key = secret_key_entry_hide.get()
        final_path = final_entry.get()

        # Check the values and perform the hide operation
        if hide_type_value == "Text":

            if hiding_type_value == "Image":

                if encryption_option_value == "Da":

                    if secret_key:
                        # Perform hiding with encryption and secret key logic
                        pass
                    else:
                        # Secret key is missing, show an error or take appropriate action
                        pass
                else:
                    # Perform hiding without encryption logic
                    pass
            else:
                # Perform text hiding in video logic
                pass
        else:
            # Perform image hiding logic
            pass

    elif current_menu_choice == "extract":
        # Logic for extraction
        extract_type_value = extract_type.get()
        file_path = file_extract.get()
        encryption_option_value = encryption_option.get()
        secret_key = secret_key_entry.get()

        # Check the values and perform the extraction operation
        if extract_type_value == "Imagine":
            # Perform image extraction logic
            if encryption_option_value == "Da":
                # Perform extraction with encryption logic
                if secret_key:
                    # Perform extraction with encryption and secret key logic
                    pass
                else:
                    # Secret key is missing, show an error or take appropriate action
                    pass
            else:
                # Perform extraction without encryption logic
                pass
        else:
            # Perform video extraction logic
            pass


current_menu_choice = "hide"
def switch_menu(menu_choice):
    global current_menu_choice
    current_menu_choice = menu_choice

    if menu_choice == "hide":
        hide_buttons_frame.pack()
        extract_buttons_frame.pack_forget()
        encryption_frame.pack_forget()
        apply_button.pack(side=tk.BOTTOM)  # Pack the apply button at the bottom
    elif menu_choice == "extract":
        hide_buttons_frame.pack_forget()
        extract_buttons_frame.pack()
        encryption_frame.pack()
        apply_button.pack(side=tk.BOTTOM)  # Show the encryption section when switching to the extract menu


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
root.title("Aplicație")
root.geometry("500x670")

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

section2_frame = tk.LabelFrame(hide_buttons_frame, text="În ce tip de fișier ascunzi?")
section2_frame.pack(pady=10, padx=10, fill="both", expand=True)

hiding_type = tk.StringVar(value="Image")
image_radio = tk.Radiobutton(section2_frame, text="Imagine", variable=hiding_type, value="Image")
image_radio.pack(pady=5, side=tk.LEFT)
video_radio = tk.Radiobutton(section2_frame, text="Videoclip", variable=hiding_type, value="Video")
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
image_radio = tk.Radiobutton(section6_frame, text="Videoclip", variable=extract_type, value="Videoclip")
image_radio.pack(pady=5, side=tk.LEFT)

section7_frame = tk.LabelFrame(extract_buttons_frame, text="Alege fișierul din care extragi mesajul.")
section7_frame.pack(pady=10, padx=10, fill="both", expand=True)

file_extract = tk.Entry(section7_frame, width=40)
file_extract.pack(pady=5, side=tk.LEFT)
browse_button = tk.Button(section7_frame, text="Alege", command=lambda: browse_file(file_extract))
browse_button.pack(pady=5, padx=5, side=tk.LEFT)

# DECRYPT
# Create a frame for the decryption section
encryption_frame = tk.LabelFrame(extract_buttons_frame, text="Decriptare")
encryption_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Add the encryption question label
encryption_label = tk.Label(encryption_frame, text="Mesajul ascuns este și criptat?")
encryption_label.pack(pady=5)

# Create a variable to store the encryption option
encryption_option = tk.StringVar(value="Nu")

# Add radio buttons for Yes/No options
yes_radio = tk.Radiobutton(encryption_frame, text="Da", variable=encryption_option, value="Da")
yes_radio.pack(pady=5, side=tk.LEFT)
no_radio = tk.Radiobutton(encryption_frame, text="Nu", variable=encryption_option, value="Nu")
no_radio.pack(pady=5, side=tk.LEFT)

# Create a frame for the secret key input
secret_key_frame = tk.LabelFrame(encryption_frame, text="Cheia secretă")
secret_key_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Add a text field for the secret key
secret_key_entry = tk.Entry(secret_key_frame, width=40, state="disabled")
secret_key_entry.pack(pady=5)

# Function to enable/disable the secret key entry based on the selected encryption option
def toggle_secret_key_entry(*args):
    if encryption_option.get() == "Da":
        secret_key_entry.config(state="normal")
    else:
        secret_key_entry.config(state="disabled")

# Bind the toggle_secret_key_entry function to the encryption option variable
encryption_option.trace("w", toggle_secret_key_entry)

# Hide the discover buttons frame initially
extract_buttons_frame.pack_forget()

root.update()
content_width = root.winfo_reqwidth()
content_height = root.winfo_reqheight()
window_width = content_width + 10  # Add some padding
window_height = content_height + 10  # Add some padding
root.geometry(f"{window_width}x{window_height}")

root.mainloop()
