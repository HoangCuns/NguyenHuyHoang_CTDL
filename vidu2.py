# Nhập số từ người dùng 
num = int(input("Nhập một số: "))

# Kiểm tra xem số đó có lớn hơn ở hay không
if num > 0:
    print("Số bạn nhập là số dương.") 
elif num < 0: 
    print("Số bạn nhập là số âm.") 
else:
    print("Số bạn nhập là số không.")