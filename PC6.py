from pyhanlp import HanLP
from tkinter import *
def jufa(text1,text2):
    text = text1.get('1.0', END)
    sentence=HanLP.parseDependency(text)
    text2.delete('1.0', END)
    text2.insert('1.0', str(text2))