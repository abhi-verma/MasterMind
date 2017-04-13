#! /usr/bin/python

print 'Content-type: text/html'

print ''

import random
import cgi
form = cgi.FieldStorage()

reds = 0
whites = 0

if "answer" in form:
	answer = form.getvalue("answer")
else:
	answer = ""
	for i in range(4):
		answer += str(random.randint(0,9))

if "guess" in form:
	guess = form.getvalue("guess")
	for key, digit in enumerate(guess):
		if digit == answer[key]:
			reds += 1
		else:
			for answerDigit in answer:
				if answerDigit == digit:
					whites += 1
					break		
else:
	guess = ""

if "noOfGuesses" in form:
	noOfGuesses = int(form.getvalue("noOfGuesses")) + 1
else:
	noOfGuesses = 0
	
if noOfGuesses == 0:
	message = 'I have chosen a 4 digit number. Can you guess it?'
elif reds == 4:
	message = 'Well Done! You got it in ' + str(noOfGuesses) + ' guess(es). <a href="">Play again</a>'
else:
	message = "You have " + str(reds) + " correct digits in the right place, and " + str(whites) + " correct digits in the wrong place. You have had " + str(noOfGuesses) + " guesses."

print '<h1>MasterMind</h1>'
print "<p>" + message + "</p>"
print '<form method="post">'
print '<input type="text" name="guess" value="' + guess + '">'
print '<input type="hidden" name="answer" value="' + answer + '">'
print '<input type="hidden" name="noOfGuesses" value="' + str(noOfGuesses) + '">'
print '<input type="submit" value="Guess!">'
print '</form>'
