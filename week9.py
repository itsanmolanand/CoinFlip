 #!/usr/bin/python
 
 #The object of the game is to ask the user to pick heads or tails and then let them see if they are correct or not.
 
import random

print "Coin Guessing Game."

f = open("Highscore.txt", "r+")

Highscore = f.read()

score = 0 

print "You high score is", Highscore

while True:

	guess = raw_input("Predict heads or tails> ")

	answer = random.choice(["heads", "tails"])

	print "It is", answer

	if guess == answer:
		score += 1
		print "Your score is: ", score
	
	else:
	
		print "Game Over"
		print "Your score is: ", score
		f.seek(0)
		if score > int(Highscore):
			f.truncate()
			score = str(score)
			f.write(score)
			Highscore = score
		break
print "Your high score is:", Highscore
	


 