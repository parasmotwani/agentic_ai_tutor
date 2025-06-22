import re
from typing import Optional
from services.gemini_client import get_gemini_response


class MathAgent:
    def __init__(self):
        self.calc_keywords = [
            'calculate', 'compute', 'evaluate', 'solve', 'what is',
            'add', 'subtract', 'multiply', 'divide', 'sum', 'product',
            'plus', 'minus', 'times', 'divided by'
        ]
    
    async def answer_question(self, question: str) -> str:
        return await self._handle_math_with_gemini(question)
    
    async def _handle_math_with_gemini(self, question: str) -> str:
        try:
            prompt = f"""
            You are a math tutor. Answer this math question clearly and concisely:
            {question}
            
            If it's a calculation, show the steps and provide the final answer.
            If it's a concept, explain it simply.
            Be helpful and educational in your response.
            """
            
            response = await get_gemini_response(prompt)
            return response
            
        except Exception as e:
            return f"Sorry, I encountered an error while processing your math question: {str(e)}"

if __name__ == "__main__":
    math_agent = MathAgent()