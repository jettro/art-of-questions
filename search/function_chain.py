import os

from langchain.chains.openai_functions import create_openai_fn_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from search import search_faq, search_talks


def init_fn_chain():
    llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=os.getenv('OPEN_AI_API_KEY'))
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a system to search for answers on a provided question."),
            ("human", "Make calls to the relevant function to using the following input: {input}"),
            ("human", "Tip: Make sure to answer in the correct format"),
        ]
    )

    return create_openai_fn_chain(
        functions=[search_faq, search_talks],
        llm=llm,
        prompt=prompt,
        verbose=True
    )


def call_the_right_function(question: str):
    chain = init_fn_chain()

    functions_map = {
        'search_faq': search_faq,
        'search_talks': search_talks
    }

    chain_response = chain.run(question)
    print(f"The response of the chain is {chain_response}")
    function_name = chain_response["name"]
    args = chain_response["arguments"]

    if function_name not in functions_map:
        chain_response["response"] = f"Could not decide which content search to perform for name '{function_name}'"
    else:
        chain_response["response"] = functions_map[function_name](**args)

    return chain_response
