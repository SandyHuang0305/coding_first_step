#fibonaci series :裴波納契數列
#兩個元素的總和確定了下一個數
a, b = 0, 1
while b < 10:
	print(b)
	a, b = b, a+b

#輸出變量值:
i = 256*256
print('i的值為',i)

#end的使用方法:可以將結果輸出在同一行or添加符號
a, b = 0, 1
while b < 1000:
	print(b, end=',')
	a,b = b, a+b


			
