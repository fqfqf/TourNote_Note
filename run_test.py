# -*- coding: utf-8 -*-
from native_bayes_sentiment_analyzer import SentimentAnalyzer


model_path = './data/bayes.pkl'
userdict_path = './data/userdict.txt'
stopword_path = './data/stopwords.txt'
corpus_path = './data/review.csv'


analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)
#text = '行程总体来说不错。门票有点略贵，但还可以接受。景区演出含有意思，孩子玩得很开心。不过景点工作人员态度太差了，一点都不礼貌。'
#text = '行程总体来说不错。景区演出含有意思，孩子玩得很开心。不过景点工作人员态度太差了，一点都不礼貌。'
text='对景点印象非常不好！东西很难吃，工作人员服务态度也差。总体来说非常差劲，不会再去了'
#analyzer.analyze(text=text)

def get_score(file):
    
    pos = analyzer.analyze(text=file)
    return pos