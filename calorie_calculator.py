from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Load API key from .env
from dotenv import load_dotenv
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

def calculate_calorie_intake(weight, gender, workout_type):
    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=gemini_api_key, temperature=0.7)

    prompt = PromptTemplate(
        input_variables=["weight", "gender", "workout_type"],
        template="Estimate the daily calorie intake for a {gender} weighing {weight} kg who wants to do {workout_type}. Provide a single number as the output."
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(weight=weight, gender=gender, workout_type=workout_type)
    
    # Extract the numeric value from the response
    try:
        calorie_intake = int(response.strip())
    except ValueError:
        calorie_intake = 2000  # Default value if parsing fails
    return calorie_intake