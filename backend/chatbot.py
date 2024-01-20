import os
import spacy
import scispacy
from collections import deque

os.environ["REPLICATE_API_TOKEN"] = "r8_331JLxDWN8d5QW8X6lWIFP9JqLTqofU2UlN10"

import replicate

nlp = spacy.load('en_core_web_sm')
current_convo = deque(maxlen = 10)

def main():
    print(get_doctor_type('I need to see a cardiologist maybe'))
    # while(True):
    #     text = input()
    #     data = generate_response(text)
    #     print(data)
    

def get_diseases(data: str) -> set:
    doc = nlp(data)
    diseases = set()
    for ent in doc.ents:
        if ent.label_ == 'DISEASE':
            diseases.add(ent.text)

    return diseases

def get_doctor_type(data: str) -> str:
    doc = nlp(data)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    doctor_types = [entity for entity in entities if "doctor" in entity[0].lower()]
    return doctor_types[0][0]

def generate_response(data: str) -> str:
    preprompt = 'I will give you input and you act as a diagnosis chatbot'
    current_convo.append(data)

    conversation_history = " ".join(current_convo)

    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
        input={
            "prompt": f"{conversation_history} \n ###Assistant: ",
            "temperature": 0.1,
            "top_p": 0.9,
            "max_length": 750,
            "repetition_penalty": 1
        })

    full_response = ""

    for item in output:
        full_response += item

    current_convo.append(full_response)

    return full_response


if __name__ == '__main__':
    main()