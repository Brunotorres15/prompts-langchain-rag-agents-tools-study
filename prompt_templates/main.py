from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
    temperature=0.7
)

template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)

# PART 1
print("-----Prompt from Template-----")
prompt = prompt_template.invoke({"topic": "dogs"})
result = llm.invoke(prompt)
print(result)



# PART 2: Prompt with System and Human Messages (Using Tuples)
# messages = [
#     ("system", "you are a comedian who tells jokes about {topic}"),
#     ("human", "Tell me {joke_count} jokes")
# ]

# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "dogs", "joke_count": 3})
# print("-----Prompt with System and Human Messages-----")
# print(prompt)
