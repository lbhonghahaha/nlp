from tkinter import *
import numpy as np
import jieba
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
def ciyun(text1):
    text = text1.get('1.0', END)
    text_cut = jieba.lcut(text)
    new_textlist = ''.join(text_cut)
    pic = np.array(Image.open('模板2.jpg'))
    wc = WordCloud(background_color='white', mask=pic, max_font_size=40, random_state=30, font_path='msyh.ttf',
                   max_words=200, min_font_size=2)
    wc.generate(new_textlist)
    plt.figure()
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()