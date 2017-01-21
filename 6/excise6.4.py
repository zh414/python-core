#coding:utf-8
#cacular average of a list and give a level
import string

data = string.digits
alpha = string.letters
s=0.0
while True:
    new_score = []
    score = raw_input("Please input one of your scores:")
    if score in data:
        new_score.append(float(score))
    else:
            break
print new_score




 