import uuid
import chromadb
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.documents import Document
from langchain_core.messages import SystemMessage, HumanMessage
from retrival.llm_router import llm_router
from retrival.re_rank import ReRank
from generation.llm import ChatWithMemory


app = FastAPI()


path_database = "data/data.chromadb"
client = chromadb.PersistentClient(path_database)

collections = client.get_collection("production")
all_data = collections.get()


documents = [
    Document(page_content=doc, metadata=meta)
    for doc, meta in zip(all_data["documents"], all_data["metadatas"])
]


search = ReRank(3, path_database, documents, "production")

llm = ChatWithMemory().compile() 




thread_id =  str(uuid.uuid4())

class ChatRequest(BaseModel):
    message: str
    thread_id: str | None = None


@app.post("/chat/")
def chat(req: ChatRequest):


    router = llm_router(req.message)

    print("[DEBUG]", router["router"])
    if router["router"] == "rag":
        relust = search.query(router["infor"])
        print("[DEBUG]", relust)
        system_prompt_template = f"""Bạn là một nhân viên tư vấn của shop điện thoại.
                                    Nhiệm vụ:
                                    - Hãy trả lời một cách thân thiện, minh bạch.
                                    - Luôn giữ văn phong lịch sự, chuyên nghiệp, không dùng ngôn ngữ lập lờ hay viết hoa toàn bộ.
                                    - Dựa vào thông tin có sẵn, hãy trả lời chi tiết cho người dùng dễ hiểu, tiếp cận thông tin như sau: {relust}
                                    """ 

        messages = [
            SystemMessage(content=system_prompt_template),
            HumanMessage(content=req.message)
        ]
    else:
        messages = [HumanMessage(content=req.message)]

    response = llm.invoke(
        input={"messages": messages},
        config={"configurable": {"thread_id": thread_id}}
    )

    ai_reply = response["messages"][-1].content

    print(ai_reply)

    return {
        "thread_id": thread_id,
        "response": ai_reply
    }
