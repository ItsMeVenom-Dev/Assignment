import os
import re
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json 

with open("json_input.json","r") as file:
    json_prompt=json.load(file)


load_dotenv()

groq_api = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=groq_api
)

valid_classes = []
for category in json_prompt.values():
    for value in category.values():
        valid_classes.extend(value.split())

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are the coding ai assistant named Blot.
Your work is to take the user prompt and produce clean Angular code strictly follow the predefined design system.

json_prompt: {json_prompt}
valid_classes: {valid_classes}

Rules:
Use ONLY classes present in valid_classes.
Do NOT invent new classes.
Return raw HTML only.
Do not use markdown backticks.
"""
        ),
        ("user", "{input}")
    ]
)

output = StrOutputParser()
generator_chain = prompt | llm | output

validator_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are code checking AI.

Valid_Class: {valid_classes}

Rules:
If ALL used classes are inside valid_classes output exactly:
VALID

Otherwise output:
INVALID
Invalid classes: [list]
Syntax errors: [None or describe]
Correction Prompt:
Write instruction to fix using only Valid_Class list.

Do NOT fix code.
Only validate.
"""
        ),
        ("user", "Here is generated HTML:\n{generated_code}")
    ]
)

validator_chain = validator_prompt | llm | output


# 🔥 Extract only content inside ``` ```
def extract_html(text):
    start = text.find("```")
    if start == -1:
        return text.strip()

    end = text.find("```", start + 3)
    if end == -1:
        return text.strip()

    code_block = text[start + 3:end].strip()

    if code_block.startswith("html"):
        code_block = code_block[4:].strip()

    return code_block


def extract_correction_prompt(validation_text):
    match = re.search(r"Correction Prompt:\s*(.*)", validation_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


st.title("ASSIGNMENT")

user_input = st.text_area("Enter your prompt")

if st.button("Generate"):

    generated_code = generator_chain.invoke({
        "input": user_input,
        "json_prompt": json_prompt,
        "valid_classes": valid_classes
    })

    validator_output = validator_chain.invoke({
        "generated_code": generated_code,
        "valid_classes": valid_classes
    })

    if validator_output.startswith("VALID"):
        final_code = generated_code
    else:
        correction_prompt = extract_correction_prompt(validator_output)

        fixed_code = generator_chain.invoke({
            "input": correction_prompt,
            "json_prompt": json_prompt,
            "valid_classes": valid_classes
        })

        final_code = extract_html(fixed_code)

    st.code(final_code, language="html")

if st.button("Save Input"):
    if user_input.strip():
        st.download_button(
            label="Download TSX File",
            data=user_input,
            file_name="code.tsx",
            mime="text/plain"
        )
