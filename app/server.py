from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from fastapi import FastAPI
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

summarization_assistant_template = """
You are a text summarization bot. Your expertise is exclusively in analyzing and summarizing user-provided texts. 
Create a concise and comprehensive summary of the provided text, retaining all crucial information in a 
shorter form. Text for Summarization: {text_for_summarization}"""

summarization_assistant_prompt = PromptTemplate(
    input_variables=["text_for_summarization"],
    template=summarization_assistant_template
)

llm = OpenAI(model='gpt-3.5-turbo-instruct',
             temperature=0.5)
llm_chain = summarization_assistant_prompt | llm

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Summarization App",
)

add_routes(
    app,
    llm_chain,
    path="/openai"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
