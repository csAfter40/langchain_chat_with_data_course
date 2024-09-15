import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]
pdf_loader = PyPDFLoader("./documents/pool_doc.pdf")
document = pdf_loader.load()
page = document[1]
print(page.metadata)
