"""
Business logic for AI agent with knowledge base integration.
"""
from dotenv import load_dotenv
load_dotenv()
import os
from llama_index.retrievers.bedrock import AmazonKnowledgeBasesRetriever
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.llms import ChatMessage, MessageRole

retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id=os.getenv("BEDROCK_KNOWLEDGE_BASE_ID"),
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 5}},
    )
llm = OpenAI(model=os.getenv("OPENAI_MODEL"))

_knowledge_base_tool = QueryEngineTool.from_defaults(
    query_engine=RetrieverQueryEngine(retriever=retriever),
    name="amazon_knowledge_base",
    description=(
        "A vector database containing research papers about AI, machine learning, "
        "and natural language processing techniques. Use this tool to answer questions "
        "about chain-of-thought prompting, reasoning in large language models, "
        "AI research methodologies, and related topics."
    ),
)

agent = ReActAgent(
    tools=[_knowledge_base_tool],
    llm=llm,
    system_prompt=(
        "You are a helpful AI research assistant with access to a knowledge base of AI research papers. "
        "When users ask questions about AI concepts, machine learning techniques, or research papers, "
        "use the available tool to retrieve accurate information from the knowledge base. "
        "Always provide clear, concise, and well-structured answers based on the retrieved information. "
        "If the information is not in the knowledge base, acknowledge this limitation. "
        "You must respond in English."
    ),
)


async def get_agent_response(message, chat_history):
    messages = []
    for msg in chat_history:
        if msg["role"] == "user":
            messages.append(ChatMessage(role=MessageRole.USER, content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(ChatMessage(role=MessageRole.ASSISTANT, content=msg["content"]))
    
    user_message = ChatMessage(role=MessageRole.USER, content=message)
    
    response = await agent.run(user_message, chat_history=messages)
    return str(response) 

