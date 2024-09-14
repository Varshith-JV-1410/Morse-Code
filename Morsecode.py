import tkinter as tk

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

# Reverse the Morse code dictionary for decryption
reverse_morse_code = {value: key for key, value in morse_code.items()}


def generate_morse_code():
    text = input_text.get("1.0", tk.END).upper().strip()
    morse_text = ""
    for char in text:
        if char in morse_code:
            morse_text += morse_code[char] + " "
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, morse_text)


def decrypt_morse_code():
    morse_text = input_text.get("1.0", tk.END).strip().split(" ")
    text = ""
    for code in morse_text:
        if code in reverse_morse_code:
            text += reverse_morse_code[code]
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text)


# Create the GUI window
window = tk.Tk()
window.title("Morse Code Generator & Decrypter")

# Create input and output text areas
input_text = tk.Text(window, height=5, width=50)
input_text.pack()

output_text = tk.Text(window, height=5, width=50)
output_text.pack()

# Create buttons
generate_button = tk.Button(window, text="Generate Morse Code", command=generate_morse_code)
generate_button.pack()

decrypt_button = tk.Button(window, text="Decrypt Morse Code", command=decrypt_morse_code)
decrypt_button.pack()

# Run the GUI
window.mainloop()