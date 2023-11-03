'''
請幫點餐機設計一個選單，當顧客
使用點餐機時，可以看到所有可以
選擇的功能，並告訴機器他們想做什麼。
歡迎使用點餐機！請選擇您想要的功能(輸入數字)：
1. 新增餐點到點餐清單
2. 從點餐清單中移除特定餐點
3. 在指定位置加入餐點
4. 計算點餐清單中某餐點的數量
5. 取消點餐清單中的最後一項餐點
6. 取消點餐清單中特定位置的餐點
7. 顯示升序排序的點餐清單
8. 顯示降序排序的點餐清單
9. 反轉點餐清單的順序
10. 查詢餐點在點餐清單中的位置
11. 退出點餐機
'''
print('''
1. 新增餐點到點餐清單
2. 從點餐清單中移除特定餐點
3. 在指定位置加入餐點
4. 計算點餐清單中某餐點的數量
5. 取消點餐清單中的最後一項餐點
6. 取消點餐清單中特定位置的餐點
7. 顯示升序排序的點餐清單
8. 顯示降序排序的點餐清單
9. 反轉點餐清單的順序
10. 查詢餐點在點餐清單中的位置
11. 退出點餐機
''')
A_list = []
while True:
    ans = int(input("歡迎使用點餐機！請選擇您想要的功能(輸入數字)："))
    if ans == 1:
        print('您選擇的功能是:1. 新增餐點到點餐清單')
        new_list = input('請輸入新的菜單:')
        A_list.append(new_list)
        print('以新增餐點到點餐清單')
    elif ans == 2:
        print('您選擇的功能是:2. 從點餐清單中移除特定餐點')
        number_list = input('請輸入您想要移除的餐點:')
        if number_list in A_list:
            A_list.remove(number_list)
            print('已從點餐清單中移除特定餐點!')
        else:
            print('該餐點不在清單中!')
    elif ans == 3:
        print('您選擇的功能是:3. 在指定位置加入餐點')
        position = int(input('請輸入您想要插入的位置:'))
        order = input('請輸入您想要加入的餐點:')
        A_list.insert(position, order)
        print('已在指定位置中加入餐點!')

    elif ans == 4:
        print('您選擇的功能是:4. 計算點餐清單中某餐點的數量')
        order = input('請輸入您想要計算的餐點')
        count = A_list.count(order)
        print('餐點' + order + '在點餐清單中的數量是:' + str(count))
    elif ans == 5:
        print('您選擇的功能是:5. 取消點餐清單中的最後一項餐點')
        if A_list:
            A_list.pop()
            print('已取消點餐清單中的最後一項餐點!')
        else:
            print('點餐清單是空的!')
    elif ans == 6:
        print('您選擇的功能是:6. 取消點餐清單中特定位置的餐點')
        position = int(input('請輸入您想要取消的餐點位置:'))
        if 0 <= position < len(A_list):
            A_list.pop(position)
            print('已取消點餐清單中特定位置的餐點!')
        else:
            print('輸入的位置不正確!')
    elif ans == 7:
        print('您選擇的功能是:7. 顯示升序排序的點餐清單')
        A_list.sort()
        print('點餐出餐順序以按升序排序!')
    elif ans == 8:
        print('您選擇的功能是:8. 顯示降序排序的點餐清單')
        A_list.sort(reverse=True)
        print('點餐出餐順序以按降序排序!')
    elif ans == 9:
        print('您選擇的功能是:9. 反轉點餐清單的順序')
        A_list.reverse()
        print('點餐清單出餐順序已反轉!')
    elif ans == 10:
        print('您選擇的功能是:10. 查詢餐點在點餐清單中的位置')
        order = input('請輸入您想要查詢出餐順序的餐點:')
        if order in A_list:
            index = A_list.index(order)
            print('餐點' + order + '出餐的順序是:' + str(index))
        else:
            print('該餐點不在清單中!')
    elif ans == 11:
        print('您選擇的功能是:11. 退出點餐機')
        print('系統關閉---')
        break
