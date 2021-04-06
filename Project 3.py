"""
Created on Tue Mar 30 13:52:12 2021

@author: Daniel
"""


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
        self.mean = None
        self.stddev = None
        self.hv = None
        
    def update_alpha(self, a):
        self.alpha = a 
        
    def update_sims(self, n_sims):
        """simulate data and perform t test n_sims times"""
        
        for i in range(n_sims):
            data = stats.norm.rvs(loc=self.mean, scale=self.stddev, size=30)
            result = stats.ttest_1samp(data, self.hv)
            self.pvalues.append(result.pvalue)
            
            
    def update_mean(self, xbar):
        self.mean = xbar       
        
    def update_sd(self, sd):
        self.stddev = sd
        
    def update_hv(self, hv):
        self.hv = hv
       
    def print_pvalues(self):
        """list out all the p values"""
        print(self.pvalues)
        
    def error_proportion(self):
        
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
    

    n_sims = int(entry.get())
    a = float(entry2.get())
    xbar = float(entry3.get())
    hv = float(entry4.get())
    sd = float(entry5.get())
    
    
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
    




label = tk.Label(text = "How many simulations would you like to run?")
label2 = tk.Label(text = "What alpha value would you like to use?")
label3 = tk.Label(text = "What mean value would you like to use?")
label4 = tk.Label(text = "What HV do you want?")
label5 = tk.Label(text = "What SD do you want?")
entry = tk.Entry(width = 20)
entry2 = tk.Entry(width = 20)
entry3 = tk.Entry(width = 20)
entry4 = tk.Entry(width =20)
entry5 = tk.Entry(width = 20)

# entry2.insert(0, "0.05")

button = tk.Button(text = "Submit", command = click)
# button2 = tk.Button(text = "Submit", command = click)
out_label = tk.Label(text="")


label.pack()
entry.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()
entry4.pack()
label5.pack()
entry5.pack()

button.pack()
out_label.pack()

window.mainloop()


