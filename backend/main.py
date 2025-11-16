import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from tools import get_reddit_comments
from system_prompt import system_prompt

app = FastAPI()

# -------------------- Models --------------------
class AgentResponse(BaseModel):
    """Summary of Reddit comments."""
    summary: str
    sources: list[str]

class SummarizerRequest(BaseModel):
    url: str
# -------------------------------------------------

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/summarize")
def summarize_comments(request: SummarizerRequest):
    url = request.url

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    tools = [get_reddit_comments]

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
        response_format=AgentResponse
    )

    try:
        result = agent.invoke({
            "messages": [
                {"role": "user", 
                 "content": url}
            ]
        })

        print(">> Fetching LLM agent response")

        #print(result["structured_response"])
        summary = result["structured_response"].summary

    except Exception as e:
        print(f">> Error running LLM agent: {e}")
        summary = "Sorry, unable to generate a summary for this discussion."

    return AgentResponse(summary=summary, sources=[])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)