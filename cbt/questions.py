import random

question = [
    "1. What is the capital of Nigeria?",
    "2. Who developed python?",
    "3. Who developed this program",
    "4. What part of Africa is Nigeria located in Africa map",
    "5. Who designed the Nigeria flag"
]

answer = {
    "1": "Abuja",
    "2": "Richie",
    "3": "Adewale",
    "4": "west",
    "5": "Taiwo"
}

def generate_questions():
     print(random.choice(question))

generate_questions()