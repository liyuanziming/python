#map:對每個數據都執行transform操作
#filter:條件過濾，只留下符合條件的

da = [1,3,5,6,34,23,54,1,23,32,22,11,33]

result = list(map(lambda x:x+5,da))

print(result)

result2 = list(filter(lambda x:x > 10 ,da))

print(result2)

