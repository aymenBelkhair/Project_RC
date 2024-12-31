#!/usr/bin/python
# -*- coding: latin-1 -*-
from stqdm import stqdm
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
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

os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-58a5ff02-897c-4ce7-9d48-e5e61c50979b"
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-738a045a-a514-48fd-8569-857cc9e811a0"
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"

@observe()
def GenAi(text,pages,message,chunks,questions_extract,question_pdf,questions_gpt):

      llm = ChatGoogleGenerativeAI(
          model="gemini-1.5-pro",google_api_key = "AIzaSyBgmAi-n-DuQXrUfEppS04PW6Fo0bbU30Q",
          temperature=0,
          max_tokens=None,
          timeout=None,
          max_retries=2
      )
      print("successful llm definition")
      embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key = "AIzaSyBgmAi-n-DuQXrUfEppS04PW6Fo0bbU30Q")
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
      secret_key="sk-lf-58a5ff02-897c-4ce7-9d48-e5e61c50979b",
      public_key="pk-lf-738a045a-a514-48fd-8569-857cc9e811a0",
      host="https://cloud.langfuse.com",
      enabled=True,
              )
              
      # Get Langchain Callback Handler scoped to the current trace context
      langfuse_handler = langfuse_context.get_current_langchain_handler()
      print("start answering")
      all_answer =[]
      for quest_extract,quest_pdf,quest_gpt,i in zip(questions_extract,question_pdf,questions_gpt,stqdm(range(len(questions_extract)))) :
              results = vector_store.similarity_search(
                  quest_extract,
                  k=4
              )
              #print(quest_gpt,i)
  
              # pp = ChatPromptTemplate.from_template("{question} the text based \\n\\n {text}")
              pp = ChatPromptTemplate(message)
              chain = pp | llm | StrOutputParser()
              
              # ai_msg = chain.invoke({"question": quest,"text":text},config={"callbacks":[langfuse_handler]})
              ai_msg = chain.invoke({"question": quest_gpt,"text":results},config={"callbacks":[langfuse_handler]})
              time.sleep(35)
              all_answer.append(quest_pdf)
              all_answer.append(f"--> {ai_msg}")
  
  
   
      joined_answer = "\n".join(all_answer)
      return joined_answer  
  
  
      

#joined_answer = langchain_fn()
#print(joined_answer)