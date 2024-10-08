# NJDC-Query-Assistant

## Project Overview

The NJDC-Query-Assistant is an AI-powered chatbot designed to assist users by providing information related to the Department of Justice (DoJ). The chatbot can answer queries about various divisions of the DoJ, the number of judges appointed in different courts, case pendency data from the National Judicial Data Grid (NJDG), procedures for paying traffic fines, live streaming of court cases, eFiling and ePay steps, Fast Track Courts, the eCourts Services Mobile app, Tele Law Services, and current case statuses.

### Key Features:
- **Divisions of DoJ**: Information about various divisions within the DoJ.
- **Judges and Vacancies**: Number of judges in Supreme Court, High Courts, District & Subordinate Courts, and current vacancies.
- **Case Pendency**: Data on pending cases through NJDG.
- **Traffic Fine Payment**: Guidance on how to pay fines for traffic violations.
- **Live Streaming**: Information on live streaming of court cases.
- **eFiling and ePay**: Steps for eFiling and ePay services.
- **Fast Track Courts**: Details about working Fast Track Courts.
- **eCourts Services Mobile App**: Information on downloading and using the eCourts Services Mobile app.
- **Tele Law Services**: Access to Tele Law services.
- **Case Status**: Information on the current status of specific cases.

The chatbot is designed to learn over time, improving its responses and capabilities, and is capable of handling large datasets.

## Installation Guide

To set up and run the NJDC-Query-Assistant, follow these steps:



https://github.com/user-attachments/assets/c85d6615-6206-4d17-b1ec-d51db6e24aac



Also install Ollama on you system and then from cmd run
```bash
ollama run llama3:instruct
ollama run llama3
```


### Running the Chatbot

You can test the chatbot using the following script:

```python
from ChatBoT import Engine

# Initialize the chatbot engine
trial = Engine()

# Example of querying the chatbot
trial.AgentToolMaster()
print(trial.complete("Tell me which state has the most number of pending criminal cases"))
```
### Work in progress demo Video


https://github.com/user-attachments/assets/866423ab-a7a7-4db0-98a4-d0706d932ac9



### Known Issues

- Ensure that all dependencies are correctly installed.
- The chatbot currently supports queries in English.
- FrontEnd and Backend are not linked.
