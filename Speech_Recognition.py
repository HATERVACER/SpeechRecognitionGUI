import speech_recognition as sr
# import webbrowser as wb
# import gttks
import pyttsx3
import os
import sys

engine = pyttsx3.init("espeak")

def talk(words):
	print(words)
	engine.say(words)
	engine.runAndWait()
def wb(url):
	request = "google-chrome " + url
	os.system(request)
	del request

talk("Привет, спроси у меня что-либо")

def command():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		talk("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)

	try:
		cmd = r.recognize_google(audio, language="ru-RU").lower()
		print("User said: " + cmd)
	except sr.UnknownValueError:
		talk("Я вас не поняла")
		cmd = command()

	return cmd

def make_something(cmd):
	if 'открой браузер' in cmd:
		os.system("google-chrome")
	elif 'привет' in cmd:
		talk("Привет привет")
	elif 'стоп' in cmd:
		talk("Досвидания")
		sys.exit()
	elif 'открой файловый менеджер' in cmd:
		os.system("dolphin")
	elif 'как тебя зовут' in cmd:
		talk("Эмма Вотсон")


while True:
	make_something(command())
