from search.langchain_components import __init_rag_chain


def search_faq(question: str) -> dict:
    """
    Uses the question to obtain an answer to FAQ related questions

    Args:
        question: The question asked by the user to answer using relevant parts of the FAQ
    """
    question_answer_chain = __init_rag_chain(index_name="DevoxxFAQ")
    response = question_answer_chain({"query": question})
    return response
