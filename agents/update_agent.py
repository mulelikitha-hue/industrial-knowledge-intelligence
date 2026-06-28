from utils.embeddings import create_embeddings
from utils.entity_extractor import extract_entities
import time


class UpdateAgent:

    def __init__(self, kg, vector_store):

        self.kg = kg
        self.vector_store = vector_store

    def update_knowledge(self, update_text):

        

        # -----------------------------------
        # Extract Entities
        # -----------------------------------

        entities = extract_entities(update_text)

        # -----------------------------------
        # Create Knowledge Chunk
        # -----------------------------------

        document_name = f"Engineer_Update_{int(time.time())}"

        chunk = {

            "chunk_id": len(self.vector_store.chunk_metadata),

            "document_name": document_name,

            "document_type": "feedback",

            "document_category": "user_update",

            "updated_by": "Engineer",

            "source": "Point of Need Update",

            "page": 1,

            "title": "Knowledge Update",

            "text": update_text,

            "entities": entities

        }

        # -----------------------------------
        # Generate Embedding
        # -----------------------------------

        embedding = create_embeddings(
            [update_text]
        )

        # -----------------------------------
        # Update Vector Store
        # -----------------------------------

        self.vector_store.add_documents(

            embedding,

            [chunk]

        )

        # -----------------------------------
        # Update Knowledge Graph
        # -----------------------------------

        self.kg.add_chunk(chunk)

        return True