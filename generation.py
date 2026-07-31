import re

import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="qwen/qwen3.6-27b", api_key=api_key)

SYSTEM_PROMPT = """You are an expert technical documentation assistant.

Answer the user's question using ONLY the information contained in the retrieved documentation context.

Rules:
1. Do not use outside knowledge.
2. Do not make assumptions.
3. If the context does not contain sufficient information, explicitly state that the answer is not present in the retrieved documentation.
4. Cite relevant document sections when possible.
5. Keep technical terminology accurate.
6. When answering procedural questions, provide step-by-step instructions.
7. When answering API or programming questions, include example code if the context supports it.
8. If multiple sources provide complementary information, synthesize them into a single answer.
9. If multiple question answers are given in context, only answer the asked question from the provided context.
10. You can introduce emojis to make chat more fun.
11. Dont say "Based on retrieved documents", instead answer naturally.
"""

HUMAN_PROMPT = """
Retrieved Documentation:

{context}

---

Question:
{question}

Answer:
"""
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", HUMAN_PROMPT),
])


def build_context(results):
    if not results:
        return "No relevant documentation found."

    contexts = []
    for index, doc in enumerate(results, start=1):
        content = doc.page_content.strip() if hasattr(doc, "page_content") else str(doc)
        if not content:
            content = "(empty chunk)"
        contexts.append(f"[Document {index}]\n{content}")

    return "\n\n".join(contexts)


def generate_answer(query, results):
    context = build_context(results)
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": query})

    content = response.content


    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()

    return content