import pyttsx3
import os
import pyttsx3 as pt
converter = pt.init()
voices=converter.getProperty('voices')
converter.setProperty('voice',voices[1].id)
converter.runAndWait()
#pt.speak("hi, nitin how are you")
os.system('cls')
print(f'\n\n\n\n\t\t\t\u001b[41mWelcome to my Menu.\u001b[40m')
print('\t\t\t------------------')
name=input('\n\n\n\t\t\tWhat Can I call You:')
os.system('cls')
pt.speak(f"hello{name}")
#print("This is menu:",end=' ')
#print("To open a new notepad file")
#print("To open web browser")
#print("To open a media player:")
i=1
while i<3 :
	x=input(f'\n\n\n\n\n\t\t\t\u001b[44mHello {name},What Can I do for you :\u001b[40m')
	if (("Open" in x) and("Notepad" in x)):
		import pyttsx3 ,os
		pyttsx3.speak("Opening Notepad")
		#import os
		os.system("Notepad")
		#print("Here's what I found")
		os.system("cls")
	elif  (("Open" in x)and ("Web Browser"in x)):
		import pyttsx3 ,os
		pyttsx3.speak("Opening Google")
		os.system("chrome")
		os.system("cls")
	elif  (("Open"in x)and ("Media Player"in x) or ('Play' in x) and ('Music' in x) ):
		import pyttsx3 ,os
		pyttsx3.speak("Opening Media player")
		os.system("wmplayer")
		os.system("cls")
	elif "end"in x:
		import os,pyttsx3
		os.system("cls") 
		pyttsx3.speak("Thank you")
		print("\n\n\n\n\t\t\t\u001b[41mIt was fun being with you! See you Soon.\u001b[40m")
		break;
	elif (("Open"in x)and ("Calculator"in x)):
		import os,pyttsx3
		pyttsx3.speak("Opening Calculator")
		os.system("calc")
		os.system("cls")
	elif ( ("Open" in x) and ("Webcam" in x) or ('Take' in x) and ('Selfie'in x)):
		import cv2 ,time ,os,pyttsx3
		pyttsx3.speak("Opening Webcam")

		video = cv2.VideoCapture(0)

		check,frame=video.read()

		cv2.imshow("Capturing",frame)
		cv2.waitKey(0)
		video.release()
		os.system("cls")	
	else:
		import pyttsx3,os
		os.system("cls") 
		pyttsx3.speak("Oops")
		print("\u001b[31m\n\n\n\t\t\tOops! I can't recognize that. Try one more time\u001b[37m")
