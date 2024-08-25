from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
import pandas as pd
llm = Ollama(model='llama3', request_timeout=120)
df1 = pd.read_csv("https://api.data.gov.in/resource/05108a17-20e1-4f77-bb6d-bb28e412d8ed?api-key=579b464db66ec23bdd00000131e09981a5794cd863858fd3fa249829&format=csv").to_string()
df2 = pd.read_csv("https://api.data.gov.in/resource/04872746-762a-4dec-8b80-d7be23b1c1c6?api-key=579b464db66ec23bdd000001467bffcff449404b71bf2bf9487e9494&format=csv").to_string()
df3 = pd.read_csv("https://api.data.gov.in/resource/390d646f-a415-4ed0-9601-419db62c72d4?api-key=579b464db66ec23bdd0000012369d6e2d71848ce66f895844edd7319&format=csv").to_string()
final_string = df1+ df2+ df3
def Court(text):
    text = "Generate a complete/proper response for the query from the following data "+ text+ final_string
    completed_text = llm.complete(text)
    return f'generated job description from other llm : {completed_text}'
court = FunctionTool.from_defaults(Court,
                                       name="Court",
                                       description="Use this tool when you have to access information about the courts",
                                       return_direct=False)