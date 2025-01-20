import pyttsx3
import PyPDF2
import tkinter as tk
import threading
import time
def extract_text_from_pdf(pdf_path):
     with open("C:/Users/AAC/Desktop/maham/sampletask.pdf", "rb") as file:
      reader = PyPDF2.PdfReader(file)
      text = ""
      for page in reader.pages:
          text += page.extract_text()
      return text
# Function to highlight the current word
def highlight_word(word, start_pos):
    text_display.tag_remove("highlight", "1.0", tk.END)  # Remove previous highlights
    clean_word = word.strip() #remove extra spacing
    pos = text_display.search(clean_word, start_pos, tk.END)  # Start searching from the current position
    if pos:
        end_pos = f"{pos}+{len(clean_word)}c"  # Define end position
        text_display.tag_add("highlight", pos, end_pos)  # Highlight the word
        text_display.tag_config("highlight", background="yellow")  # Highlight style
        text_display.see(pos)
        return end_pos  # Return the end position for the next search
    return start_pos  # If no match is found, return the current position

def read_and_highlight():
    start_pos = "1.0"  # Start from the beginning of the text
    words = pdf_text.split()  # Split text into words
    for word in words:
        start_pos = highlight_word(word, start_pos)  # Highlight the current word and get the next position
        tts_engine.say(word)  # Speak the word
        tts_engine.runAndWait()  # Wait for TTS to finish
       

tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 600)  

pdf_path = ("C:/Users/AAC/Desktop/maham/sampletask.pdf")
pdf_text = extract_text_from_pdf(pdf_path)
def start_reading():
    threading.Thread(target=read_and_highlight).start()
# GUI Setup
app = tk.Tk()
app.title("PDF to Speech with Word Highlighting")
app.geometry("800x600")
# Text Display Box
text_display = tk.Text(app, wrap=tk.WORD, font=("Arial", 14), height=20, width=80)
text_display.insert("1.0", pdf_text)  # Insert the extracted text into the GUI
text_display.pack(pady=10)
# Automatically start reading after the GUI loads
app.after(1000, start_reading)  # Start reading after 1 second
# Run the GUI
app.mainloop()
