# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Sample MCP client for testing turbopuffer-mcp server locally."""

import asyncio

from dedalus_mcp.client import MCPClient
from dedalus_mcp.client.errors import AuthRequiredError

SERVER_URL = "http://localhost:8080/mcp"


async def main() -> None:
    try:
        client = await MCPClient.connect(SERVER_URL)
    except AuthRequiredError:
        print("Server requires OAuth/DAuth authentication. Use an authenticated MCP client.")
        return

    tools = await client.list_tools()
    print(f"\nAvailable tools ({len(tools.tools)}):\n")
    for tool in tools.tools:
        print(f"  {tool.name}")

    print("\n--- smoke_ping ---")
    ping = await client.call_tool("smoke_ping", {"message": "hello from client"})
    print(ping)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
