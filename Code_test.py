# Nhập các thông tin cần thiết
so_tien_vay = float(input("Nhập số tiền vay (VND): "))
lai_suat_hang_nam = float(input("Nhập lãi suất hàng năm (%): ")) / 100
thoi_han_vay = int(input("Nhập thời hạn vay (số năm): "))

# Chuyển đổi lãi suất hàng năm thành lãi suất hàng tháng
lai_suat_hang_thang = lai_suat_hang_nam / 12

# Tính tổng số kỳ thanh toán (tháng)
tong_so_ky = thoi_han_vay * 12

# Công thức tính khoản thanh toán hàng tháng
khoan_thanh_toan_hang_thang = (so_tien_vay * lai_suat_hang_thang) / (1 - (1 + lai_suat_hang_thang) ** -tong_so_ky)

# In kết quả
print(f"Số tiền thanh toán hàng tháng là: {khoan_thanh_toan_hang_thang:.2f} VND")
