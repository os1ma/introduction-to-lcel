from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()


prompt = PromptTemplate.from_template(
    """料理のレシピを考えてください。

料理名: {dish}"""
)

model = ChatOpenAI(model_name="gpt-3.5-turbo-1106", temperature=0)

chain = prompt | model | StrOutputParser()

result = chain.invoke({"dish": "カレー"})
print(type(result))
print(result)
