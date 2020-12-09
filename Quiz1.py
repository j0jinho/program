#Score
score = 0
score = int(score)

#Introduce the game
print("Hi welcome to League of Legends Trivia!")
print("Reply with the correct number.")

#Question 1
print("""Who is the first champion designed for League of Legends?""")

answer1 = "Singed".lower()
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! Singed is correct!")
    score = score + 1

#Question 2
print("""Who won Worlds 2020?
1. T1
2. Sn Gaming
3. G2 Esports 
4. Damonwon Gaming""")

answer1 = "4"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! Damwon Gaming is correct!")
    score = score + 1


#Question 3
print("""Who was the 2020 Most Valuable Player?
1. TSM Bjergsen
2. TL Corejj
3. 100 Ssumday
4. C9 Blabber""")

answer1 = "2"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! TL Corejj is correct!")
    score = score + 1


#Question 4
print("""Which pro retired this year?
1. Hai
2. Flame
3. Bjergsen 
4. Faker""")

answer1 = "3"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! Bjergsen is correct!")
    score = score + 1


#Question 5
print("""What is Gromps full name
1. Sir Grompleton
2. Grompule
3. Gromp 
4. Lord Grompulus Kevin Ribbiton of Croaksworth""")

answer1 = "4"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! Lord Grompulus Kevin Ribbiton of Croaksworth correct!")
    score = score + 1

#Display score and finish quiz
print(f"Your score is {score}!")
print("thanks for playing!")