import os

from utils.document_parser import extract_text
from utils.processor import clean_text, chunk_text
from utils.entity_extractor import extract_entities
from utils.document_classifier import classify_document


def ingest_documents(files):

    all_chunks = []

    chunk_id = 0

    for file_path in files:

        # ----------------------------
        # Document Metadata
        # ----------------------------
        document_name = os.path.basename(file_path)

        document_type = document_name.split(".")[-1].lower()

        # ----------------------------
        # Extract Text
        # ----------------------------
        text = extract_text(file_path)

        # ----------------------------
        # Clean Text
        # ----------------------------
        text = clean_text(text)


        document_category = classify_document(text)

        # ----------------------------
        # Create Chunks
        # ----------------------------
        chunks = chunk_text(text)

        # ----------------------------
        # Store Chunk Metadata
        # ----------------------------
        for chunk in chunks:

            entities = extract_entities(chunk["text"])

            all_chunks.append({

                "chunk_id": chunk_id,

                "document_name": document_name,

                "document_type": document_type,

                "document_category": document_category,

                "page": chunk["page"],

                "title": chunk["title"],

                "text": chunk["text"],

                "entities": entities

            })

            chunk_id += 1

            

    return all_chunks