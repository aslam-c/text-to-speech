import PyPDF2
import pyttsx3

def pdfToText():
    pdfreader = PyPDF2.PdfReader(open("./files/python.pdf", "rb"))
    speaker = pyttsx3.init()
    for page_num in range(pdfreader.numPages):
        text = pdfreader.getPage(page_num).extractText()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    speaker.say("Saving content,please wait ")
    speaker.save_to_file(clean_text, './files/python.mp3')
    speaker.runAndWait()
    speaker.stop()


pdfToText()