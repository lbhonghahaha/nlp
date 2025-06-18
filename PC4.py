import math
import numpy as np
import jieba
import jieba.posseg as psg
from tkinter import *

# 文档分词
def preprocess(sentence, pos=False):
    if not pos:
        seg_list = jieba.cut(sentence)
    else:
        seg_list = psg.cut(sentence)

    stop_word_path = 'stopwords.txt'
    stopword_list = [sw.replace('\n', '') for sw in open(stop_word_path, encoding='utf-8').readlines()]

    filiter_list = []
    for seg in seg_list:
        if not pos:
            word = seg
            flag = 'n'
        else:
            word = seg.word
            flag = seg.flag
        if not flag.startswith('n'):
            continue
        if not word in stopword_list and len(word) > 1:
            filiter_list.append(word)
    return filiter_list

def load_data(pos = False, corpus_path = 'corpus.txt'):
    doc_list = []
    for line in open(corpus_path, 'r', encoding='utf-8'):
        content = line.strip()
        filter_list = preprocess(content, pos)
        doc_list.append(filter_list)
    return doc_list


def get_idf(doc_list):
    idf_dict = {}
    sent_count = len(doc_list)

    for doc in doc_list:
        for word in set(doc):
            idf_dict[word] = idf_dict.get(word, 0.0) + 1.0

    for k, v in idf_dict.items():
        idf_dict[k] = math.log(sent_count / (1.0 + v))
        defalut_idf = math.log(sent_count / 1.0)
        return idf_dict, defalut_idf


def get_tf_dic(word_list):
    tf_dic = {}
    for word in word_list:
        tf_dic[word] = tf_dic.get(word, 0.0) + 1.0

    sent_count = len(word_list)
    for k, v in tf_dic.items():
        tf_dic[k] = float(v) / sent_count
    return tf_dic


def get_tfidf(idf_dic, default_idf, word_list, keyword_num):
    tfidf_dic = {}
    for word in word_list:
        idf = idf_dic.get(word, default_idf)
        tf_dic = get_tf_dic(word_list)
        tf = tf_dic.get(word, 0)

        tfidf = tf * idf
        tfidf_dic[word] = tfidf
    print(tfidf_dic.items())

    for k, v in sorted(tfidf_dic.items(), key=lambda x: x[1], reverse=True)[:keyword_num]:
        print(k + "/", end='')
    print()


def tfidf_extract(word_list, pos=False, keyword_num = 10):
    doc_list = load_data(pos)
    idf_dic, default_idf = get_idf(doc_list)
    tfidf_model = get_tfidf(idf_dic, default_idf, word_list, keyword_num)

def keyword(text1):
    text = text1.get('1.0', END)
    filter_list = preprocess(text, pos=True)
    tfidf_extract(filter_list)

def tyc(text1,text2):
    text = text1.get('1.0', END)
    filter_list = preprocess(text, pos=True)
    text2.delete('1.0', END)
    text2.insert('1.0', filter_list)

def datebase(text2,pos=False):
    doc_list = load_data(pos)
    text2.delete('1.0', END)
    text2.insert('1.0', doc_list)