# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:48:54 2019

@author: Darshit.Purohit
"""

import tkinter as tk
#import time

def distancing(key, counterperson):
    root = tk.Tk()
    root.title("Maintain distance!")
    alert_msg = "Person "+str(key)+" and person "+str(counterperson)+" are standing close to eachother."
    label = tk.Label(root, text=alert_msg)
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    button = tk.Button(root, text="OK", command=lambda: root.destroy())
    button.pack(side="bottom", fill="none", expand=True)
    root.after(3000, lambda: root.destroy())
    root.mainloop()

#alert(3)
