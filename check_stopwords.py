#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 13:37
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : check_stopwords.py
# @Software: PyCharm

import string

stopwords_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
                  'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
                  'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom',
                  'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                  'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
                  'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
                  'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to',
                  'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
                  'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
                  'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                  'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll',
                  'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven',
                  'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']


def check_stopwords(query):
    """
    停止词检查
    :param query: 查询字段
    :return: 检查过后的字符串
    """
    query_no_punct_str = ''.join([char if char not in string.punctuation else ' ' for char in query.strip()])

    return ' '.join([query_word for query_word in query_no_punct_str.split() if query_word not in stopwords_list])


def main():
    """
    函数入口
    :return:
    """
    while True:
        query_str = input('请输入查询字段：')
        print('请求的查询字段：', query_str)
        print('检查后的查询字段：', check_stopwords(query_str))
        print('--------------------------')


if __name__ == '__main__':
    main()
