# -*- coding: utf-8 -*-
"""
#################################################################
 -*- coding: utf-8 -*-       JMJ                               
Cassie Nataro                 +
Daniel Lim                             
Andres Cruz Maldonado

Project 3 
###################################################################
"""

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
        self.mean = None
        self.stddev = None
        self.hv = None
        
    def update_alpha(self, a):
        """update value of alpha to be the input"""
        self.alpha = a 
        
    def update_sims(self, n_sims):
        """simulate data and perform t test n_sims times"""
        
        for i in range(n_sims):
            data = stats.norm.rvs(loc=self.mean, scale=self.stddev, size=30)
            result = stats.ttest_1samp(data, self.hv)
            self.pvalues.append(result.pvalue)
            
            
    def update_mean(self, xbar):
        """update value of mean to be the input"""
        self.mean = xbar       
        
    def update_sd(self, sd):
        """update value of standard deviation to be the input"""
        self.stddev = sd
        
    def update_hv(self, hv):
        """update value of hypothesis value to be the input"""
        self.hv = hv
       
    def print_pvalues(self):
        """list out all the p values"""
        print(self.pvalues)
        
    def error_proportion(self):
        """tests type II error"""

        self.smaller = []
    
        for i in self.pvalues:
            if i > self.alpha:
                self.larger.append(i)
            else:
                self.smaller.append(i)
                
        self.error_rate = len(self.smaller)/len(self.pvalues)
        print(self.error_rate)
    
mysims = HTSims()
window = tk.Tk()


def click():
    """takes inputs and from the entries and updates the necessary class methods"""
    
    #Error check: checks whether it is a numeric input
    try:
        n_sims = int(entry5.get())
        a = float(entry3.get())
        xbar = float(entry4.get())
        hv = float(entry.get())
        sd = float(entry2.get())


        mysims.update_alpha(a)
        mysims.update_mean(xbar)
        mysims.update_hv(hv)
        mysims.update_sd(sd)
        mysims.update_sims(n_sims)
        mysims.error_proportion()



        if xbar == hv:
            out_label["text"] = f"{mysims.error_rate} is the type 1 error rate"
        else:
            out_label["text"] = f"{1 - mysims.error_rate} is the type 2 error rate"
            
    except ValueError:    
        out_label["text"] = "Your input is not a valid number"
        
    

def clear():
    """clears all the labels"""
    
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)

#sets up fonts
gold = '#FFB81C'
green ='#154734'
myFont = font.Font(family = 'Georgia', size = 16, weight = 'bold')

#templates for all the labels
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

#organizes window
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

#organizes and sets up buttons and out label
button = tk.Button(text = "Submit", command = click)
button.grid(row = 6, column = 1)
button_r = tk.Button(text = "Reset", command = clear)
button_r.grid(row = 6, column =2)
out_label = tk.Label(text="")
out_label.grid(row = 7, column = 2)
out_label['font'] = myFont


window.mainloop()