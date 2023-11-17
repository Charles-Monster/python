# d={1:'a',2:'b'}
# values=d.values()
# for value in values:
#     print(value)
#item 可以列舉出字典裡所有的鍵值對，
#返回被移出的資料值
# d={1:'a',2:'b'}
# items=d.items()
# for item in items:
#     print(item)
#     print(item[0],item[1])
# d={1:'a',2:'b'}
# items=d.items()
# for key,value in items:
#     print(key,value)
# food_list={'蛋糕':1,'三明治':10,'果汁':20,'薯條':15,'披薩':2}

# for food2,count in food_list.items() :
#     if food2=='果汁':
#         print(food2+':'+str(count)+'杯')
#     else:
#         print(food2+':'+str(count)+'份')
#新增/修改元素
#設定對應位置的元素數值
#若鍵不存在則會自動新增
#ex:
# book={}
# book['書名']='海邊的朱柏翰'
# book['作者']='朱柏翰'
# print(book)
# food_list={'蛋糕':1,'三明治':10,'果汁':20,'薯條':15,'披薩':2}
# food_list['冰淇淋']=10
# food_list['熱狗']=20
# food_list['果汁']=25
# for food2,count in food_list.items() :
#     if food2=='果汁':
#         print(food2+':'+str(count)+'杯')
#     else:
#          print(food2+':'+str(count)+'份')

