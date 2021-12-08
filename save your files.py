#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:27:57 2021

@author: clockshield
"""

from tkinter import *

root=Tk()
root.title("Fibonacci")
root.geometry("400x400")


label_series = Label(root,text = "Fibonnici Series: ")
label_flower = Label(root)
label_spirals = Label(root)

def Fibonacci():
    num_1 = 0
    num_2 = 1
    counter = 1
    sum = 0
    while (counter <= 10):
        label_series["text"] += str(sum) + " "
        num_1 = num_2
        num_2 = sum
        sum = num_1 + num_2
        counter = counter + 1
    label_flower["text"] = "The Flower Has Bloomed lolololol"
    label_spirals["text"] = "Spirals in the right direction are " + str(num_1) + ". Spirals in the left direction are " + str(num_2) + "."
    
btn = Button(root, text = "Show the FBI", command=Fibonacci)

btn.pack()
label_series.pack()
label_flower.pack()
label_spirals.pack()
root.mainloop()
