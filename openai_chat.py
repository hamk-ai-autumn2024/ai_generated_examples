import os
from openai import OpenAI
from typing import List, Dict, Optional
import sys

# Constants
DEFAULT_MODEL = "openai/gpt-5-mini"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_SYSTEM_PROMPT = ""
MAX_TOKENS = 150
EXIT_COMMANDS = {"exit", "quit", "bye", "q"}
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

class ChatBot:
    """Interactive text-based chat using OpenRouter API with streaming responses."""
    
    def __init__(self, model: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE):
        """
        Initialize the ChatBot with OpenRouter configuration.
        
        Args:
            model (str): The model to use (e.g., "openai/gpt-4o-mini", "anthropic/claude-3-sonnet")
            temperature (float): Sampling temperature for responses
        
        Raises:
            ValueError: If API key is not found or invalid configuration
        """
        self.model = model
        self.temperature = temperature
        self.conversation_history: List[Dict[str, str]] = []
        
        # Check for OpenRouter API key
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable is not set")
        
        # Get optional site configuration
        site_url = os.getenv("OPENROUTER_SITE_URL", "")
        site_name = os.getenv("OPENROUTER_SITE_NAME", "ChatBot")
        
        # Initialize OpenRouter client using OpenAI SDK
        try:
            self.client = OpenAI(
                api_key=api_key,
                base_url=OPENROUTER_BASE_URL,
                default_headers={
                    "HTTP-Referer": site_url,
                    "X-Title": site_name,
                }
            )
        except Exception as e:
            raise ValueError(f"Failed to initialize OpenRouter client: {e}")
        
        # Set system prompt
        if DEFAULT_SYSTEM_PROMPT:
            self.conversation_history.append({
                "role": "system",
                "content": DEFAULT_SYSTEM_PROMPT
            })
    
    def stream_response(self, user_message: str) -> Optional[str]:
        """
        Stream a response from OpenRouter for the given user message.
        
        Args:
            user_message (str): The user's input message
            
        Returns:
            Optional[str]: The complete AI response or None if error occurred
        """
        try:
            # Add user message to conversation history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Make streaming API call to OpenRouter
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=self.temperature,
                max_tokens=MAX_TOKENS,
                stream=True
            )
            
            # Collect the complete response while streaming
            complete_response = ""
            
            for chunk in stream:
                # Check if chunk has content
                if (chunk.choices and 
                    len(chunk.choices) > 0 and 
                    chunk.choices[0].delta and 
                    chunk.choices[0].delta.content is not None):
                    content = chunk.choices[0].delta.content
                    complete_response += content
                    # Print content immediately for streaming effect
                    print(content, end="", flush=True)
            
            # Add complete AI response to conversation history
            if complete_response:
                self.conversation_history.append({
                    "role": "assistant",
                    "content": complete_response
                })
            
            return complete_response if complete_response else None
            
        except Exception as e:
            error_msg = str(e).lower()
            if "openrouter" in error_msg or "api" in error_msg:
                print(f"\nOpenRouter API error: {e}")
            else:
                print(f"\nUnexpected error: {e}")
            return None
    
    def start_chat(self) -> None:
        """Start the interactive chat session."""
        print("=" * 60)
        print("Interactive Chat with OpenRouter API (Streaming)")
        print("=" * 60)
        print(f"Model: {self.model}")
        print(f"Temperature: {self.temperature}")
        print("Type 'exit', 'quit', 'bye', or 'q' to end the conversation.")
        print("-" * 60)
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # Check for exit commands
                if user_input.lower() in EXIT_COMMANDS:
                    print("\nGoodbye! Thanks for chatting!")
                    break
                
                # Skip empty inputs
                if not user_input:
                    print("Please enter a message or type 'exit' to quit.")
                    continue
                
                # Get streamed AI response
                print("\nAI: ", end="", flush=True)
                response = self.stream_response(user_input)
                
                if response:
                    # Print newline after streaming is complete
                    print()
                else:
                    print("Sorry, I couldn't process your request. Please try again.")
                    
            except KeyboardInterrupt:
                print("\n\nChat interrupted. Goodbye!")
                break
            except EOFError:
                print("\n\nChat ended. Goodbye!")
                break
            except Exception as e:
                print(f"\nUnexpected error occurred: {e}")
                print("Please try again or type 'exit' to quit.")

def main():
    """Main function to run the chat application."""
    try:
        chatbot = ChatBot()
        chatbot.start_chat()
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please ensure OPENROUTER_API_KEY environment variable is set correctly.")
        print("Optional: Set OPENROUTER_SITE_URL and OPENROUTER_SITE_NAME for better tracking.")
    except Exception as e:
        print(f"Failed to start chat application: {e}")

if __name__ == "__main__":
    main()