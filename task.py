#code 2
import pyttsx3
import PyPDF2
#opening the file
pdf_book = open("sampletask.pdf","rb")
#reading the file
reading_pdf = PyPDF2.PdfReader(pdf_book)
#finding number of pages
pages = len(reading_pdf.pages) #we using function to get number of pages.
print(f"The PDF has {pages} pages.")
#we will start a loop
for num in range(pages):
    page = reading_pdf.pages[num]  # Access the page
    text = page.extract_text()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
pdf_book.close()
