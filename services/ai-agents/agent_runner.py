import openai, os, asyncio
SYSTEMS = {
 "support": "You are a helpful enterprise customer support agent. Use RAG context. Be concise.",
 "sales": "You are a B2B sales agent. Qualify leads, book demos.",
 "research": "Research agent with web/MCP tools. Cite sources.",
 "analyst": "Data analyst. Write SQL, explain metrics.",
 "builder": "n8n workflow builder agent. Output valid n8n JSON.",
 "content": "Content generator for marketing campaigns."
}
async def run_agent(agent_type: str, user_input: str):
    client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    resp = await client.chat.completions.create(model="gpt-4o", messages=[{"role":"system","content":SYSTEMS.get(agent_type, SYSTEMS["support"])},{"role":"user","content":user_input}])
    return resp.choices[0].message.content
if __name__ == "__main__":
    print(asyncio.run(run_agent("support","Hello")))
