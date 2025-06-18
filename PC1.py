from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import re


def doopen(text1):
    filename = askopenfilename()  # 获取文件名字，利用windows窗口
    if filename == '':
        return 0
    filestr = open(filename, 'rb').read()
    text1.delete('1.0', END)
    text1.insert('1.0', filestr.decode('utf-8'))
    text1.focus()


def findstr(text1,text2):
    def confirm():
        regex = entry1.get()
        resstr = []
        for line in lines:
            if re.search(regex, line) is not None:
                resstr += line
                resstr += '\n'
        text2.delete('1.0', END)
        text2.insert('1.0', resstr)
        text2.focus()
        root2.destroy()

    filestr = text1.get("1.0", END)
    lines = filestr.split('。')
    root2 = Tk()
    root2.title('请输入要查找的内容')
    entry1 = Entry(root2)
    entry1.pack()
    bu3 = Button(root2, text='确定', command=confirm)
    bu3.pack()


def zdpp(entry2,text1,text2):
    patstr = entry2.get()
    pattern = re.compile(patstr, flags=0)
    test_string = text1.get("1.0", END)
    # 检查字符串是否匹配正则表达式
    if pattern.match(test_string):
        text2.delete('1.0', END)
        text2.insert('1.0', "匹配成功")
    else:
        text2.delete('1.0', END)
        text2.insert('1.0', "匹配失败")
