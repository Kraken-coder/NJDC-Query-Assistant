from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent
from Court import court
class Engine:
    def __init__(self):
        self.llm = Ollama(model='llama3:instruct')
 
    def AgentToolMaster(self):
        tools = [
            court
        ]
        self.agent = ReActAgent.from_tools(tools , llm = self.llm , verbose= True , context= "Purpose : You are helping assistant chatbot of National Justice Data Grid you have to use relevant tool to answer your tools include court to use these tools pass the user prompt directly ")
    def complete(self,text):
        text = self.agent.query(text)
        return text
        
        