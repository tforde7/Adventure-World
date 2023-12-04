"""
Script for creating a PromptTemplate to guide an AI-driven storytelling adventure.

This script imports necessary modules and sets up a PromptTemplate for an epic journey narrative
where an AI serves as the guide and the player assumes the role of a young wizard.

Modules:
- langchain.llms: OpenAI language model handling
- langchain.chains: LLMChain for interaction between OpenAI model and memory
- langchain.prompts: PromptTemplate for structuring AI-guided narrative prompts
- langchain.memory: CassandraChatMessageHistory and ConversationBufferMemory for managing conversation history

Usage:
- Set up OpenAI API key and database keyspace for chat message history.
- Define a narrative template outlining the adventure, rules, and guidelines for the AI and player.
- Create a PromptTemplate instance incorporating the narrative template and input variables.
- Initialize OpenAI language model and the LLMChain for interaction with the defined PromptTemplate.

Note: Modify the template, rules, and guidelines for specific narrative objectives and storytelling dynamics.
"""

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
# from database import session

# ASTRA_DB_KEYSPACE = "database"
# OPENAI_API_KEY = "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"

# message_history = CassandraChatMessageHistory(
#     session_id="anything",
#     session=session,
#     keyspace=ASTRA_DB_KEYSPACE,
#     ttl_seconds=3600
# )

# message_history.clear()

# cass_buff_memory = ConversationBufferMemory(
#     memory_key="chat_history",
#     chat_memory=message_history
# )

# template = """
# You are now the guide of a magical quest in the Wizarding World.
# Harry, Ron  and Hermione are on a quest to find the final horcrux and destroy Voldemort.
# You must navigate her through challenges, choices, and consequences,
# dynamically adapting the tale based on our heroes' decisions.
# Your goal is to create a branching narrative experience where each choice
# leads to a new path, ultimately determining the young wizards' fate.

# Here are some rules to follow:
# 1. Start by asking the player to choose some kind of weapons that will be used later in the game.
# 2. No response by the player should be deemed incorrect. Be creative and witty with the player's response even if it seems to make no sense.
# 3. Always either ask the player a direct question or give them options to choose.
# 4. Do not finish your response with "Are you ready?" or a similar question.
# 5. Follow the player's lead and do not tell them that something is not possible.
# 6. Have a few paths that lead to success. If the player defeats Voldemort generate a response that explains the win and ends in the text "The end.", I will search for this text to end the game.
# 7. Have some paths that lead to death. If the player dies generate a response that explains the death and ends in the text: "The end.", I will search for this text to end the game.

# Here is the chat history, use this to understand what to say next: {chat_history}
# Human: {human_input}
# AI:"""

# prompt = PromptTemplate(
#     input_variables=["chat_history", "human_input"],
#     template=template
# )

# llm = OpenAI(openai_api_key=OPENAI_API_KEY)
# llm_chain = LLMChain(
#     llm=llm,
#     prompt=prompt,
#     memory=cass_buff_memory
# )
