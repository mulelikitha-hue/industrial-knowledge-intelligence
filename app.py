import os
import streamlit as st

from utils.knowledge_graph import KnowledgeGraph
from utils.document_ingestor import ingest_documents
from utils.embeddings import create_embeddings
from utils.vector_store import VectorStore
from agents.knowledge_analyze import KnowledgeAgent
from agents.maintenance_agent import MaintenanceAgent
from agents.router_agent import RouterAgent
from agents.compliance_agent import ComplianceAgent
from agents.update_agent import UpdateAgent
from agents.lessons_agent import LessonsLearnedAgent


st.set_page_config(page_title="Industrial Knowledge Intelligence", layout="wide")

st.title("🏭 Industrial Knowledge Intelligence Platform")

st.write("Upload one or more industrial documents and ask questions across all of them.")

# =====================================================
# Upload Multiple Documents
# =====================================================

uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["pdf", "docx", "pptx", "csv", "xlsx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:

    os.makedirs("uploads", exist_ok=True)

    saved_files = []

    for uploaded_file in uploaded_files:

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        saved_files.append(file_path)

    st.success(f"{len(saved_files)} document(s) uploaded successfully.")

    # =====================================================
    # Document Ingestion
    # =====================================================

    chunks = ingest_documents(saved_files)

    



    #st.write(chunks[0])

    kg = KnowledgeGraph()

    for chunk in chunks:
        kg.add_chunk(chunk)

    st.subheader("Knowledge Graph Statistics")

    st.write("Total Nodes :", kg.graph.number_of_nodes())

    st.write("Total Edges :", kg.graph.number_of_edges())

    st.write("Total Chunks :", len(chunks))

    texts = [chunk["text"] for chunk in chunks]

    # =====================================================
    # Embeddings
    # =====================================================

    embeddings = create_embeddings(texts)

    embedding_dimension = embeddings.shape[1]

    vector_store = VectorStore(embedding_dimension)

    vector_store.add_documents(
        embeddings,
        chunks
    )

    knowledge_agent = KnowledgeAgent(
        kg,
        vector_store
    )

    maintenance_agent = MaintenanceAgent(
        knowledge_agent
    )

    compliance_agent = ComplianceAgent(
        knowledge_agent
    )

    lessons_agent = LessonsLearnedAgent(
        knowledge_agent
    )

    update_agent = UpdateAgent(
        kg,
        vector_store
    )

    router_agent = RouterAgent(
        knowledge_agent,
        maintenance_agent,
        compliance_agent,
        lessons_agent
    )


    # =====================================================
    # User Query
    # =====================================================

    query = st.text_input(
        "Ask a question from the uploaded documents"
    )

    if query:
        
        category, answer, results = router_agent.route(query)

        st.info(
            f"🤖 Answered by: {category.replace('_', ' ').title()} Agent"
        )

        

        st.subheader("Retrieved Context")

        for item in results:

            chunk = item["chunk"]

            st.markdown(
                f"""
    **Document:** {chunk['document_name']}

    **Type:** {chunk['document_type']}

    **Page:** {chunk['page']}

    **Chunk ID:** {chunk['chunk_id']}

    **FAISS Score:** {item['faiss_score']:.4f}

    **CrossEncoder Score:** {item['reranker_score']:.4f}
    """
            )

            st.text_area(
                f"Chunk {chunk['chunk_id']}",
                chunk["text"],
                height=180,
                key=f"retrieved_{chunk['document_name']}_{chunk['chunk_id']}"
            )




            st.divider()

        st.subheader("Industrial Knowledge Assistant")

        st.text_area(
            "Answer",
            answer,
            height=300
        )


        st.markdown("### Was this answer helpful?")

        feedback = st.radio(

            "",

            ["👍 Yes", "👎 No"],

            horizontal=True

        )

        if feedback == "👎 No":

            update_text = st.text_area(

                "Provide the corrected or updated knowledge"

            )

            if st.button("Update Knowledge Base"):

                update_agent.update_knowledge(update_text)

                st.success(

                    "Knowledge Base Updated Successfully!"

                )



                    