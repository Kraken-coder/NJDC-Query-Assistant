from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
import pandas as pd
class Engine:
    def __init__(self):
        self.df1 = pd.read_csv("https://api.data.gov.in/resource/05108a17-20e1-4f77-bb6d-bb28e412d8ed?api-key=579b464db66ec23bdd00000131e09981a5794cd863858fd3fa249829&format=csv")
        self.df2 = pd.read_csv("https://api.data.gov.in/resource/04872746-762a-4dec-8b80-d7be23b1c1c6?api-key=579b464db66ec23bdd000001467bffcff449404b71bf2bf9487e9494&format=csv")
        self.df3 = pd.read_csv("https://api.data.gov.in/resource/390d646f-a415-4ed0-9601-419db62c72d4?api-key=579b464db66ec23bdd0000012369d6e2d71848ce66f895844edd7319&format=csv")  
        self.df4 = pd.read_csv("https://api.data.gov.in/resource/909348af-833d-4a9a-a1db-779dfbb7f3fe?api-key=579b464db66ec23bdd00000145af631e055c4aa97a40f6826da90025&format=csv")
        self.llm = Ollama(model='llama3:instruct')
        self.queryengine1 = PandasQueryEngine(df = self.df1 , verbose = True , llm= self.llm)
        self.queryengine2 = PandasQueryEngine(df=self.df2 , verbose= True, llm= self.llm)
        self.queryengine3 = PandasQueryEngine(df=self.df3 , verbose= True, llm= self.llm)  
    def update_data(self):
        try:
            self.df1 = pd.read_csv("https://api.data.gov.in/resource/05108a17-20e1-4f77-bb6d-bb28e412d8ed?api-key=579b464db66ec23bdd00000131e09981a5794cd863858fd3fa249829&format=csv")
            self.df2 = pd.read_csv("https://api.data.gov.in/resource/04872746-762a-4dec-8b80-d7be23b1c1c6?api-key=579b464db66ec23bdd000001467bffcff449404b71bf2bf9487e9494&format=csv")
            self.df3 = pd.read_csv("https://api.data.gov.in/resource/390d646f-a415-4ed0-9601-419db62c72d4?api-key=579b464db66ec23bdd0000012369d6e2d71848ce66f895844edd7319&format=csv")      
            return "data returned successfully" 
        except:
            print("Something went wrong")
    def AgentToolMaster(self):
        tools = [
            QueryEngineTool(
                query_engine=self.queryengine1,
                metadata=ToolMetadata(
                    name="PendencyDataLowerJudiciary",
                    description="Get data of State/UT-wise Pendency of Civil and Criminal Cases in Respect of Lower Judiciary"
                )
            ),
            QueryEngineTool(
                query_engine=self.queryengine2,
                metadata=ToolMetadata(
                    name="PendencyDataHighCourts",
                    description="Get data of Court-wise Number of Cases Pending in the High Courts"
                )
            ),
            QueryEngineTool(
                query_engine=self.queryengine3,
                metadata=ToolMetadata(
                    name="PendencyDataDistrictCourts",
                    description="Get data of State/UT-wise Details of Pending Cases in District & Subordinate Courts"
                )
            )
        ]
        self.agent = ReActAgent.from_tools(tools , llm = self.llm , verbose= True , context= "Purpose : You are helping assistant chatbot of National Justice Data Grid you have to use relevant tool to answer your tools include {State/UTs-wise_Pendency ,Cases_Pending_in_the_High_Courts , Pending_Cases_in_District_&_Subordinate Courts} to use these tools pass the user prompt directly ")
    def complete(self,text):
        text = self.agent.query(text)
        return text
        
        