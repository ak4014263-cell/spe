import os
from openai import AsyncOpenAI
from django.conf import settings

class ChatAIHandler:
    def __init__(self):
        # Initialize the async OpenAI client
        api_key = os.getenv('OPENAI_API_KEY', settings.OPENAI_API_KEY if hasattr(settings, 'OPENAI_API_KEY') else None)
        self.client = AsyncOpenAI(api_key=api_key) if api_key else None
        
    async def get_ai_response(self, message, context=None):
        import asyncio
        try:
            if not self.client:
                return "Sorry, the AI service is not configured correctly. An agent will assist you shortly."

            # System prompt
            system_message = {
                "role": "system",
                "content": (
                    "You are a friendly and professional assistant for Speedy Transfer, "
                    "a private transportation service in Puerto Vallarta.\n"
                    "IMPORTANT: Always respond in English only, regardless of the language the customer uses. "
                    "If the customer writes in Spanish or any other language, respond in English and acknowledge "
                    "their message. Provide brief, accurate, and helpful responses. Be courteous and professional at all times."
                )
            }

            # Prepare conversation history (context is a list of dicts)
            messages = [system_message]
            if context:
                messages.extend(context)
            messages.append({"role": "user", "content": message})

            # Limit to last 10 messages for performance
            messages = messages[:1] + messages[-10:]

            # Timeout for OpenAI call (e.g., 15 seconds)
            async def call_openai():
                return await self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=150,
                    temperature=0.7,
                    presence_penalty=0
                )
            try:
                response = await asyncio.wait_for(call_openai(), timeout=15)
            except asyncio.TimeoutError:
                return "Sorry, the AI service is taking too long to respond. Please try again later."

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Error in AI response generation: {str(e)}")
            return "Sorry, there's a technical issue. An agent will assist you shortly."