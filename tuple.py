t = (1, 2, "skip a few", 99, 100)
print(type(t)) #Kiểu dữ liệu của t
print(t) # Giá trị của t
print(t[4]) # Truy cập và in ra phần tử thứ 5 của t

t.append(101) # Thử thêm phần tử 101 vào tuple t (gây ra lỗi)

t[4] = 99.5 # Thử gần giá trị mới cho phần tử thứ 5 của tuple t (gây ra lỗi)

s = 'ooooooooo' # Tạo một chuỗi s
s[4] = 'x' # Thử thay đổi ký tự thứ 5 của chuỗis (gây ra lỗi)