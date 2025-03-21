from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Load API key from .env
from dotenv import load_dotenv
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

def provide_life_advice(goal):
    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=gemini_api_key, temperature=0.7)

    prompt = PromptTemplate(
        input_variables=["goal"],
        template="Provide motivational advice and a step-by-step plan to achieve this goal: {goal}."
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(goal=goal)