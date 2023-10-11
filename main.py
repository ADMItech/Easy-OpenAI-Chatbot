###################################
# !/usr/bin/python
# Python 3.10
# (C) 2023 admi.tech
###################################

# Import main packages
import openai

# Connection Key to openAI
openai.api_key = "key"  # add your own key - go to web and generate one


# FUNCTIONS
def chat_with_bot(question1):
    """Function takes question and returns answer of ChatGPT"""
    answer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question1}
        ]
    )
    return answer.choices[0]['message']['content']


# MAIN LOOP
if __name__ == "__main__":
    while True:
        question = input("Ty : ")
        if question.lower() in ["koniec", "exit"]:
            break
        print("Počítač : ", chat_with_bot(question))
