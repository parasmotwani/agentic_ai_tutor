import re
from typing import Optional
from tools.physics_constants import get_physics_constant
from services.gemini_client import get_gemini_response

class PhysicsAgent:
    def __init__(self):
        self.constant_keywords = [
            'constant', 'value of', 'what is the value', 'planck', 'boltzmann',
            'avogadro', 'gravitational', 'coulomb', 'elementary charge',
            'electron mass', 'proton mass', 'neutron mass', 'speed of light',
            'universal gas', 'faraday', 'permittivity', 'permeability'
        ]
        self.constant_names = [
            'planck constant', 'boltzmann constant', 'avogadro number',
            'gravitational constant', 'coulomb constant', 'elementary charge',
            'electron mass', 'proton mass', 'neutron mass', 'speed of light',
            'universal gas constant', 'faraday constant', 'vacuum permittivity',
            'vacuum permeability', 'fine structure constant', 'bohr radius'
        ]
    async def answer_question(self, question: str) -> str:
        if self._is_constant_request(question):
            constant_name = self._extract_constant_name(question)
            if constant_name:
                return self._handle_constant_request(constant_name)
        return await self._handle_complex_physics(question)
    def _is_constant_request(self, question: str) -> bool:
        question_lower = question.lower()
        has_constant_keywords = any(keyword in question_lower for keyword in self.constant_keywords)
        has_constant_names = any(constant in question_lower for constant in self.constant_names)
        return has_constant_keywords or has_constant_names
    def _extract_constant_name(self, question: str) -> Optional[str]:
        question_lower = question.lower()
        for constant in self.constant_names:
            if constant in question_lower:
                return constant
        patterns = [
            r'what\s+is\s+the\s+value\s+of\s+([a-zA-Z\s]+)',
            r'value\s+of\s+([a-zA-Z\s]+)',
            r'constant\s+([a-zA-Z\s]+)',
            r'([a-zA-Z\s]+)\s+constant'
        ]
        for pattern in patterns:
            match = re.search(pattern, question_lower)
            if match:
                constant_name = match.group(1).strip()
                mapped_name = self._map_constant_name(constant_name)
                if mapped_name:
                    return mapped_name
        return None
    def _map_constant_name(self, name: str) -> Optional[str]:
        name_mapping = {
            'planck': 'planck constant',
            'boltzmann': 'boltzmann constant',
            'avogadro': 'avogadro number',
            'gravitational': 'gravitational constant',
            'coulomb': 'coulomb constant',
            'elementary charge': 'elementary charge',
            'electron': 'electron mass',
            'proton': 'proton mass',
            'neutron': 'neutron mass',
            'speed of light': 'speed of light',
            'universal gas': 'universal gas constant',
            'faraday': 'faraday constant',
            'vacuum permittivity': 'vacuum permittivity',
            'vacuum permeability': 'vacuum permeability',
            'fine structure': 'fine structure constant',
            'bohr radius': 'bohr radius'
        }
        for key, value in name_mapping.items():
            if key in name:
                return value
        return None
    def _handle_constant_request(self, constant_name: str) -> str:
        try:
            constant_info = get_physics_constant(constant_name)
            if constant_info:
                return f"The {constant_name} is {constant_info['value']} {constant_info['unit']}. {constant_info.get('description', '')}"
            else:
                return f"Sorry, I don't have information about the {constant_name}."
        except Exception as e:
            return f"Sorry, I encountered an error while looking up the {constant_name}: {str(e)}"
    async def _handle_complex_physics(self, question: str) -> str:
        try:
            prompt = f"""
            You are a physics tutor. Answer this physics question clearly and concisely:
            {question}
            If it's a calculation, show the steps. If it's a concept, explain it simply.
            Focus on the fundamental principles and provide accurate information.
            """
            response = await get_gemini_response(prompt)
            return response
        except Exception as e:
            return f"Sorry, I encountered an error while processing your physics question: {str(e)}" 