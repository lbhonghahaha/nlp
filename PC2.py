import jieba
from tkinter import *
from tkinter import messagebox

def jbfc(text1, text2):
    stext = text1.get('1.0', END)
    seg_list = jieba.cut(stext, cut_all=False)
    seg_res = "/".join(seg_list)
    text2.delete('1.0', END)
    text2.insert('1.0', seg_res)


def cdmx(text1):
    def guanbi():
        root3.destroy()

    def xiangliang():
        M = len(dic)
        vet = [0] * M
        enstr = en2.get()
        enlist = jieba.cut(enstr, cut_all=False)
        for line in enlist:
            try:
                index = dic.index(line)
                vet[index] = vet[index] + 1
            except ValueError:
                messagebox.showerror("错误", f"词典中不存在元素'{line}'")
        lbres.delete('1.0', END)
        lbres.insert('1.0', vet)

    stext = text1.get('1.0', END)
    seg_list = jieba.cut(stext, cut_all=False)
    global dic
    dic = []
    for line in seg_list:
        if line not in dic:
            dic.append(line)
    root3 = Tk()
    root3.title("词袋模型展示")
    lb1 = Label(root3, text='生成的词典如下：')
    lb1.pack()
    root3.geometry('380x850')
    text3 = Text(root3)
    text3.pack()
    text3.delete('1.0', END)
    text3.insert('1.0', dic)
    lb2 = Label(root3, text='请输入字符串：')
    lb2.pack()
    en2 = Entry(root3)
    en2.pack()
    lb3 = Label(root3, text='生成的特征向量如下：')
    lb3.pack()
    lbres = Text(root3)
    lbres.pack()
    bu7 = Button(root3, text='生成特征向量', command=xiangliang)
    bu7.pack()
    bu8 = Button(root3, text='关  闭', command=guanbi)
    bu8.pack()
