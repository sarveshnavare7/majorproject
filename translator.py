import speech_recognition as sr
# explicit function to take input commands and recognize them
def takeCommandMarathi():

	r = sr.Recognizer()
	with sr.Microphone() as source:
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		print('Listening')
		r.pause_threshold = 0.7
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='mr-In')
			
			# for listening the command in indian english
			print("the query is printed='", Query, "'")
		
		# handling the exception, so that assistant can
		# ask for telling again the command
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		return Query

from googletrans import Translator
translator = Translator()
results = translator.translate(takeCommandMarathi())
print(results.text)

# https://www.google.com/search?q=how+do+you+run+a+python+script+in+django&oq=how+do+you+run+a+python+script+in+django&aqs=chrome..69i57j0i22i30l4j0i390l2.19035j0j7&sourceid=chrome&ie=UTF-8
# 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