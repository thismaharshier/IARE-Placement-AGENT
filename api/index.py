import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI()

# Data (Use your actual chunked placement data here)
placement_docs = [
    Document(page_content="Accenture: Hiring 2025 Batch. Roles: Associate / Advanced Associate Software Engineer. Salary: ₹4.5 - 6.5 LPA. Recruitment: 26-28 September 2024. Eligibility: B.Tech, No Active Backlogs, Branches: CSE, IT, CSIT, CSE(AI&ML), CSE(DS), CSE(CS), ECE, EEE, AERO, MECH, CIVIL."),
    Document(page_content="UTS (Unistring Tech Solutions): Hiring 2025 Batch. Role: Jr. Hardware Design Engineer. Salary: ₹5.0 LPA. Recruitment: 05 September 2024. Eligibility: B.Tech - ECE & EEE, No Active Backlogs."),
    Document(page_content="Goldman Sachs: Hiring Final (Full-time) & Pre-final (Interns). Salary: ₹30 LPA. Timeline: Internships (Aug-Sep), ECHP (Jan-Mar)."),
    Document(page_content="ZeroCodeHR: Hiring 2027 Passout. Role: Implementation Analyst. Salary: ₹9 LPA (Intern Stipend: ₹32K/PM). Recruitment: 17 March 2026. Eligibility: 8.0 CGPA, No Backlogs."),
    Document(page_content="JUSPAY: Hiring 2026 Batch. Role: System Reliability Engineer (SRE). Salary: ₹11.0 LPA. Recruitment: November 2025.")
]

# Initialize AI Components globally to keep them warm
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = InMemoryVectorStore.from_documents(placement_docs, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are the official IARE Campus Placement AI Agent. Answer using only the context provided. If you don't know, say so.\n\nContext:\n{context}"),
    ("human", "{input}"),
])

qa_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, qa_chain)

class UserQuery(BaseModel):
    query: str

@app.post("/api/chat")
def chat_with_agent(req: UserQuery):
    try:
        response = rag_chain.invoke({"input": req.query})
        return {"answer": response["answer"]}
    except Exception as e:
        return {"answer": f"Error connecting to agent: {str(e)}"}
