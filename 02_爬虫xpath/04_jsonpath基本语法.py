import jsonpath
import json

obj = json.load(open('datastudy.json','r',encoding='utf-8'))
# author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author_list)

# 所有的作者
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)

# tag_list = jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)

# price_list = jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)


#第二本书
# book = jsonpath.jsonpath(obj,'$..book[2]')
# print(book)

#最后一本
# book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
# print(book)


#切片操作
# book_list = jsonpath.jsonpath(obj,'$..book[1:2]')
# print(book_list)

#过滤操作
# book_list = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# print(book_list)

#过滤操作
book_list = jsonpath.jsonpath(obj,'$..book[?(@.price<10)]')
print(book_list)