from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
 
def read_text(file_path):
    
    loader = PyPDFLoader(file_path,extract_images=True)
    pages = []
    text = ''
    i=0
    pattern = re.compile(r'SOMMAIRE|[.]{7,}', re.IGNORECASE)
    for page in loader.load():
      if pattern.search(page.page_content):
          pass
          i+=1
      else:
          pages.append(page)
          i+=1
    
    for i in range(len(pages)):
        text += pages[i].page_content.replace("\n", "")
        
    return text.lower(),pages
    
def text_to_chunks(text):   
        text_splitter = RecursiveCharacterTextSplitter(chunk_size= 400, chunk_overlap = 20)
        chunks = text_splitter.split_text(text)
        return chunks


def pdf(file_path):
      text,pages = read_text(file_path)
      chunks = text_to_chunks(text)
      return chunks,text,pages
      
# Execute the coroutine
if __name__ == "__main__":
    pdf()


