#!/usr/bin/python
# -*- coding: latin-1 -*-
from stqdm import stqdm
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import pypdf
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
import time
import os
from langfuse.decorators import langfuse_context
from tqdm import tqdm
from langchain.schema import StrOutputParser
from langfuse.decorators import observe
from langchain.prompts import ChatPromptTemplate
from langfuse.decorators import observe, langfuse_context
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from datetime import datetime
import streamlit as st
os.environ["LANGFUSE_SECRET_KEY"] = #key
os.environ["LANGFUSE_PUBLIC_KEY"] = #key
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"

KEY_OPENAI = os.getenv('KEY_OPENAI')
# Get the current date and time
now = datetime.now()

# Format it as a string
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

@observe()
def GenAi(text,pages,message,chunks,questions_extract,question_pdf,questions_gpt):
      print("-----------------------")
      print(f"----{formatted_date_time}----")
      print("-----------------------")
      
      llm = ChatOpenAI(model="gpt-4",api_key = KEY_OPENAI)
      print("successful llm definition")
      embeddings = OpenAIEmbeddings(model="text-embedding-3-large",api_key = KEY_OPENAI)
      vector_store = FAISS.from_texts(chunks, embedding = embeddings)
      vector_store.save_local("faiss_index")
      print("successful vectore store and embedding creation")
      index = faiss.IndexFlatL2(len(embeddings.embed_query(text)))
      vector_store = FAISS(
          embedding_function=embeddings,
          index=index,
          docstore=InMemoryDocstore(),
          index_to_docstore_id={},
      )
      
      documents =[page for page in pages]
      ids = [i for i in range(len(pages))]
      vector_store.add_documents(documents=documents, ids=ids)
      # Configure the Langfuse client
      
              
      
      
      langfuse_context.configure(
      secret_key=#key,
      public_key=#key,
      host="https://cloud.langfuse.com",
      enabled=True,
              )
              
      # Get Langchain Callback Handler scoped to the current trace context
      langfuse_handler = langfuse_context.get_current_langchain_handler()
      print("start answering")
      all_answer =[]
      dc={}
      for quest_extract,quest_pdf,quest_gpt,i in zip(questions_extract,question_pdf,questions_gpt,stqdm(range(len(questions_extract)))) :
              results = vector_store.similarity_search(
                  quest_extract.lower(),
                  k=2
              )
              
  
              
              pp = ChatPromptTemplate(message)
              chain = pp | llm | StrOutputParser()
              
              resul = results[0].page_content+'//n'+results[1].page_content #+'//n'+results[2].page_content
              ai_msg = chain.invoke({"question": quest_gpt,"text": resul},config={"callbacks":[langfuse_handler]})
              split_items = quest_pdf.split("<>")
              if len(split_items) > 1 and split_items[1] != '':
                  dc[quest_pdf.split("<>")[1]]=ai_msg
              all_answer.append(quest_pdf.split("<>")[0])
              all_answer.append(f"--> {ai_msg}")
              
              
              
              
  
   
      joined_answer = "\n".join(all_answer)
      return joined_answer,dc
  
  
      
