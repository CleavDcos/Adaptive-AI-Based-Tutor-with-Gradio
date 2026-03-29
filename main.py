import os
import gradio as gr
from openai import OpenAI   
from dotenv import load_dotenv


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key loaded successfully")

openai_client = OpenAI(api_key=openai_api_key)
print("OpenAI client configured")