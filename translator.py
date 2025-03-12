import tkinter as tk
from deep_translator import GoogleTranslator

def translate():
    root.update_idletasks()  # Ensures UI updates before reading text
    
    # Get text input from the Text widget
    text = input_text.get("1.0", tk.END).strip()
    
    # Get language code from entry box
    target_lang = lang_entry.get().strip()

    print(f"DEBUG - Text Entered: '{text}'")  # Debugging output
    print(f"DEBUG - Language Code Entered: '{target_lang}'")  # Debugging output

    # Check if text is missing
    if not text:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "⚠️ Please enter text to translate.")
        return

    # Check if language code is missing
    if not target_lang:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "⚠️ Please enter a target language code (e.g., 'fr').")
        return

    try:
        # Perform translation
        translator = GoogleTranslator(target=target_lang)
        translated_text = translator.translate(text)

        print(f"DEBUG - Translated Text: '{translated_text}'")  # Debugging output

        # Display translated text
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"❌ Error: {str(e)}")

# Create the main GUI window
root = tk.Tk()
root.title("Language Translator")
root.geometry("450x400")

# Input Text Label & Box
tk.Label(root, text="Enter Text:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Target Language Label & Entry Box
tk.Label(root, text="Enter Target Language Code (e.g., 'fr' for French):").pack()
lang_entry = tk.Entry(root)
lang_entry.pack()

# Translate Button
tk.Button(root, text="Translate", command=translate).pack()

# Output Label & Box
tk.Label(root, text="Translated Text:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Run the GUI
root.mainloop()
