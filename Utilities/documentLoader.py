from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document

import os
import shutil


data_path = "Data"

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    chunks = text_splitter(documents)
    ##save_chunks(chunks)

def load_documents():
    loader = DirectoryLoader(data_path,glob="*.pdf")
    return loader.load()

def text_splitter(documents : list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)

    print(f"Split {len(documents)} documents into {len(chunks)} chunks")

    documents = chunks[10]
    print(documents.page_content)
    print(documents.metadata)
    return chunks



