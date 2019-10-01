list_num = [i for i in range(1,10)]
print(list_num)
list_num = list(range(10))
print(list_num)
list_num= list(range(100))
print(list_num)
even = [i for i in range(0,10,2)]
print(even)
dict = {"a":1,"b":2,"c":3}
key_list = list(dict.keys())
print(key_list)
value_list = list(dict.values())
print(value_list)

add =5,7,9,10
res = sum(add)
print(res)