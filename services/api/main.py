from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncpg, os, jwt, datetime
app = FastAPI(title="Automation Platform API", version="2026.1")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
DB_URL = os.getenv("DATABASE_URL","postgres://automation:postgres@localhost/automation")
JWT_SECRET = os.getenv("JWT_SECRET","change_me")

async def db(): return await asyncpg.connect(DB_URL)

@app.get("/health")
async def health(): return {"ok": True, "version": "2026.1"}

class AuthLogin(BaseModel):
    email: str; password: str
@app.post("/v1/auth/login")
async def login(b: AuthLogin):
    # demo – in prod verify bcrypt
    token = jwt.encode({"sub": b.email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)}, JWT_SECRET, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

@app.get("/v1/workflows")
async def list_workflows(org_id: str = "00000000-0000-0000-0000-000000000001"):
    conn = await db()
    rows = await conn.fetch("SELECT id, name, slug, is_active FROM workflows WHERE organization_id=$1 ORDER BY created_at DESC", org_id)
    await conn.close()
    return [dict(r) for r in rows]

class RagQuery(BaseModel):
    organization_id: str; query: str; k: int = 5
@app.post("/v1/rag/search")
async def rag_search(q: RagQuery):
    conn = await db()
    rows = await conn.fetch("SELECT id, title, content FROM vector_documents WHERE organization_id=$1 ORDER BY created_at DESC LIMIT $2", q.organization_id, q.k)
    await conn.close()
    return {"results": [dict(r) for r in rows]}

class ChatIn(BaseModel):
    agent_type: str; message: str
@app.post("/v1/agents/chat")
async def agent_chat(b: ChatIn):
    # proxy to OpenAI in production – here echo
    return {"agent": b.agent_type, "reply": f"[{b.agent_type}] received: {b.message[:120]}"}
