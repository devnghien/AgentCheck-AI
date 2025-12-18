import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Lấy key từ file .env (file này sẽ nằm trong .gitignore)
API_KEY=os.getenv("GGAI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1/models?key={API_KEY}"

response = requests.get(url)
models = response.json()

if 'models' in models:
    print("CÁC MODEL BẠN CÓ THỂ DÙNG:")
    for m in models['models']:
        # Chỉ lấy những model hỗ trợ tạo nội dung (generateContent)
        if 'generateContent' in m['supportedGenerationMethods']:
            print(f"- {m['name']}")
else:
    print("Lỗi khi lấy danh sách:", models)