import copy

""" arr = [1, 42, 16, 8]
print(arr)
arr.append(28)
print(arr)
arr.insert(2, 10500)
print(arr)
arr.remove(10500)
print(arr)
arr.clear()
print(arr)
arr.append(55)
arr.append(65)
arr.append(75)
arr.append(85)
print(arr)
# print(arr.index(100500))
arr.pop()
print(arr)
arr.pop(1)
print(arr)
arr.append(8)
arr.append("Microsoft")
arr.append(8)
arr.insert(1,8)
print(arr)
print(arr.count(8))
#print(arr.sort())
arr.reverse()
arr.remove("Microsoft")
print(arr)
print(len(arr))
print(min(arr))
print(max(arr))

for x in arr:
    print(x)

names = ["Bob", "Uitny", "Lussy", "Dan", "Alise", "Kite"]
names.sort()
print(names)
for i in names:
    print (i)

names1 = ["Tom", "Bob", "Uitny", "Lussy", "Dan", "Alise", "Kite"]
#names2 = names1
names2 = copy.deepcopy(names1)
print("names1: ", names1)
print("names2: ", names2)
names2.append("Stive")
print("names1: ", names1)
print("names2: ", names2)

names3 = names1[3:5]
print("names3: ", names3)
names3 = names1[:2]
print("names3: ", names3)
names3 = names1[3:5:2]
print("names3: ", names3)

"""
# # -------1v---------
# num = [5, 75, 82, 2, 15, 1, 14]
# print(num)
# min_value = min(num)
# max_value = max(num)
# min_index = num.index(min_value)
# max_index = num.index(max_value)
# print("min_value", min_value)
# print("max_value", max_value)
# print("min_index", min_index)
# print("max_index", max_index)
# temp = num[min_index]
# num[min_index] = num[max_index]
# num[max_index] = temp

# print("New Arr = ", num)

# # -------2v---------
# num1 = [5, 75, 82, 2, 15, 1, 14]
# summ = sum(num1[1::2])
# print(summ)


# # -------3v---------
# num2 = [1, 2, 3, 4, 5]
# num3 = copy.deepcopy(num2)
# print("num2: ", num2)
# print("num3: ", num3)

# # -------4v---------
# num4 = [11, 12, 13, 14, 15]
# num5 = [16, 17, 18, 19, 20]
# num6 = []
# num6.extend(num4)
# num6.extend(num5)
# print(num6)





