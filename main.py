from tkinter import *
import PC1
import PC2
#import PC3
import PC4
import PC5
import PC7
root=Tk()
root.title('正则表达式')
root.geometry('720x350')
menubar= Menu(root)
menu1= Menu(menubar, tearoff=False)
menubar.add_cascade(label="文件(F)", menu=menu1)
menu2= Menu(menubar, tearoff=False)
menubar.add_cascade(label="功能(E)", menu=menu2)
menu3= Menu(menubar, tearoff=False)
menubar.add_cascade(label="关键词(K)", menu=menu3)
menu4= Menu(menubar, tearoff=False)
menubar.add_cascade(label="句法分析(S)", menu=menu4)
menu1.add_command(label="打开文件(O)",command=lambda:PC1.doopen(text1))
menu1.add_command(label="关闭(E)",command=lambda:root.destroy())
menu2.add_command(label="查找字符串",command=lambda:PC1.findstr(text1,text2))
#menu2.add_command(label="正则匹配",command=lambda:PC1.zdpp(entry2,text1,text2))
menu2.add_command(label='结巴分词',command=lambda:PC2.jbfc(text1,text2))
menu2.add_command(label='词袋模型',command=lambda:PC2.cdmx(text1))
#menu2.add_command(label='词性标注',command=lambda:PC3.cxbz(text1,text2))
#menu2.add_command(label='命名实体识别',command=lambda:PC3.mmst(text1,text2))
menu3.add_command(label='去除停用词',command=lambda:PC4.tyc(text1,text2))
menu3.add_command(label='查看数据集',command=lambda:PC4.datebase(text1))
menu3.add_command(label='关键词提取',command=lambda:PC4.keyword(text1))
menu3.add_command(label='生成词云',command=lambda:PC5.ciyun(text1))
menu4.add_command(label='句法分析')
menu4.add_command(label='天气查询',command=lambda:PC7.tianqichaxun(text1,text2,''))
root.config(menu = menubar)
labelframe1=LabelFrame(root,width=80,height=40,text='文本区')
labelframe1.grid(row=1,column=1)
text1=Text(labelframe1,width=50,height=24)
text1.grid(row=1,column=1)
text2=Text(labelframe1,width=50,height=24,fg='blue')
text2.grid(row=1,column=2)
'''
labelframe2=LabelFrame(root,width=80,height=40,text='功能区')
labelframe2.grid(row=1,column=2)
label1=Label(labelframe2,text='请输入正则表达式')
label1.pack()
entry2=Entry(labelframe2)
entry2.pack()
'''
root.mainloop()

