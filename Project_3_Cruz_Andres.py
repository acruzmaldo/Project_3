# -*- coding: utf-8 -*-


""""
Reset Button
""""


import tkinter as tk

from scipy import stats

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

def click():
    
    n_sims = int(entry.get())
    a = float(entry2.get())
    xbar = float(entry3.get())
    
    mysims.update_alpha(a)
    mysims.update_mean(xbar)
    mysims.update(n_sims)
    mysims.error_proportion()
    
    tk.Label(window, text=f"{mysims.error_rate} is the type 1 error rate.").pack()

def clear():
    """clears all the labels"""
    
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)


label = tk.Label(text = "How many simulations would you like to run?")
label2 = tk.Label(text = "What alpha value would you like to use?")
label3 = tk.Label(text = "What mean value would you like to use?")
entry = tk.Entry(width = 20)
entry2 = tk.Entry(width = 20)
entry3 = tk.Entry(width = 20)


button = tk.Button(text = "Submit", command = click)
button_r = tk.Button(text = "Reset", command = clear)
out_label = tk.Label(text="")


label.pack()
entry.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
button.pack()
button_r.pack()
out_label.pack()

window.mainloop()
