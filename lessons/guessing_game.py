import random

num = random.randint(1,10)

try:
        userguess = int(input("guess number 1 to 10 >>  "))
        while userguess != num:
            print("wrong guess try again")
            userguess = int(input("guess number 1 to 10 >>  "))
except (TypeError, ValueError, KeyboardInterrupt):
      print("error wrong format / invalid input")
      exit()

print("found it XD")