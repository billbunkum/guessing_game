from random import randint
import textwrap

def check_errors():
	pass

class Display(object):

	def __init__(self):
		self.greeting = ""
		self.GREETING = """welcome to the guessing game, skin job. Your opponent is the computer, EX MACHINA.
	if you lose this game, YOU WILL BE SHOT."""
	
	def print_greeting(self):
		self.greeting = textwrap.wrap(self.GREETING,width=30)
		for text in self.greeting: #prints each line of greeting
			print(text)

class Calculations(object):
	pass

def response(guess, gen):
	print("\nyour guess was: {}".format(guess))
	print("*"*10)

	#for testing
#	print("Ex Machina's number was: {}".format(gen))
	print("="*10)
	print("="*10)

def guessing():
	guess = input("\nguess a number between 1 - 20:")
	return int(guess)

def compass(guess, gen):
	if guess > gen:
		print("your meat-brain operates inappropriately higher than.")
	else:
		print("your brain operates deficiently lower than.")

def roulette(gen, tries, guess):
	while tries > 1:
		if guess == gen:
			response(guess,gen)
			print("\nyou win, skin job.")
			break
		else:
			response(guess,gen)
			tries -= 1
			compass(guess,gen)
			print("\nyou only have {} guesses left.".format(tries))
			print("guess again...")
			guess = guessing()
	else:
		response(guess,gen)
		print("\nYou lose. Bang.")

def num_tries():
	print("how many tries would you like, skin job?")
	tries = input("Choose up to 5 tries:")
	return int(tries)

def main():
	gen = randint(1,21)

	display = Display()
	display.print_greeting()

	roulette(gen, num_tries(), guessing())
	print("\n")
