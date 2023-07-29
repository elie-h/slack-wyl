# from langchain.agents import AgentType, Tool, initialize_agent
# from langchain.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.utilities import PythonREPL, SearxSearchWrapper, TextRequestsWrapper


# # Agent POC: Not currently used anywhere
# def generate_agent_response(conversation: list[Message]) -> str:
#     search = SearxSearchWrapper(searx_host="http://127.0.0.1:8080", k=10)
#     requests = TextRequestsWrapper()
#     python_repl = PythonREPL()

#     def search_func(input: str):
#         res = search.results(input, num_results=5)
#         formatted_results_list = []
#         for r in res:
#             formatted_results_list.append(
#                 f"{r['title']} - {r['link']} - {r['snippet']}"
#             )

#         formatted_results = "\n".join(formatted_results_list)
#         return formatted_results

#     tools = [
#         Tool(
#             name="Current Search",
#             func=search_func,
#             description="useful for when you need to answer questions about current events or the current state of the world. the input to this should be a single search term.",
#         ),
#         Tool(
#             name="Get Page",
#             func=requests.get,
#             description="useful for when you need to get the contents of a webpage. the input to this should be a single url.",
#         ),
#         Tool(
#             name="Python Repl",
#             func=python_repl.run,
#             description="useful for when you need to run python code to answer questions",
#         ),
#     ]

#     memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#     for message in conversation[:-1]:
#         if message.role == RoleEnum.USER:
#             memory.chat_memory.add_user_message(message.content)
#         elif message.role == RoleEnum.AI:
#             memory.chat_memory.add_ai_message(message.content)
#         else:
#             raise ValueError("Invalid role on message", message)

#     llm = ChatOpenAI(client=None, openai_api_key=OPENAI_API_KEY, temperature=0)
#     agent_chain = initialize_agent(
#         tools,
#         llm,
#         agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
#         verbose=True,
#         memory=memory,
#     )

#     output = agent_chain.run(input=conversation[-1].content)
#     return output
