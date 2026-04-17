import math

# Nhập số
x = float(input("Nhập số cần tính căn bậc 2: "))

# Kiểm tra điều kiện
if x < 0:
    print("Không thể tính căn bậc 2 của số âm (trong số thực)")
else:
    result = math.sqrt(x)
    print("Căn bậc 2 của", x, "là:", result)
