from search.langchain_components import __init_langchain_vector_store


def search_talks(question: str) -> list:
    """
    Uses the question to find talks using the titles of the talks

    Args:
        question: The question asked by the user to find talks for
    """
    vector_store = __init_langchain_vector_store(index_name="DevoxxTalk",
                                                 attributes=["speakers", "talk_times"])
    response = vector_store.similarity_search_with_score(query=question)
    return response
