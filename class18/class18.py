#sort 可以排列由小至大的元素
# l = [3, 1, 5, 4, 2]
# l.sort(reverse=True)
# print(l)
#reverse (sort中的)可以將程式排序倒過來
#reverse可以顛倒串列的順序
# l = [3, 1, 5, 4, 2]
# l.reverse()
# print(l)
#index可以找到串列中對應元素質的位置所引，且指定的元素必須存在，索引對應第一個找到元素位置
# l = ['a', 'b', 'c', 'a']
# print(l.index('a'))

#字典資料型態Dictionary
#可以保存鍵與值對應資料
#可以修改元素值
#使用{}表示，用逗號分隔資料內容，用分號:表示鍵與值
#字典內的元素都沒有順序
# {'星期一': '蘋果', '星期二': '香蕉'}
#使用大括號包含鍵值資料，鍵與值以分號區隔
#指令格式:{key: value,.......}
#取得鍵(key)並的數值
# book = {'書名': 'jojo的奇幻冒險', '作者': 'dddd'}
# book['書名']
# book['作者']

#元素走訪可以處裡字典中的每個元素(key)
#下面是元素走訪的例子:
# food={'星期一':'蘋果','星期二':'香蕉','星期三':'葡萄'}
# for week in food:
#     print(week)
#結果為星期一，星期二，星期三
food = {'星期一': '蘋果', '星期二': '香蕉', '星期三': '葡萄'}
for week in food:
    print(food[week])
#keys可以列舉字典裡的所有key，返回key的串列
# d = {1: 'a', 2: 'b'}
# keys = d.keys()
# for key in keys:
#     print(key)
#指令格式:
#字典.keys
#執行結果:
#1
#2
