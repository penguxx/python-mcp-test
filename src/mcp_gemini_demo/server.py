import platform
from datetime import datetime
from mcp.server.mcpserver import MCPServer
mcp = MCPServer("mcp-gemini-demo")


@mcp.tool()
def get_system_info() -> str:
    """Get operating system and date/time information."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os_name = platform.system()
    os_version = platform.release()
    return f"System: {os_name} {os_version} | Uhrzeit: {now}"

if __name__ == "__main__":
    # Startet den Server über Standard-Ein-/Ausgabe (stdio)
    mcp.run()