import jieba.posseg as psg
from tkinter import *
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer
#加载分词模型
def mmst(text1,text2):
    recognizer = NamedEntityRecognizer('ltp_data_v3.4.0/ner.model')
    postagger = Postagger("ltp_data_v3.4.0/pos.model")
    segmentor = Segmentor("ltp_data_v3.4.0/cws.model")
    textstr=text1.get("1.0", END)
    words = segmentor.segment(textstr) #分词
    postags = postagger.postag(words)  #词性标注
    netags = recognizer.recognize(words, postags) #命名实体识别
    persons, places, orgs = set(), set(), set()#转换为集合
    i = 0
    for tag, word in zip(netags, words):#合成元组
        j = i
        if "Nh" in tag:
            if str(tag).startswith('S'):
                persons.add(word)
            elif str(tag).startswith('B'):
                union_person = word
                while netags[j] != 'E-Nh':
                    j += 1
                    if j < len(words):
                        union_person += words[j]
                persons.add(union_person)

        if "Ns" in tag:
            if str(tag).startswith('S'):
                places.add(word)
            elif str(tag).startswith('B'):
                union_place = word
                while netags[j] != 'E-Ns':
                    j += 1
                    if j < len(words):
                        union_place += words[j]
                places.add(union_place)

        if "Ni" in tag:
            if str(tag).startswith('S'):
                orgs.add(word)
            elif str(tag).startswith('B'):
                union_org = word
                while netags[j] != 'E-Ni':
                    j += 1
                    if j < len(words):
                        union_org += words[j]
                orgs.add(union_org)
        i += 1
    text2.delete('1.0', END)
    text2.insert(END,'\n人名:')
    text2.insert(END, list(persons))
    text2.insert(END,'\n地名:')
    text2.insert(END, list(places))
    text2.insert(END,'\n专有名词:')
    text2.insert(END, list(orgs))

def cxbz(text1,text2):
    textstr = text1.get("1.0", END)
    seg_list=psg.cut(textstr)
    resstr=''.join(['{0}/{1}'.format(w,t) for w,t in seg_list])
    text2.delete('1.0', END)
    text2.insert('1.0', resstr)
