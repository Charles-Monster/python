# l = ['a', 'b', 'c', 'd']
# print(l)
#  ['A'] 'A'
# print(l)
#如果這樣打的話
#l[0] = ['A']
#會在清單裡面在新增一個清單
#結果:['a' ['A'], 'b', 'c', 'd']
# 所以如果要把一個清單中的元素換掉的話，就不能在家中括號。
#正確寫法:
#?[?] ='?'
# weather = ['晴天', '多雲', '雨天', '陰天', '晴天', '多雲', '雷陣雨', '晴天']
# print(weather)

# while True:
#     try:
#         ans = int(input('請輸入要修改的星期數字(1~7)'))
#     except:
#         print('請輸入數字編號')
#     else:
#         if ans > len(weather) or ans < 1:
#             print('輸入錯誤查無此星期，請重新輸入')
#         else:
#             print('您要修改的是' + str(ans))
#             print('原本的天氣' + weather[ans - 1])
#             new_weather = input('請輸入新的天氣:')
#             weather[ans - 1] = new_weather
#             print('修改後的天氣是' + weather[ans - 1])
#             print(weather)
#             break
# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)
# l = ['a', 'b', 'c']
# a = l.copy()
# a[0] = 1
# print(a, l)
# 新變數 = 原始串列.copy()
# fruit_list = ['火龍果', '哈密瓜', '百香果', '橘子', '蘋果', '香蕉', '梨', '李', '桃']
# print('最長的水果名字是' + max(fruit_list))
# print('最短的水果名字是' + min(fruit_list))
# birthday='2023/10/20'
# birthday=birthday.split('/')
# birthday='-'.join(birthday)
# print(birthday)
