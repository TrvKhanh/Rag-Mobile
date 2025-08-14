import importlib.metadata

packages = [
    "chromadb",
    "sentence-transformers",
    "langchain",
    "langgraph",
    "langchain-community",
    "rank-bm25",
    "langchain-google-genai",
    "langchain-chroma",
    "fastapi",
    "uvicorn"
]

with open("requirements.txt", "w") as f:
    for pkg in packages:
        try:
            ver = importlib.metadata.version(pkg)
            f.write(f"{pkg}=={ver}\n")
        except importlib.metadata.PackageNotFoundError:
            print(f"⚠️ Không tìm thấy package: {pkg}")
        except Exception as e:
            print(f"⚠️ Lỗi khi lấy version của {pkg}: {e}")

print("✅ requirements.txt đã được tạo thành công!")
