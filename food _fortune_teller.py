import random
print ("Welcome to the food fortune teller!\nWe will ask you for a person's name and tell you what he or she will eat.") 
name = input ("What is the person's name?\n")
adj = ["disgustingly", "happily", "voraciously", "sloppily", "delicately"]
apps = ["snails", "salad", "bacon", "chopped liver", "brussel sprouts"]
main = ["steak", "cereal", "grilled snake", "frog legs", "gruel"]
when = ["breakfast", "lunch", "dinner", "snack", "dessert"]
print (name.title(),"will", random.choice(adj),"eat", random.choice(apps), "and" ,random.choice(main),"for",random.choice(when),".")

