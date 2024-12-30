import streamlit as st
import logging
from car_price_predictor.scripts.ai_chat_analyst_script import QASystem

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Verify QASystem import
try:
    logger.info("Successfully imported QASystem")
except Exception as e:
    logger.error(f"Error importing QASystem: {e}")

# Initialize Streamlit session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'qa_system' not in st.session_state:
    st.session_state.qa_system = None
    st.session_state.chain = None

# Initialize the QASystem
def initialize_qa_system():
    sources = [
        {
            "path": "Sources/mmv.pdf",
            "type": "pdf"
        },
        {
            "path": "Sources/autoconsumer.pdf",
            "type": "pdf"
        },
        {
            "path": "Sources/car_prices.csv",
            "type": "csv",
            "columns": ['year', 'make', 'model', 'trim', 'body', 'transmission', 'vin', 'state', 'condition', 'odometer', 'color', 
                'interior', 'seller', 'mmr', 'sellingprice', 'saledate']
        }
    ]
    try:
        st.session_state.qa_system = QASystem(chunk_size=1000, chunk_overlap=50)
        st.session_state.chain = st.session_state.qa_system.create_chain(sources)
        logger.info("QA System initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing QA System: {e}")
        raise e

# Page configuration
st.set_page_config(
    page_title="🚗 AI Chat Assistant",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Main title with custom styling
st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>🚗 AI Chat Assistant</h1>
    """, unsafe_allow_html=True)

# Initialize QA system if not done
if st.session_state.qa_system is None:
    with st.spinner("Initializing AI system..."):
        try:
            initialize_qa_system()
            st.success("System initialized successfully! Ready to chat about cars!")
        except Exception as e:
            st.error(f"Failed to initialize system: {str(e)}")

# Create layout containers
st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True)
chat_container = st.container()
input_container = st.container()

# Chat interface in the chat container
with chat_container:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Input interface in the input container
with input_container:
    st.markdown("<div style='height: 5vh;'></div>", unsafe_allow_html=True)
    
    # Chat input with placeholder text
    if user_input := st.chat_input("Ask me anything about cars..."):
        # Log user input
        logger.info(f"Received user input: {user_input}")
        
        # Add and display user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate and display AI response
        with st.chat_message("assistant"):
            placeholder = st.empty()
            try:
                response = st.session_state.chain.invoke(user_input)
                placeholder.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                logger.info("Successfully generated response")
            except Exception as e:
                error_msg = f"Error generating response: {str(e)}"
                placeholder.error(error_msg)
                logger.error(error_msg)

# Add bottom spacing
st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True)