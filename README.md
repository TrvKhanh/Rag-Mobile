# 🤖 AI Chatbot với FastAPI + Streamlit

Một ứng dụng chatbot thông minh được xây dựng bằng FastAPI (backend) và Streamlit (frontend), tích hợp với Google Gemini AI và hệ thống RAG (Retrieval-Augmented Generation).

## ✨ Tính năng

- 🚀 **FastAPI Backend**: API server mạnh mẽ với auto-documentation
- 💬 **Streamlit Frontend**: Giao diện chat trực quan và thân thiện
- 🤖 **Google Gemini AI**: Tích hợp mô hình AI tiên tiến
- 🔍 **Vietnamese SBERT**: Hệ thống embedding cho tiếng Việt
- 💾 **Conversation Management**: Quản lý lịch sử chat theo conversation
- 📊 **Real-time Stats**: Thống kê thời gian thực
- 🎨 **Modern UI**: Giao diện đẹp mắt với CSS tùy chỉnh
- 🔧 **RESTful API**: API đầy đủ cho tích hợp với ứng dụng khác

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
                                    │   AI Models     │
                                    │ • Generator     │
                                    │ • Embedding     │
                                    └─────────────────┘
```

## 🚀 Cài đặt

### 1. Clone repository
```bash
git clone <repository-url>
cd ChatBot
```

### 2. Tạo môi trường ảo
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate  # Windows
```

### 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 4. Cấu hình API Key
Tạo file `.env` trong thư mục gốc và thêm Google AI API key:
```
GOOGLE_API_KEY=your_google_ai_api_key_here
```

## 🎯 Sử dụng

### Chạy toàn bộ hệ thống (Khuyến nghị)
```bash
python run_full_system.py
```

### Chạy riêng lẻ

#### 1. Chạy API Server
```bash
python api/main.py
```
API server sẽ chạy tại `http://localhost:8000`

#### 2. Chạy Streamlit Interface
```bash
streamlit run app/chatbot_interface.py
```
Streamlit sẽ chạy tại `http://localhost:8501`

## 📡 API Endpoints

### Core Endpoints
- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /chat` - Gửi tin nhắn chat
- `POST /initialize` - Khởi tạo mô hình AI

### Conversation Management
- `GET /conversations` - Lấy danh sách conversations
- `GET /conversations/{id}` - Lấy lịch sử conversation
- `DELETE /conversations/{id}` - Xóa conversation
- `DELETE /conversations` - Xóa tất cả conversations

### Statistics
- `GET /stats` - Lấy thống kê hệ thống

### API Documentation
Truy cập `http://localhost:8000/docs` để xem Swagger UI documentation.

## 💬 Sử dụng API

### Gửi tin nhắn chat
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Xin chào!", "conversation_id": "optional_id"}'
```

### Lấy thống kê
```bash
curl "http://localhost:8000/stats"
```

### Health check
```bash
curl "http://localhost:8000/health"
```

## 📁 Cấu trúc dự án

```
ChatBot/
├── api/
│   └── main.py                 # FastAPI server
├── app/
│   └── chatbot_interface.py    # Streamlit frontend
├── src/
│   ├── generation/
│   │   ├── generator.py        # Mô hình AI chính
│   │   └── memory.py          # Quản lý bộ nhớ
│   ├── embedding/
│   │   └── embedding_model.py  # Mô hình embedding
│   ├── retrieval/              # Hệ thống retrieval
│   └── rag_system.py          # Hệ thống RAG chính
├── .streamlit/
│   └── config.toml            # Cấu hình Streamlit
├── requirements.txt
├── run_full_system.py         # Script chạy toàn bộ hệ thống
└── README.md
```

## 🔧 Cấu hình

### Mô hình AI
- **Generator**: Google Gemini 1.5 Flash
- **Embedding**: Vietnamese SBERT (keepitreal/vietnamese-sbert)

### Ports
- **API Server**: 8000
- **Streamlit**: 8501

### Environment Variables
- `GOOGLE_API_KEY`: Google AI API key

## 🛠️ Phát triển

### Thêm API endpoints
1. Thêm endpoint mới trong `api/main.py`
2. Cập nhật Pydantic models nếu cần
3. Test với Swagger UI

### Tùy chỉnh giao diện
Chỉnh sửa CSS trong `app/chatbot_interface.py` hoặc thêm components mới.

### Tích hợp với ứng dụng khác
Sử dụng REST API endpoints để tích hợp chatbot vào ứng dụng của bạn.

## 📝 Ghi chú

- Đảm bảo có kết nối internet để sử dụng Google AI API
- API key cần có quyền truy cập vào Google Generative AI
- Mô hình embedding sẽ được tải lần đầu khi khởi tạo
- Hệ thống hỗ trợ multiple conversations

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:
1. Fork repository
2. Tạo branch mới
3. Commit changes
4. Tạo Pull Request

## 📄 License

MIT License - xem file LICENSE để biết thêm chi tiết. 