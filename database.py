from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

#Sử dụng SQLite cho ví dụ này
SQLALCHEMY_DATABASE_URL = "sqlite:///./agentcheck.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Định nghĩa mô hình dữ liệu cho bảng (Model)
class VerificationRecord(Base):
    __tablename__ = "verification_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    analysis = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

#Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)