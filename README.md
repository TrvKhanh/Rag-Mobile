# 🤖 AI Chatbot - Hệ thống Tư vấn Điện thoại 

Một hệ thống RAG (Retrieval-Augmented Generation) tư vấn điện thoại

## ✨ Tính năng chính

- 🚀 **FastAPI Backend**: Tạo api
- 💬 **Streamlit Frontend**:Giao diện cơ bản
- 🤖 **Google Gemini 2.5 Flash**
- 🔍 **Hệ thống RAG**: Tìm kiếm và truy xuất thông tin 
- 🧠 **LLM Router**: Phân loại và định tuyến câu hỏi 
- 💾 **Memory Management**: Quản lý bộ nhớ và lịch sử chat
- 🔄 **Hybrid Search**: Kết hợp BM25 và Vector Search


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
                                    │                 │
                                    └─────────────────┘
```

## 📁 Cấu trúc dự án

```
src/
├── api.py                    # FastAPI server chính           # API đơn giản (backup)
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

