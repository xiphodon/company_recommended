#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 18:38
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : neo4j_test.py
# @Software: PyCharm

from py2neo import Graph, Node, Relationship

graph = Graph(r'http://localhost:7474', username='test_db', password='123456')

# for i in range(10):
#     company = Node('company', id=i, name='公司' + str(i))
#     print(company)
#     graph.create(company)

# node_1 = graph.find_one('company', property_key='id', property_value=1)
# node_2 = graph.find_one('company', property_key='id', property_value=2)
# node_3 = graph.find_one('company', property_key='id', property_value=3)
# node_4 = graph.find_one('company', property_key='id', property_value=4)

# r_1_2 = Relationship(node_1, 'export', node_2)
# r_3_2 = Relationship(node_3, 'export', node_2)
# r_4_2 = Relationship(node_4, 'export', node_2)

# r_1_2['hscode'] = '6001'
# r_3_2['hscode'] = '7001'
# r_4_2['hscode'] = '8001'

# graph.create(r_1_2)
# graph.create(r_3_2)
# graph.create(r_4_2)

sql_1 = "match (c1:company{id:1})-[r1:export{hscode:'6001'}]->(c2:company)<-[r2:export]-(c:company) return c, r1, r2"
sql_2 = "match (c1:company{id:1})-[r1:export]->(c2:company)<-[r2:export]-(c:company) where r2.hscode in r1.hscode return c"

result = graph.run(sql_2)

for item in result:
    print(item)

