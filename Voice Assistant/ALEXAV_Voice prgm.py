import os
import speech_recognition as sr
import webbrowser
import pyttsx3

print("In Which Mode You want to Operate : Cli OR Voice")
l=input()
pyttsx3.speak("Loading Your Program")
print('LOADING...\n')


from tqdm.auto import tqdm
for i in tqdm(range(1841)) :
    print(" ",end='\r')
    
print('\tLoad Successfull')
print(f'\n\n\n\n\t\t\t\u001b[41mWelcome to my Menu.\u001b[40m')
print("\u001b[44mEnter your requirements,We are listeing ...\u001b[40m\n")
i=1
while i<3 :
    #ch=input()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(' ______________')
        print('\u001b[44m| start saying...\u001b[40m\n')
        audio = r.listen(source)
        print(' _____________________')
        print('\u001b[44m| we got it ,plz wait..\u001b[40m\n')

    ch = r.recognize_google(audio)

    if "date" in ch :
        webbrowser.open("https://www.google.com/search?q=date&oq=date&aqs=chrome..69i57j0l6j46.1097j0j15&sourceid=chrome&ie=UTF-8")

    elif("what" in ch) or ("do" in ch) :
        pyttsx3.speak("Here are things I can do")
        print("\t\u001b[44m list of Operations-\u001b[40m\n")
        print("\tOpen any Gui program" )
        print("\tBrowsing the Internet")
        print("\tRun Applications")
        print("\tChange setting of System")
        print("\tSend Email")
        print("\tTake Notes")

    elif"control" in ch :
        pyttsx3.speak("Opening control pannel")
        os.system("control")

    elif"virtualbox" in ch:
        pyttsx3.speak("Opening virtual box")
        os.system("VirtualBox")

    elif"calculator" in ch:
        pyttsx3.speak("Opening Calculator ")
        #os.system("cls")
        os.system("calc")
    
    elif (("note" in ch) or ("notepad" in ch)):
        pyttsx3.speak("Opening Notepad")
        os.system("Notepad")

    elif"Wikipedia" in ch:
        pyttsx3.speak("Opening Wikipedia")
        #os.system("cls")
        webbrowser.open("https://en.wikipedia.org/wiki/Python_(programming_language")

    elif"Instagram" in ch:
        pyttsx3.speak("Instagram")
        #os.system("cls")
        webbrowser.open("https://www.instagram.com/?hl=en")

    elif"YouTube" in ch:
        pyttsx3.speak("Opening Youtube ")
        #os.system("cls")
        webbrowser.open("https://www.youtube.com/results?search_query=IIEC")

    elif"buy" in ch:
        pyttsx3.speak("Opening Amazon ")
        #os.system("cls")
        webbrowser.open("https://www.amazon.in/s?k=Laptop&ref=nb_sb_noss_2")

    elif"clear" in ch:
        pyttsx3.speak("clearing  ")
        os.system("cls")
        #webbrowser.open("https://www.amazon.in/s?k=Laptop&ref=nb_sb_noss_2")
    
    elif "stop"in ch:
        import os,pyttsx3
        #os.system("cls") 
        pyttsx3.speak("Thank you")
        print("\n\n\n\n\t\t\t\u001b[41mIt was fun being with you! See you Soon.\u001b[40m")
        break ;
    else:
        print(ch)

     


     