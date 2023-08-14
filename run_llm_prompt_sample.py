from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub
from langchain.llms import OpenAI


def initialize_huggingface_llm(prompt: PromptTemplate, temperature: float, max_length: int) -> LLMChain:
    repo_id = "google/flan-t5-xxl"

    # Experiment with the max_length parameter and temperature
    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": temperature, "max_length": max_length}
    )
    return LLMChain(prompt=prompt, llm=llm)


def initialize_openai_llm(prompt: PromptTemplate, temperature: float, max_length: int) -> LLMChain:
    llm = OpenAI(model_name="text-davinci-003", temperature=temperature, max_tokens=max_length)
    return LLMChain(prompt=prompt, llm=llm)


def generate_prompt() -> PromptTemplate:
    # You can play around with the prompt, see the results change if you make small changes to the prompt
    template = """Given the name of the country, give the languages that are spoken in that country. 
    Start with the official languages of the country and continue with the other languages of that country.
    Country: {country}?
    Languages: 
    """

    return PromptTemplate(template=template, input_variables=["country"])


if __name__ == '__main__':
    load_dotenv()

    # Try other values to see impact on results
    country = "belgium"
    country_max_length = 100
    country_temperature = 0.1

    country_prompt = generate_prompt()

    hugging_chain = initialize_huggingface_llm(prompt=country_prompt,
                                               temperature=country_temperature,
                                               max_length=country_max_length)
    print("HuggingFace")
    print(hugging_chain.run(country))

    openai_chain = initialize_openai_llm(prompt=country_prompt,
                                         temperature=country_temperature,
                                         max_length=country_max_length)
    print("\nOpenAI")
    print(openai_chain.run(country))
