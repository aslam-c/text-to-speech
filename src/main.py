import PyPDF2
import pyttsx3

# converts pdf document to audible mp3
# arguments
# documentPath : from where the input is to be taken
# outputAudioPath : audio output file
# voiceSelection : 1 = female (default) , 0 = male

def pdfToText(documentPath, outputAudioPath, voiceSelection=1):
    pdfreader = PyPDF2.PdfReader(open(documentPath, "rb"))
    speaker = pyttsx3.init()
    for page_num in range(pdfreader.numPages):
        text = pdfreader.getPage(page_num).extractText()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[voiceSelection].id)
    speaker.say("Saving content,please wait ")
    speaker.save_to_file(clean_text, outputAudioPath)
    speaker.runAndWait()
    speaker.stop()

pdfToText("./files/inputs/python.pdf", './files/outputs/audio.mp3', 0)
