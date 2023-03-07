print("Welcome to the game")

playing = input("Do you want to play ?")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")
score = 0

answer = input("What is a goat? ")
if answer.lower() == "a goat is an animal":
    print("Correct!")
    score += 1
else:
    print("Thats wrong")

answer = input("What is CPU? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Thats wrong")

answer = input("What is python? ")
if answer.lower() == "python is a programming language":
    print("Correct!")
    score += 1
else:
    print("Thats wrong")
    
answer = input("What is linux? ")
if answer.lower() == "linux is  an operating system":
    print("Correct!")
    score += 1
else:
    print("Thats wrong")

print("You have got " + str(score) + " questions correct")
print("You have got " + str((score / 4) * 100) + "%.")