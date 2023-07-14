'''
今天python一樣要做自我介紹，他要介紹自己的年齡，班上有一位同學她今年8歲，你們要讓python說出自己跟那位同學加起來幾歲！
EX:
請輸入python年齡:10
python與同學年齡加起來16歲
'''
name = "python"
age = int(input("請輸入你的年齡:"))
age2 = age + 8
print('我叫做' + name + '我今年' + str(age) + '我同學' + '今年8歲我們兩個的歲數加起來總共是' +
      str(age + 8))
