from fastmcp import FastMCP, Context
from youtube_transcript_api import YouTubeTranscriptApi
import csv
import re
import os

# Get configuration from environment variables
SERVER_NAME = os.getenv("MCP_SERVER_NAME", "YouTube MCP Server")
SERVER_VERSION = os.getenv("MCP_SERVER_VERSION", "0.1.0")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

mcp = FastMCP(
    name=SERVER_NAME,
    version=SERVER_VERSION,
)


@mcp.tool
async def get_youtube_transcript(video_id: str, language: str = "en") -> str:
    """
    Get the transcript of a YouTube video.

    Args:
        video_id (str): The YouTube video ID (e.g., from https://youtube.com/watch?v=VIDEO_ID)
        language (str): The language code for the transcript (default: "en")

    Returns:
        str: The full transcript text
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_id, languages=[language])
        transcript_text = " ".join([entry['text']
                                   for entry in transcript_list])
        return transcript_text
    except Exception as e:
        return f"Error getting transcript: {str(e)}"


@mcp.tool
async def extract_video_id_from_url(url: str) -> str:
    """
    Extract the video ID from a YouTube URL.

    Args:
        url (str): The YouTube URL

    Returns:
        str: The video ID or error message
    """
    # Match various YouTube URL formats
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([^&\n?#]+)',
        r'youtube\.com/watch\?.*v=([^&\n?#]+)'
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return "Could not extract video ID from URL"


def main():
    """Main entry point for the MCP server."""
    mcp.run(
        transport="http",
        host=HOST,
        port=PORT
    )


if __name__ == "__main__":
    main()
