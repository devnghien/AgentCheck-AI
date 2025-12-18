import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  // Hàm gọi API sang Backend (FastAPI)
  const checkTrust = async () => {
    if (!url) return alert("Vui lòng nhập đường link!")
    
    setLoading(true)
    setResult(null) // Reset kết quả cũ

    try {
      // Gọi vào cái API bạn đã viết hôm qua (Port 8000)
      const response = await fetch(`http://127.0.0.1:8000/check-trust?url=${url}`)
      const data = await response.json()
      setResult(data)
    } catch (error) {
      alert("Lỗi kết nối Server! Bạn đã bật backend (uvicorn) chưa?")
      console.error(error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>🛡️ AgentCheck</h1>
      <p>Hệ thống xác thực tin cậy sử dụng AI</p>
      
      <div className="card">
        <input 
          type="text" 
          placeholder="Nhập link nghi ngờ (ví dụ: facebook.com)..." 
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          className="input-box"
        />
        
        <button onClick={checkTrust} disabled={loading}>
          {loading ? "Đang AI phân tích..." : "Kiểm tra ngay"}
        </button>
      </div>

      {/* Chỉ hiển thị kết quả khi đã có dữ liệu */}
      {result && (
        <div className="result-box">
          <h3>Kết quả phân tích:</h3>
          <p><strong>URL:</strong> {result.url}</p>
          <p><strong>Đánh giá:</strong> {result.analysis}</p>
          <hr/>
          <p className="meta">
            {/* Logic hiển thị nguồn dữ liệu: Cache hay AI mới */}
            Nguồn: {result.status && result.status.includes("Cache") 
              ? "⚡ Lấy từ Cache (Cực nhanh)" 
              : "🤖 AI vừa phân tích"}
          </p>
        </div>
      )}
    </div>
  )
}

export default App