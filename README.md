# YouTube MCP Server

A Model Context Protocol (MCP) server that provides YouTube-related tools including transcript extraction and name digitization.

## Features

- **YouTube Transcript Extraction**: Get transcripts from YouTube videos
- **Video ID Extraction**: Extract video IDs from YouTube URLs
- **Name Digitization**: Convert names to ASCII code format

## Configuration

The server can be configured using environment variables. Copy `.env.example` to `.env` and modify as needed:

```bash
cp .env.example .env
```

### Environment Variables

- `HOST`: Server host (default: `0.0.0.0`)
- `PORT`: Server port (default: `8000`)
- `LOG_LEVEL`: Logging level (default: `INFO`)
- `MCP_SERVER_NAME`: Server name (default: `YouTube MCP Server`)
- `MCP_SERVER_VERSION`: Server version (default: `0.1.0`)
- `PYTHONUNBUFFERED`: Python output buffering (default: `1`)

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Local Development

```bash
# Install dependencies
uv sync

# Copy environment variables
cp .env.example .env

# Run the server
uv run server.py
```

### Docker

```bash
# Build the Docker image
docker build -t youtube-mcp-server .

# Run the container
docker run --rm youtube-mcp-server

# Run with port mapping for HTTP access
docker run --rm -p 8000:8000 youtube-mcp-server
```

### Docker Compose

For easier management and deployment:

```bash
# Start the service
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the service
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

#### Production Deployment

For production with additional services like reverse proxy:

```bash
# Start with production profile
docker-compose -f docker-compose.yml -f docker-compose.prod.yml --profile production up -d

# Access the service through Traefik
# Service: http://youtube-mcp.localhost
# Traefik Dashboard: http://localhost:8080
```

## Tools Available

### `get_youtube_transcript`
Extract transcript text from a YouTube video.

### `extract_video_id_from_url`
Extract the video ID from various YouTube URL formats.


## Development

```bash
# Add new dependencies
uv add package-name

# Run in development mode
uv run server.py
```
