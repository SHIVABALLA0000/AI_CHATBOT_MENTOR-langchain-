### AI CHATBOT MENTOR

A) __OVERVIEW__
1)AI Chatbot Mentor is a domain-specific intelligent learning assistant designed to provide focused mentorship across multiple technical subjects.
2)Unlike generic chatbots, the system restricts responses strictly to the user-selected learning module, ensuring accurate, relevant, and distraction-free guidance.
3)The application delivers an interactive mentoring experience where learners can ask questions, maintain session-based conversations, clear discussions, and download chat history for later reference.

B) __IMPLEMENTATION__
1)The system is implemented using Streamlit for the user interface and LangChain for large language model orchestration.
2)A module-selection interface initializes the session by activating a domain-specific system prompt. This prompt enforces strict response boundaries by instructing the language model to answer only within the selected domain and reject unrelated questions with a predefined response.
3)Conversation memory is maintained using Streamlit’s session state, enabling coherent multi-turn interactions.
4)Clear-chat functionality resets the conversation while preserving domain constraints, and a chat-download feature exports the full session as a text file for offline learning or documentation.
5)The architecture is modular, separating UI logic, prompt definitions, LLM configuration, and utility functions for clarity and maintainability.