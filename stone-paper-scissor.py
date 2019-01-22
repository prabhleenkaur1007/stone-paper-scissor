#let's play a game!!!
user1=str(input("user1: "))
user2=str(input("user2: "))


if user1 == "stone"and user2 == "stone"or user1=="scissor"and user2=="scissor"or user1=="paper"and user2=="paper":
    print ("result is draw")

elif user1=="paper"and user2=="stone"or user1=="stone"and user2=="scissor"or user1=="scissor"and user2=="paper":
    print ("user1 wins")

else:
    print ("user2 wins")#let's play a game!!!
score1= 0
score2=0
for x in range (5):
  user1=str(input("user1: "))
  user2=str(input("user2: "))


  if user1 == "stone"and user2 == "stone"or user1=="scissor"and user2=="scissor"or user1=="paper"and user2=="paper":
      print ("result is draw")

  elif user1=="paper"and user2=="stone"or user1=="stone"and user2=="scissor"or user1=="scissor"and user2=="paper":
      print ("user1 wins")
      score1+=1

  else:
      print ("user2 wins")
      score2+=1
print(score1,score2)


