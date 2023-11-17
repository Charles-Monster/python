#鍵檢查可以判斷字典有沒有該鍵，如果有則回傳true，如果沒有則回傳false
# d={1:'a',2:'b'}
# 1 in d
# "A"in d
# "a"in d
# print("a"in d)
# food_list={'蛋糕':1,'三明治':10,'果汁':20,'薯條':15,'披薩':2}
# food_list['冰淇淋']=10
# food_list['熱狗']=20
# food_list['果汁']=25
# parents_food_list={'蛋糕':1,'三明治':10,'果汁':20,'薯條':15,'披薩':2}
# for food2,count in food_list.items() :
#     if food2=='果汁':
#         print(food2+':'+str(count)+'杯')
#     else:
#          print(food2+':'+str(count)+'份')
# print('還須購買的食物及數量')
# for food,count in food_list.items():
#     if not (food in parents_food_list):
#         print(food + ':'+str(count))
#     elif food in parents_food_list and parents_food_list[food]<count:
#         print(food+':'+str(count-parents_food_list[food]))
#字典中的pop可以移出指定鍵的資料(必須存在)
#可以移除鍵(值也會消失不見)
#返回被移出的資料值
# d={1:'a',2:'b'}
# v=d.pop
# print('更新後的字典:',d)
# print('移出的數值',v)
#字典中的pop2:
#可以嘗試移出不存在的鍵
#如果鍵不存在，返回預設值
#如果鍵存在，會變成:
# {2:'b'}
# d={1:'a',2:'b'}
# v=d.pop(0,'刪除資料失敗')
# print('更新後的字典:',d)
# print('移出的數值',v)
# food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
# food_list["冰淇淋"] = 10
# food_list["熱狗"] = 20
# food_list["果汁"] = 25
# # 派對後剩下的食物和數量
# remaining_food = {"蛋糕": 0, "三明治": 5, "果汁": 8, "薯條": 10, \
#                 "披薩": 1, "冰淇淋": 3, "熱狗": 0}
# # 更新食物列表並移除已經吃完的食物
# for food, count in remaining_food.items():
#     if count == 0:
#         food_list.pop(food, None)
#         print(food + "已經吃完")
#     else:
#         food_list[food] = count
# for food, count in food_list.items():
#     if food == "果汁":
#         print(food + ": " + str(count) + "杯")
#     else:
#         print(food + ": " + str(count) + "份")
#字典中的len可以取得字典的長度(鍵值數量)
# food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
# print(len(food_list))
# food_list["冰淇淋"] = 10
# food_list["熱狗"] = 20
# food_list["果汁"] = 25
# print(len(food_list))
gift_list={'小明':'樂高積木','小花':'畫筆','小強':'足球','小美':'書','小偉':'遙控車'}
for name, gift in gift_list.items():
    print(name+'送你一個'+gift)
print('一共收到'+str(len(gift_list))+'個禮物')
