# 1. Biến (Variables): Nơi lưu trữ dữ liệu
name = "Founding Engineer" # Chuỗi (String)
days_left = 60             # Số nguyên (Integer)
is_ready = True            # Logic (Boolean)

# 2. Hàm (Functions): Một cỗ máy xử lý nhỏ
def start_journey(role, days):
    # f-string: Cách nhúng biến vào chuỗi trong Python
    print(f"--- BẮT ĐẦU ---")
    print(f"Mục tiêu: Trở thành {role}")
    
    # 3. Điều kiện (If-Else)
    if days < 30:
        return "Không thể, quá gấp!"
    else:
        return f"Còn {days} ngày. Chiến đấu thôi!"

# 4. Chạy chương trình
# Gọi hàm và in kết quả ra màn hình
result = start_journey(name, days_left)
print(result)