from tkinter import filedialog
import os.path

filname = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
print(filname)
filname = os.path.basename(filname)
print(filname)
