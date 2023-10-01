from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

from search import search_faq, search_talks, call_the_right_function


def init_page():
    """Write the basic skeleton of the page"""
    top_container = st.container()
    with top_container:
        col1, col2, col3 = st.columns(spec=[1, 3, 1], gap="large")

        with col1:
            st.image("./resources/devoxx.png")
        with col2:
            search_input = st.text_input(label=":magnifier:",
                                         label_visibility="collapsed",
                                         placeholder="Enter your question here")
        with col3:
            st.write("Home | Sponsors | Content")

    return search_input


def show_results(question: str = None):
    # answer_1 = search_faq(question=question)
    # answer_2 = search_talks(question=question)
    #
    # st.write(search_input)
    # st.subheader("Answers from FAQ")
    # st.write(answer_1)
    # st.subheader("Answers from Talks")
    # st.write(answer_2)

    # TODO: Comment the top of this function and remove the comment from the code below. Fix the error.
    # TODO: You can use this part of the docs
    # TODO https://python.langchain.com/docs/modules/chains/how_to/openai_functions

    answer = call_the_right_function(question=question)
    st.write(f"Called function: {answer['name']}")
    st.divider()

    if answer['name'] == 'search_talks':
        show_search_talks(answer['response'])
    elif answer['name'] == 'search_faq':
        show_search_faq(answer['response'])


def show_search_talks(talks: list):
    for document, score in talks:
        st.write("Talk title: ")
        st.subheader(document.page_content)
        st.write("Speaker(s)")
        speaker = document.metadata["speakers"].replace("#", " - ")
        st.markdown(f":rainbow[{speaker}]")
        times = document.metadata["talk_times"].split("#")
        start = datetime.strptime(times[0], "%Y-%m-%dT%H:%M:%S%z")
        end = datetime.strptime(times[1], "%Y-%m-%dT%H:%M:%S%z")
        st.markdown(f"Time: *{start.strftime('%A %H:%M')} - {end.strftime('%H:%M')}*")
        st.write("Score: ", score)
        st.divider()


def show_search_faq(answer_result:dict):
    st.markdown(f'''
    :gray[The LLM has generated the following answer to your question.]        
    ''')
    st.subheader(answer_result['result'])
    st.divider()
    st.markdown(f'''
    :gray[The following results were used to generate the answer]
    ''')
    for source in answer_result['source_documents']:
        st.write(source.page_content)
        st.write("-----")


if __name__ == '__main__':
    load_dotenv()

    st.set_page_config(page_title="Devoxx",
                       page_icon="./resources/favicon.jpg",
                       layout="wide",
                       initial_sidebar_state="auto",
                       menu_items=None)

    search_input = init_page()

    if search_input:
        show_results(question=search_input)
    else:
        st.write("Welcome to the website of Devoxx 2023. If you want to know more, use the search "
                 "at the top of the page.")
