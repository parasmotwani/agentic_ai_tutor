"""
gemini_client.py
Async client for sending prompts to the Gemini API and returning responses.
"""

import os
import aiohttp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class GeminiClient:
    """Async client for interacting with Google's Gemini API."""
    
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/"
        self.model = "gemini-1.5-flash"   # <-- Just ONE model
    
    async def get_response(self, prompt: str) -> str:
        """
        Send a prompt to Gemini API and return the response.
        """
        url = f"{self.base_url}{self.model}:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    try:
                        return result["candidates"][0]["content"]["parts"][0]["text"]
                    except Exception:
                        return "[Gemini API: No valid response]"
                else:
                    return f"[Gemini API error: {resp.status}]"

# Global client instance
_gemini_client = None

def get_gemini_client() -> GeminiClient:
    """Get or create a global Gemini client instance."""
    global _gemini_client
    if _gemini_client is None:
        _gemini_client = GeminiClient()
    return _gemini_client

async def get_gemini_response(prompt: str) -> str:
    """
    Convenience function to get a response from Gemini API.
    
    Args:
        prompt: The input prompt
        
    Returns:
        Generated response text
    """
    try:
        client = get_gemini_client()
        response = await client.get_response(prompt)
        
        if response is None:
            return "Sorry, I couldn't generate a response at this time."
        
        return response
    except Exception as e:
        print(f"Error in get_gemini_response: {e}")
        return "Sorry, I'm having trouble processing your request right now."

if __name__ == "__main__":
    import asyncio
    
    async def test_gemini():
        """Test the Gemini client."""
        try:
            test_prompt = "What is 2 + 2? Please provide a simple answer."
            response = await get_gemini_response(test_prompt)
            print(f"Prompt: {test_prompt}")
            print(f"Response: {response}")
        except Exception as e:
            print(f"Test failed: {e}")
    
    # Run the test
    asyncio.run(test_gemini()) 