<<<<<<< HEAD
import requests

API_KEY = "AIzaSyAchmL49SGwxgj0V6UeGzbPDjSVcRyTBiY"
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
=======
import requests

API_KEY = "AIzaSyAchmL49SGwxgj0V6UeGzbPDjSVcRyTBiY"
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
>>>>>>> dc83ea6796fa2aa4883397a1ddac607ce7af01dc
    print("Lỗi khi lấy danh sách:", models)