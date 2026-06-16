import os
import json 
import pandas as pd
from dotenv import load_dotenv
from .utils import read_file, get_table_data
from .logger import logging

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
OPENAI_KEY=os.getenv("OPENAI_KEY")

llm = ChatOpenAI(api_key=OPENAI_KEY, model_name="gpt-3.5-turbo", temperature=0.7)

quiz_generation_prompt = ChatPromptTemplate.from_template(
    """You are an expert MCQ maker. Given the above text, it is your job to
    create quiz of {number} multiple choice questions for {subject} students in {tone} tone. Make sure the questions are not repeated and check all the questions to be conforming the text as well. Make sure to format your response like RESPONSE JSON below and use it as a guide. 
    Ensure to make {number} MCQs
    ### RESPONSE_JSON
    {response_json}"""
)

quiz_chain = quiz_generation_prompt | llm | StrOutputParser()

quiz_evaluation_prompt = ChatPromptTemplate.from_template(
    """You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
    You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
    if the quiz is not at per with the cognitive and analytical abilities of the students,\
    update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
    Quiz_MCQs:
    {quiz}

    Check from an expert English Writer of the above quiz:"""
)

quiz_review_chain = quiz_evaluation_prompt | llm | StrOutputParser()

generate_evaluation_chain = (
    RunnablePassthrough.assign(
        quiz=quiz_chain
    ).assign(
        review=quiz_review_chain
    )
)