import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import WebBaseLoader

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]
web_loader = WebBaseLoader("https://askthepoolguy.com/pool-encyclopedia/")
web_docs = web_loader.load()
breakpoint()
