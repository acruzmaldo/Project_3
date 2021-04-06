#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:06:24 2021

@author: cassienataro
"""

#program with a GUI
#first task, plan what the GUI will look like
#user needs to change the mean, change the std dev, change alpha, change their hypothesis
#number of simulations 
#sample size will be constant and it will be normal



import tkinter as tk

from scipy import stats

import tkinter.font as font


class HTSims:
    """simulations for testing one sample"""
    def __init__(self):
        """initialize the class"""
        self.pvalues = []
        self.alpha = 0.05
        self.smaller = []
        self.larger = []
        self.error_rate = None
        self.mean = 10 
        
    def update_alpha(self, a):
        self.alpha = a 
        
    def update_mean(self, xbar):
        self.mean = xbar
        
    def update(self, n_sims):
        """simulate data and perform t test n_sims times"""
        
        for i in range(n_sims):
            data = stats.norm.rvs(loc=self.mean, scale=5, size=30)
            result = stats.ttest_1samp(data, self.mean)
            self.pvalues.append(result.pvalue)
            
    def print_pvalues(self):
        """list out all the p values"""
        print(self.pvalues)
        
    def error_proportion(self):
        
        for i in self.pvalues:
            if i > self.alpha:
                self.larger.append(i)
            else:
                self.smaller.append(i)
                
        self.error_rate = len(self.smaller)/len(self.pvalues)
        print(self.error_rate)
    
mysims = HTSims()
window = tk.Tk()
window.title("Hypothesis Testing Simulations")


def click():
    
    n_sims = int(entry.get())
    a = float(entry2.get())
    xbar = float(entry3.get())
    
    mysims.update_alpha(a)
    mysims.update_mean(xbar)
    mysims.update(n_sims)
    mysims.error_proportion()
    
    tk.Label(window, text=f"{mysims.error_rate} is the type 1 error rate.").pack()
    

gold = '#FFB81C'
green ='#154734'
myFont = font.Font(family = 'Georgia', size = 16, weight = 'bold')


label = tk.Label(text = "What mean value would you like to use?", 
                 fg = gold,
                 bg = green)
label.grid(row = 1, column = 1)
label['font'] = myFont

label2 = tk.Label(text = "What std. dev. value would you like to use?", 
                  fg = gold,
                  bg = green)
label2.grid(row = 2, column = 1)
label2['font'] = myFont

label3 = tk.Label(text = "What alpha value would you like to use?", 
                  fg = gold,
                  bg = green)
label3.grid(row = 3, column =1)
label3['font'] = myFont

label4 = label3 = tk.Label(text = "What is your hypothesis value?", 
                  fg = gold,
                  bg = green)
label4.grid(row = 4, column =1)
label4['font'] = myFont

label5 = tk.Label(text = "How many simulations would you like to run?", 
                  fg = gold,
                  bg = green)
label5.grid(row = 5, column =1)
label5['font'] = myFont


entry = tk.Entry(width = 20)
entry.grid(row = 1, column = 2)
entry2 = tk.Entry(width = 20)
entry2.grid(row = 2, column = 2)
entry3 = tk.Entry(width = 20)
entry3.grid(row = 3, column =2)
entry4 = tk.Entry(width = 20)
entry4.grid(row = 4, column = 2)
entry5 = tk.Entry(width = 20)
entry5.grid(row = 5, column = 2)


# entry2.insert(0, "0.05")

button = tk.Button(text = "Submit", command = click)
# button2 = tk.Button(text = "Submit", command = click)
out_label = tk.Label(text="")





window.mainloop()









