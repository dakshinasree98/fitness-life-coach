from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
import os

# Load API key from .env
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def provide_life_advice(goal):
    llm = OpenAI(api_key=openai_api_key, temperature=0.7)

    prompt = PromptTemplate(
        input_variables=["goal"],
        template="Provide motivational advice and a step-by-step plan to achieve this goal: {goal}."
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(goal=goal)