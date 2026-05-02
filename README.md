# SMA MCP SSE n8n Client

A Python MCP server using Server-Sent Events (SSE), designed to expose tools that can be consumed by clients such as n8n MCP Client.

## Overview

This project demonstrates how to build an MCP server with Python using `FastMCP`.

The server exposes two tools:

- `get_employee_data`: returns sample employee information
- `web_search`: performs web search using the Tavily API

The server runs on:


http://localhost:23000/sse