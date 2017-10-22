#!/bin/python
from datetime import date
import io


def age(day_of_birth):
    return 40

def loop(loop_times):
   for i in range(loop_times):
       print(i)

def read_file(filename):
    file = io.open(filename, "r")
    print(file.readable())
    for line in file:
        print(line)
    file.close()

read_file("/Users/tommy/Documents/gitignore_global.txt")


# loop(100)
#
# first_name = raw_input("What's your firstname ? ")
# last_name = raw_input("What's your lastname ? ")
# day_of_birth = raw_input("When were you born ? ")
# age = age(day_of_birth)
# today = date.today()
# print("Hello, {} {}.".format(first_name, last_name))
# print("Today, {}, you are {} years old.".format(today, age))
