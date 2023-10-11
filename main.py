###################################
# !/usr/bin/python
# Python 3.10
# (C) 2023 admi.tech
###################################

# Import main packages
import openai

# Connection Key to openAI
openai.api_key = " "  # add your own key - go to web and generate one


# FUNCTIONS
def chat_with_bot(question):
    answer = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": question}]
    )
