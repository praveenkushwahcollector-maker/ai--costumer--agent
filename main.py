import os
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

class SmartCustomerAgent:
    def __init__(self, knowledge_file="knowledge.txt"):
        print("Loading knowledge base...")
        # 1. ज्ञान (Knowledge) फ़ाइल को लोड करना
        if os.path.exists(knowledge_file):
            loader = TextLoader(knowledge_file)
            self.index = VectorstoreIndexCreator().from_loaders([loader])
            print("Knowledge base loaded successfully!")
        else:
            self.index = None
            print("Warning: Knowledge file not found.")

    def ask(self, query):
        if not self.index:
            return "माफ़ कीजिए, मेरे पास अभी ज्ञान फ़ाइल (Knowledge Base) उपलब्ध नहीं है।"
        
        # 2. AI कस्टमर के सवाल का जवाब नॉलेज बेस से खोजकर देगा
        response = self.index.query(query)
        return response

if __name__ == "__main__":
    agent = SmartCustomerAgent()
    
    # टेस्ट सवाल
    question = "आपकी सेवाएं क्या-क्या हैं और संपर्क कैसे करें?"
    print(f"\nUser: {question}")
    print(f"AI Agent: {agent.ask(question)}")
