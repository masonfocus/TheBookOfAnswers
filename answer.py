#!/usr/bin/python3

import random as r

with open("./answers.txt","r") as file:
    content = file.readlines()
    lenth = len(content)
    n = r.randint(0,lenth)
    print(content[n])