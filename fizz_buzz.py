# -*- coding: utf-8 -*-
"""fizz_buzz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Rlu_JFgxxqeSeGkNTv0H9p1cZh754kl
"""

# Loop for 100 times i.e. range
for num in range(1,101):
    # Number divisible by 15,(divisible
    # by both 3 & 5), print 'FizzBuzz'
    # in place of the number  
    if num % 15 == 0:
        print("FizzBuzz")
    # Number divisible by 3, print 'Fizz'
    # in place of the number
    elif num % 3 == 0:
        print("Fizz")
    # Number divisible by 5,
    # print 'Buzz' in
    # place of the number    
    elif num % 5 == 0:
        print("Buzz")
    # Print numbers    
    else :    
        print(num)

for num in range(1,101):  
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")  
    elif num % 5 == 0:
        print("Buzz")   
    else :    
        print(num)