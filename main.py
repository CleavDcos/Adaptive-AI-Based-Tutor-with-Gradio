import os
import gradio as gr
from openai import OpenAI   
from dotenv import load_dotenv

#load env variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key loaded successfully")

openai_client = OpenAI(api_key=openai_api_key)
print("OpenAI client configured")

#Create the main function which will behvave as the tutor
#Using openAI api
def get_ai_tutor_response(user_question):
    """
    Sends a question to the OpenAI API, asking it to respond as an AI Tutor.

    Args:
        user_question (str): The question asked by the user.

    Returns:
        str: The AI's response, or an error message.
    """
    system_prompt = "You are a helpful and patient AI Tutor. Explain the concepts clearly and concisely"

    try:
        #make api call
        response = openai_client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role":"system", "content":system_prompt},
                {"role":"user", "content":user_question}
            ],
            temperature=0.7,#this is randomness allowing some creativity for ai
        )
        #extact the response 
        ai_response = response.choices[0].message.content.strip()
        return ai_response
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return "Sorry, I couldn't process your question at the moment. Please try again later."
    
#test_question = "explain concept of gravity"
#print(f"asking test question: {test_question}  ")
#test_response = get_ai_tutor_response(test_question)
#print(f"AI Tutor response: {test_response}")


#Build interface using Gradio
#gr.Interface(fn=get_ai_tutor_response, inputs="text", outputs="text", title="Adaptive AI Tutor").launch()
ai_tutor_interface_simple = gr.Interface(
fn=get_ai_tutor_response,
inputs=gr.Textbox(lines=2,placeholder="Ask the AI Tutor Anything!", label ="Your Question"),
outputs=gr.Textbox(label="AI Tutor Response"),
title = "Simple AI Tutor",
description = "Ask the AI Tutor any question and get a clear and concise response!"
)

print("Launching Gradio interface...")
ai_tutor_interface_simple.launch()