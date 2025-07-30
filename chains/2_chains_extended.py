from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables from .env
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedia who tells jokes about {topic}"),
        ("human", "tell me {joke_count} jokes")
    ]
)

uppercase_output = RunnableLambda(lambda x: x.upper())

# Create the combined chain using LangChain Expression Language
chain = prompt_template | model | StrOutputParser() | uppercase_output

# Run the chain
result = chain.invoke({"topic": "developers", "joke_count": 1})

# Output
print(result)