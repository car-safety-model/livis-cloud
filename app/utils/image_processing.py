from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

def extract_text(image_url):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY")
    )

    message = HumanMessage(
        content=[
            {"type": "text", "text": "identify the road sign in the image notify the user with the message"},
            {
                "type": "image_url",
                "image_url": image_url,
            },
        ]
    )
    ai_msg = llm.invoke([message])

    return ai_msg.content
