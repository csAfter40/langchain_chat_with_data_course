import sys
import os
import openai
from dotenv import load_dotenv, find_dotenv

# # pdf
# from langchain_community.document_loaders import PyPDFLoader
# load_dotenv(find_dotenv())
# openai.api_key = os.environ['OPENAI_API_KEY']
# pdf_loader = PyPDFLoader("./documents/pool_doc.pdf")
# document = pdf_loader.load()
# page = document[1]
# print(page.metadata)

# # youtube audio
# from langchain_community.document_loaders.generic import GenericLoader
# from langchain_community.document_loaders.parsers import OpenAIWhisperParser
# from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
# url = "https://www.youtube.com/watch?v=DBHCXD3SS8U"
# save_dir = "./temp/"
# yt_loader = GenericLoader(YoutubeAudioLoader([url], save_dir), OpenAIWhisperParser())
# yt_docs = yt_loader.load()
# print(yt_docs[0].page_content)


# web
from langchain_community.document_loaders import WebBaseLoader
web_loader = WebBaseLoader("https://askthepoolguy.com/pool-encyclopedia/")
web_docs = web_loader.load()
breakpoint()