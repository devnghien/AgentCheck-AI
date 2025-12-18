from fastapi import FastAPI, Depends
from groq import Groq
from sqlalchemy.orm import Session
import database # Import module database đã tạo
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()
# Cho phép Frontend (React) gọi vào Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()
# Lấy key từ file .env (file này sẽ nằm trong .gitignore)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Hàm lấy kết nối DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/check-trust")
def check_trust(url: str, db: Session = Depends(get_db)):
    # Kiểm tra trước khi gửi yêu cầu đến AI
    existing_log = db.query(database.VerificationRecord).filter(database.VerificationRecord.url == url).first()
    if existing_log:
        print(f"Lấy kết quả từ Cache cho URL: {url}")
        return {
            "id": existing_log.id,
            "url": existing_log.url,
            "analysis": existing_log.analysis,
            "saved_at": existing_log.created_at
        }
    # Nếu chưa có trong DB, gọi AI để phân tích
    print(f"Chưa có trong cache, gọi AI phân tích cho URL: {url}")

    # Sử dụng model Llama 3 (của Meta) chạy trên hạ tầng Groq
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user", 
                "content": f"Link này có an toàn không: {url}"
            }
        ]
    )
        
    ai_text = completion.choices[0].message.content
    # Lưu kết quả vào DB
    new_log = database.VerificationRecord(
        url=url,
        analysis=ai_text
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return {
        "status": "Success (New Analysis)",
        "url": url, 
        "analysis": ai_text, 
        "saved_at": new_log.created_at
    }