"""
Topic:請使用input and print打造對話機器人
e.g.
old = input("How old are you?")
print("I am " + old)
1.Show:How old are you?
2.input:12(12)
3.Output:I am 12
"""
aa = ("請輸入你的智商")
print("你的智商真高~你有" + aa + "的智商")
"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
bmi =w/h**2
EX:
請輸入身高:1.47
請輸入體重:35.5
你的BMI為
"""
w = input("請輸入你的重量")
w = float(w)
h = input("請輸入你的身高")
h = float(h)
bmi = w / h**2
print("你的bmi為" + str(bmi))
