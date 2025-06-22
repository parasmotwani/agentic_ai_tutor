import re
from typing import Optional
from services.gemini_client import get_gemini_response
from agents.math_agent import MathAgent
from agents.physics_agent import PhysicsAgent


class TutorAgent:
    
    def __init__(self):
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()
    
    async def answer_question(self, question: str) -> str:
        subject = await self._classify_with_gemini(question)
        
        if subject == 'math':
            return await self.math_agent.answer_question(question)
        elif subject == 'physics':
            return await self.physics_agent.answer_question(question)
        else:
            return self._handle_general_question(question)
    
    async def _classify_with_gemini(self, question: str) -> str:
        try:
            prompt = f"""
            Analyze this question and classify it into one of these categories:
            - 'math': Questions about mathematics, calculations, equations, algebra, geometry, calculus, statistics, etc.
            - 'physics': Questions about physics concepts, forces, energy, motion, constants, particles, etc.
            - 'general': Any other type of question
            
            Question: {question}
            
            Respond with only: math, physics, or general
            """
            
            response = await get_gemini_response(prompt)
            response = response.strip().lower()
            
            if response in ['math', 'physics', 'general']:
                return response
            return 'general'
            
        except Exception as e:
            print(f"Error classifying with Gemini: {e}")
            return 'general'
    
    def _handle_general_question(self, question: str) -> str:
        return f"I'm sorry, but I'm specifically designed to help with math and physics questions. Your question '{question}' doesn't seem to be related to math or physics. Please try asking questions like:\n\n• What is 2 + 3?\n• What is Planck's constant?\n• Calculate 15 * 7\n• What is the speed of light?\n• Explain quantum mechanics\n• Solve the equation x² + 5x + 6 = 0" 