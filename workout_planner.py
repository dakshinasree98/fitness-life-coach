from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Load API key from .env
from dotenv import load_dotenv
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

def generate_workout_plan(weight, gender, workout_type):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=gemini_api_key, temperature=0.7)

    prompt = PromptTemplate(
        input_variables=["weight", "gender", "workout_type"],
        template="Generate a 2-week workout plan for a {gender} weighing {weight} kg who wants to do {workout_type}. Include rest days."
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(weight=weight, gender=gender, workout_type=workout_type)