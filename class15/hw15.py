'''
hw15
請將hw13的作業升級
• 請將果汁新增到list並使用list完成之前的功能
juices_list = ["蘋果汁","柳橙汁","葡萄汁","系統關閉"]
'''

while True:
    juices_list = ["1.蘋果汁", "2.柳橙汁", "3.葡萄汁", "4.系統關閉"]
    for index in range(len(juices_list)):
        print(juices_list[index])
    ans = input("請輸入編號:")
    if ans == "1":
        print(ans[0])
    elif ans == "2":
        print(ans[1])
    elif ans == "3":
        print(ans[2])
    elif ans == "4":
        print(ans[3])
        break
    else:
        print("輸入錯誤查無此果汁，請重新輸入")