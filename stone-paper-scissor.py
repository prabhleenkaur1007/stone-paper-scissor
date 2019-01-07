#let's play a game!!!
user1=str(input("user1: "))
user2=str(input("user2: "))


if user1 == "stone"and user2 == "stone"or user1=="scissor"and user2=="scissor"or user1=="paper"and user2=="paper":
    print ("result is draw")

elif user1=="paper"and user2=="stone"or user1=="stone"and user2=="scissor"or user1=="scissor"and user2=="paper":
    print ("user1 wins")

else:
    print ("user2 wins")
