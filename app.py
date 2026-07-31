import time
import streamlit as st
from generation import generate_answer
from retrieval import retrieve_documents

# -----------------------------
# Page Configuration & Theme injection
# -----------------------------
st.set_page_config(
    page_title="RAG Playground Pro",
    page_icon="⚡",
    layout="wide",
)

# Injecting modern CSS for gradients, soft shadows, transitions, and glow effects
st.html("""
    <style>
        /* Global font/style adjustments */
        .stApp {
            background: linear-gradient(180deg, #0e1117 0%, #161a24 100%);
        }
        
        /* Modern Header Glow */
        .main-header {
            background: linear-gradient(45deg, #FF4B4B, #4A90E2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 2.8rem !important;
            margin-bottom: 0px;
        }
        
        /* Glassmorphism containers */
        div[data-testid="stVVerticalBlockBorder"] {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 12px !important;
            padding: 20px !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease-in-out;
        }
        
        div[data-testid="stVVerticalBlockBorder"]:hover {
            border-color: rgba(74, 144, 226, 0.4) !important;
            box-shadow: 0 4px 25px rgba(74, 144, 226, 0.1);
        }

        /* Sleek Pills/Badges */
        .source-badge {
            display: inline-block;
            background: rgba(74, 144, 226, 0.15);
            color: #4A90E2;
            border: 1px solid rgba(74, 144, 226, 0.3);
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            margin: 4px;
            transition: background 0.2s;
        }
        .source-badge:hover {
            background: rgba(74, 144, 226, 0.3);
        }

        /* Custom Streamlit Button Styling overrides */
        button[data-testid="stBaseButton-secondaryFormSubmit"], 
        button[data-testid="stBaseButton-secondary"] {
            background: linear-gradient(90deg, #FF4B4B 0%, #ff7676 100%) !important;
            color: white !important;
            font-weight: 600 !important;
            border: none !important;
            border-radius: 8px !important;
            transition: transform 0.1s ease, box-shadow 0.2s ease !important;
        }
        button[data-testid="stBaseButton-secondary"]:hover {
            transform: translateY(-1px);
            box-shadow: 0 0 15px rgba(255, 75, 75, 0.4) !important;
        }
        
        /* Expander tweaks */
        .streamlit-expanderHeader {
            background-color: rgba(255, 255, 255, 0.02) !important;
            border-radius: 6px !important;
        }
    </style>
""")

# -----------------------------
# Data Maps
# -----------------------------
COLLECTION_MAP = {
    "FAQs": "faqs",
    "Knowledge Base Articles": "knowledge_base_articles",
    "Product Documentation": "product_documentation",
}

COLLECTIONS = {
    "FAQs": {
        "collection": COLLECTION_MAP["FAQs"],
        "sources": ["GitHub", "OpenAI", "Stripe"],
    },
    "Knowledge Base Articles": {
        "collection": COLLECTION_MAP["Knowledge Base Articles"],
        "sources": ["Atlassian", "Notion"],
    },
    "Product Documentation": {
        "collection": COLLECTION_MAP["Product Documentation"],
        "sources": [
            "Docker",
            "Python Stdlib & Async",
            "Kubernetes",
            "React Hooks & Patterns",
        ],
    },
}

# -----------------------------
# Sidebar Configuration
# -----------------------------
with st.sidebar:
    st.markdown("### Control Center")
    doc_type = st.radio("Choose a document category", list(COLLECTIONS.keys()))
    st.divider()
    
    st.subheader("Available Sources")
    # Modern micro-pill elements instead of a standard bullet list
    badges_html = "".join([f'<span class="source-badge">{source}</span>' for source in COLLECTIONS[doc_type]["sources"]])
    st.html(f"<div>{badges_html}</div><br>")
    
    st.divider()
    st.subheader("Retrieval Settings")
    top_k = st.slider(
        "Number of chunks to retrieve",
        min_value=1,
        max_value=30,
        value=10,
        step=1,
        help="Controls how many chunks are fetched before reranking.",
    )
    st.caption("The reranker will optimize and filter down to the top 5 chunks.")
    st.divider()
    st.info(
        f"Connected Collection:\n\n"
        f"`{COLLECTIONS[doc_type]['collection']}`"
    )

# -----------------------------
# Main Header Layout
# -----------------------------
st.html('<h1 class="main-header">RAG Console</h1>')
st.caption("Compare advanced retrieval, neural reranking, and generation topologies seamlessly.")
st.write("")

# Initialize Session State Variables
for key in ["retrieved_docs", "reranked_docs", "retrieval_error", "generation_error", "generated_answer"]:
    if key not in st.session_state:
        st.session_state[key] = [] if "docs" in key else ""
if "response_time" not in st.session_state:
    st.session_state.response_time = "0 ms"

# -----------------------------
# Top-Level Modern Performance Metrics Card
# -----------------------------
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.metric("Retrieved Vector Chunks", len(st.session_state.retrieved_docs))
with m_col2:
    st.metric("Cross-Encoder Filtered", len(st.session_state.reranked_docs[:5]))
with m_col3:
    st.metric("Latency Performance", st.session_state.response_time)

st.write("")

# -----------------------------
# Query Execution Section
# -----------------------------
query = st.text_area(
    "Ask your pipeline a question",
    placeholder="e.g., How does Kubernetes service discovery work?",
    height=100,
)

run_button = st.button("Run Search", use_container_width=True)

if run_button and query.strip():
    start_time = time.perf_counter()
    with st.spinner("Executing dense vector retrieval and computing LLM responses..."):
        try:
            retrieved_docs, reranked_docs = retrieve_documents(
                query=query,
                collection_label=doc_type,
                top_k=top_k,
                return_all=True,
            )
            st.session_state.retrieved_docs = retrieved_docs
            st.session_state.reranked_docs = reranked_docs
            st.session_state.retrieval_error = ""
            
            if reranked_docs:
                st.session_state.generated_answer = generate_answer(query, reranked_docs)
                st.session_state.generation_error = ""
            else:
                st.session_state.generated_answer = "No relevant chunks were found to generate an answer."
                st.session_state.generation_error = ""
                
            st.session_state.response_time = f"{round((time.perf_counter() - start_time) * 1000, 1)} ms"
            st.rerun()  # Forces layout refresh to reflect metric metrics instantly
        except Exception as exc:
            st.session_state.retrieved_docs = []
            st.session_state.reranked_docs = []
            st.session_state.retrieval_error = str(exc)
            st.session_state.generation_error = ""
            st.session_state.generated_answer = ""
            st.session_state.response_time = "Error"

st.write("")

# -----------------------------
# Primary Results Pane: Final Answer First
# -----------------------------
st.subheader("🤖 Generated Synthesized Answer")
answer_container = st.container(border=True)
with answer_container:
    if st.session_state.generation_error:
        st.error(st.session_state.generation_error)
    elif st.session_state.generated_answer:
        st.markdown(st.session_state.generated_answer)
    else:
        st.caption("Waiting for query input execution... Final contextual output will materialize here.")

st.write("")

# -----------------------------
# Deep-Dive Granular Data Chunks Layout
# -----------------------------
def display_chunks_with_expand(chunks, title, max_preview_chars=180):
    if not chunks:
        return
    for index, doc in enumerate(chunks, start=1):
        chunk_text = doc.page_content.strip() if hasattr(doc, 'page_content') else str(doc).strip()
        if not chunk_text:
            chunk_text = "(empty chunk)"
        
        preview = chunk_text[:max_preview_chars] + ("..." if len(chunk_text) > max_preview_chars else "")
        
        # Polished custom header string inside an elegant layout expander block
        with st.expander(f"📄 {title} #{index} | `{preview[:40]}`...", expanded=False):
            st.text_area("Full Source Text Context", chunk_text, height=150, disabled=True, key=f"ta_{title}_{index}")

left_col, right_col = st.columns([1, 1], gap="medium")

with left_col:
    st.subheader("Vector Retrieved Chunks")
    with st.container(border=True):
        if st.session_state.retrieval_error:
            st.error(st.session_state.retrieval_error)
        elif st.session_state.retrieved_docs:
            display_chunks_with_expand(st.session_state.retrieved_docs, "Retrieved Chunk")
        else:
            st.caption("Raw context chunks vector pool returns will map here.")

with right_col:
    st.subheader("Re-ranked Top Chunks")
    with st.container(border=True):
        if st.session_state.reranked_docs:
            display_chunks_with_expand(st.session_state.reranked_docs[:5], "Reranked Top Match")
        else:
            st.caption("Reranked cross-encoder alignments will map here.")