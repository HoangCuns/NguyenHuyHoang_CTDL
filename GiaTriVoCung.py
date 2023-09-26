# Tạo biến numstring và gán giá trị là chuỗi "3.1415926"
numstring = "3.1415926"

# Sử dụng hàm float() để chuyển đổi chuỗi numstring thành số thực và lưu vào biến y
y = float(numstring)

# In ra kiểu dữ liệu của biến y bằng hàm type()
print("y has type", type(y))

# Tạo biến best_number và gán giá trị là số nguyên 73
best_number = 73

# Sử dụng hàm str() để chuyển đổi số nguyên best_number thành chuỗi và lưu vào biến x
x = str(best_number)

# In ra kiểu dữ liệu của biến x
print("x has type", type(x))

# Tạo biến thisworks và gán giá trị là float("inf"), tạo ra một giá trị vô cùng (infinity)
thisworks = float("inf")

# In ra kiểu dữ liệu của biến thisworks
print("float('inf') has type", type(thisworks))

# Thực hiện phép toán float('inf') + 1, kết quả sẽ là một giá trị vô cùng mới
infinity_plus_one = float('inf') + 1
