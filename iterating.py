mylist = [1, 3, 5]
mytuple = (1, 2, 'skip a few', 99, 100)
myset = {'a', 'b', 'z'}
mystring = 'abracadabra'
mydict = {'a': 96, 'b': 97, 'c': 98}

# Lặp qua danh sách (list)
for item in mylist:
    print(item)
# Kết quả:
# 1
# 3
# 5

# Lặp qua tuple
for item in mytuple:
    print(item)
# Kết quả:
# 1
# 2
# skip a few
# 99
# 100

# Lặp qua tập hợp (set)
for element in myset:
    print(element)
# Kết quả:
# a
# b
# z

# Lặp qua chuỗi (string)
for character in mystring:
    print(character)
# Kết quả:
# a
# b
# r
# a
# c
# a
# d
# a
# b
# r
# a

# Lặp qua từ điển (dictionary) để lấy các khóa (keys)
for key in mydict:
    print(key)
# Kết quả:
# a
# b
# c

# Lặp qua từ điển để lấy cả khóa và giá trị (key và value)
for key, value in mydict.items():
    print(key, value)
# Kết quả:
# a 96
# b 97
# c 98

# Lặp qua từ điển để lấy giá trị (value)
for value in mydict.values():
    print(value)
# Kết quả:
# 96
# 97
# 98

# Sử dụng lớp range để lặp qua dãy số
for i in range(10):
    j = 10 * i + 1
    print(j, end=' ')

# kết quả : 1 11 21 31 41 51 61 71 81 91 
