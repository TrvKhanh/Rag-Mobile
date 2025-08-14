# 🤖 AI Chatbot - Hệ thống Tư vấn Điện thoại Thông minh

Một hệ thống chatbot AI tiên tiến được xây dựng để tư vấn về điện thoại, tích hợp với Google Gemini AI, hệ thống RAG (Retrieval-Augmented Generation), và giao diện web hiện đại.

## ✨ Tính năng chính

- 🚀 **FastAPI Backend**: API server mạnh mẽ với auto-documentation
- 💬 **Streamlit Frontend**: Giao diện chat trực quan và thân thiện
- 🤖 **Google Gemini 2.5 Flash**: Tích hợp mô hình AI tiên tiến nhất
- 🔍 **Hệ thống RAG**: Tìm kiếm và truy xuất thông tin thông minh
- 🧠 **LLM Router**: Phân loại và định tuyến câu hỏi thông minh
- 💾 **Memory Management**: Quản lý bộ nhớ và lịch sử chat
- 🎯 **Vietnamese SBERT**: Hệ thống embedding tối ưu cho tiếng Việt
- 🔄 **Hybrid Search**: Kết hợp BM25 và Vector Search
- 📊 **Real-time Response**: Phản hồi nhanh chóng và chính xác

## 🏗️ Kiến trúc hệ thống

```
┌─────────────────┐    HTTP/JSON    ┌─────────────────┐
│   Streamlit     │ ◄─────────────► │   FastAPI       │
│   Frontend      │                 │   Backend       │
│   (Port 8501)   │                 │   (Port 8000)   │
└─────────────────┘                 └─────────────────┘
                                              │
                                              ▼
                                    ┌─────────────────┐
                                    │   Core System   │
                                    │ • LLM Router    │
                                    │ • RAG Engine    │
                                    │ • Memory Mgmt   │
                                    └─────────────────┘
                                              │
                                              ▼
                                    ┌─────────────────┐
                                    │   AI Models     │
                                    │ • Gemini 2.5    │
                                    │ • Vietnamese    │
                                    │   SBERT         │
                                    └─────────────────┘
```

## 📁 Cấu trúc dự án

```
src/
├── api.py                    # FastAPI server chính
├── api_simple.py             # API đơn giản (backup)
├── streamlit.py              # Giao diện Streamlit
├── requirements.txt          # Dependencies
├── README.md                 # Tài liệu dự án
├── data/                     # Dữ liệu và database
│   └── data.chromadb        # ChromaDB database
├── retrival/                 # Hệ thống tìm kiếm
│   ├── llm_router.py        # Phân loại và định tuyến
│   └── re_rank.py           # Hybrid search + re-ranking
└── generation/               # Hệ thống sinh câu trả lời
    └── llm.py               # LLM với memory management
```

## 🚀 Cài đặt

### 1. Clone repository
```bash
git clone <repository-url>
cd chatbot/src
```

### 2. Tạo môi trường ảo
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate     # Windows
```

### 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 4. Cấu hình API Key
Tạo file `.env` trong thư mục `src` và thêm Google AI API key:
```
GOOGLE_API_KEY=your_google_ai_api_key_here
```

## 🎯 Sử dụng

### Chạy API Server
```bash
cd src
python -m uvicorn api:app --reload
```
API server sẽ chạy tại `http://localhost:8000`

### Chạy Streamlit Interface
```bash
cd src
streamlit run streamlit.py
```
Streamlit sẽ chạy tại `http://localhost:8501`

### Chạy API đơn giản (nếu có vấn đề với API chính)
```bash
cd src
python -m uvicorn api_simple:app --reload
```

## 📡 API Endpoints

### Core Endpoints
- `POST /chat/` - Gửi tin nhắn chat
  ```json
  {
    "message": "Xin chào!",
    "thread_id": "optional_thread_id"
  }
  ```

### Response Format
```json
{
  "thread_id": "uuid",
  "response": "Phản hồi từ AI"
}
```

### API Documentation
Truy cập `http://localhost:8000/docs` để xem Swagger UI documentation.

## 🔧 Các thành phần chính

### 1. LLM Router (`retrival/llm_router.py`)
- Phân loại câu hỏi thành 2 loại: `chatchit` (trò chuyện) và `rag` (tìm kiếm thông tin)
- Chuẩn hóa và tóm tắt nội dung câu hỏi
- Tối ưu hóa truy vấn cho hệ thống RAG

### 2. RAG System (`retrival/re_rank.py`)
- **Hybrid Search**: Kết hợp BM25 và Vector Search
- **Re-ranking**: Sử dụng Vietnamese SBERT để sắp xếp kết quả
- **Score Threshold**: Lọc kết quả theo ngưỡng điểm

### 3. LLM with Memory (`generation/llm.py`)
- **ChatWithMemory**: Quản lý bộ nhớ dài hạn và ngắn hạn
- **Auto-summarization**: Tự động tóm tắt khi lịch sử quá dài
- **Thread Management**: Quản lý các cuộc hội thoại riêng biệt

### 4. FastAPI Server (`api.py`)
- RESTful API endpoints
- Error handling và logging
- Thread ID management
- Integration với tất cả components

### 5. Streamlit Interface (`streamlit.py`)
- Giao diện chat trực quan
- Real-time messaging
- Custom CSS styling
- Conversation history

## 💬 Ví dụ sử dụng

### Chat thông thường
```
User: "Chào bạn, hôm nay thời tiết đẹp nhỉ?"
Router: chatchit
Response: "Chào bạn! Lisa đây. Hôm nay thời tiết thật đẹp phải không? Bạn có muốn tìm hiểu về điện thoại nào không?"
```

### Tìm kiếm thông tin sản phẩm
```
User: "Tôi muốn mua iPhone 16, giá bao nhiêu?"
Router: rag
Query: "thông tin chi tiết iphone 16"
Response: "Chào bạn! Lisa đây. Về iPhone 16, đây là thông tin chi tiết..."
```

## 🛠️ Cấu hình nâng cao

### Mô hình AI
- **Generator**: Google Gemini 2.5 Flash
- **Embedding**: Vietnamese SBERT (keepitreal/vietnamese-sbert)
- **Re-ranker**: ViRanker (namdp-ptit/ViRanker)

### Database
- **Vector Store**: ChromaDB
- **Collection**: "production"
- **Persistence**: Local file system

### Performance
- **Top-k**: 3-5 documents
- **Score Threshold**: 5.0
- **Memory Threshold**: 10 messages

## 🔍 Troubleshooting

### Lỗi thường gặp

1. **Collection không tồn tại**
   - Tự động tạo collection mặc định
   - Thêm documents mẫu

2. **Tensor iteration error**
   - Đã fix trong `re_rank.py`
   - Xử lý tensor 0-d

3. **API key không hợp lệ**
   - Kiểm tra file `.env`
   - Đảm bảo API key có quyền truy cập Gemini

### Debug Mode
Thêm print statements trong code để debug:
```python
print("[DEBUG]", router["router"])
print("[DEBUG]", relust)
```

## 📈 Performance Tips

1. **Sử dụng API đơn giản** nếu không cần RAG
2. **Giảm top-k** để tăng tốc độ
3. **Tăng score threshold** để giảm noise
4. **Sử dụng thread_id** để duy trì context

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:
1. Fork repository
2. Tạo branch mới
3. Commit changes
4. Tạo Pull Request

## 📄 License

MIT License - xem file LICENSE để biết thêm chi tiết.

## 📞 Hỗ trợ

Nếu gặp vấn đề, vui lòng:
1. Kiểm tra logs trong terminal
2. Xem API documentation tại `/docs`
3. Tạo issue trên GitHub

---

**Lưu ý**: Đảm bảo có kết nối internet để sử dụng Google AI API và tải các mô hình embedding. 