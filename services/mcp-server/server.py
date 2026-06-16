from mcp.server.fastmcp import FastMCP
mcp = FastMCP("automation-platform")
@mcp.tool()
def postgres_query(sql: str) -> str:
    # Read-only analytics query with RLS
    return "rows..."
@mcp.tool()
def n8n_trigger(workflow_id: str, payload: dict) -> str:
    return "triggered"
@mcp.tool()
def s3_get(key: str) -> str:
    return f"s3://bucket/{key}"
if __name__ == "__main__":
    mcp.run()
