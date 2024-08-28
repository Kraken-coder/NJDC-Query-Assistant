from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent
from llama_index.core import SimpleDirectoryReader
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.core import StorageContext
from llama_index.core import KnowledgeGraphIndex
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from Court import court
class Engine:
    def __init__(self):
        self.llm = Ollama(model='llama3:instruct')
        documents = SimpleDirectoryReader("NJDC-Query-Assistant/ChatBOT/datacheck", exclude_hidden=False).load_data()
        graph_store = SimpleGraphStore()
        storage_context = StorageContext.from_defaults(graph_store=graph_store)
        embed_model = resolve_embed_model("local:BAAI/bge-m3")
        index = KnowledgeGraphIndex.from_documents(documents=documents,
                                                   max_triplets_per_chunk=3,
                                                   storage_context=storage_context,
                                                   embed_model=embed_model,
                                                   include_embeddings=True,
                                                   llm=self.llm)
        self.query_engine = index.as_query_engine(include_text=True,
                                                  response_mode="tree_summarize",
                                                  embedding_mode="hybrid",
                                                  similarity_top_k=5,
                                                  llm=self.llm)

    def AgentToolMaster(self):
        tools = [
            court,
            QueryEngineTool(
                query_engine=self.query_engine,
                metadata=ToolMetadata(
                    name="Helper",
                    description="Use this for queries related to procedures like paying traffic violation fines, live streams of court cases, eFiling, ePay, Fast Track Courts, or downloading the eCourts Services Mobile App."
                )
            )
        ]
        self.agent = ReActAgent.from_tools(
            tools,
            llm=self.llm,
            verbose=True,
            context=(
                "Purpose: You are the assistant chatbot of the National Justice Data Grid. "
                "Use the 'court' tool for specific court-related queries. To use this tool pass the users query directly without any modifications it takes only one argument which is the user query. "
                "Use 'Helper' for assisting with general procedural inquiries such as payment, live streams, or downloading apps."
            )
        )

    def complete(self, text):
        return self.agent.query(text)   