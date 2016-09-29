from random import randint
import textwrap

GREETING = """welcome to the guessing game, skin job. Your opponent is the computer, EX MACHINA.
if you lose this game, YOU WILL BE SHOT."""

def response(guess, gen):
	print("\nyour guess was: {}".format(guess))
	print("*"*10)
	print("Ex Machina's number was: {}".format(gen))
	print("="*10)
	print("="*10)

def guessing():
	guess = input("\nguess a number between 1 - 20:")
	return int(guess)

def roulette(gen, tries, guess):
	while tries > 1:
		if guess == gen:
			response(guess,gen)
			print("\nyou win, skin job.")
			break
		else:
			response(guess,gen)
			tries -= 1
			gen = randint(1,21)
			print("\nyou only have {} guesses left.".format(tries))
			print("guess again...")
			guess = guessing()
	else:
		response(guess,gen)
		print("\nYou lose. Bang.")

def numTries():
	print("how many tries would you like, skin job?")
	tries = input("Choose up to 5 tries:")
	return int(tries)

def main():
	gen = randint(1,21)

	greeting = textwrap.wrap(GREETING,width=30)
	for text in greeting: #prints each line of greeting
		print(text)

	roulette(gen, numTries(), guessing())
	print("\n")

if __name__ == "__main__":
	main()