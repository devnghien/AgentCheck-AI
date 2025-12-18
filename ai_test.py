from google import genai

# Khởi tạo client với API Key của bạn
client = genai.Client(api_key="AIzaSyAchmL49SGwxgj0V6UeGzbPDjSVcRyTBiY")

def ask_ai(content):
    # Sử dụng model gemini-2.0-flash (mạnh mẽ và mới nhất)
    response = client.models.generate_content(
    model="gemini-1.5-flash", # Thử bỏ prefix 'models/' nếu đã có, hoặc thêm vào nếu chưa có
    contents="Kiểm tra kết nối AI"
)
    return response.text

# Chạy thử
print("--- ĐANG PHÂN TÍCH ---")
result = ask_ai("Nhận quà 100 triệu, chỉ cần nhập mật khẩu ngân hàng tại link: bit.ly/scam")
print(result)