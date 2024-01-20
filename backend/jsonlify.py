import pandas as pd
import math

DATA_PATH = "gatorhacks/data/dataset.csv"

df = pd.read_csv(DATA_PATH)

with open('gatorhacks/data/dataset.jsonl', 'w') as file:
    file.write('[\n')
    for idx in df.index:
        input = 'I have '
        for i in range(1, 17):
            symptom = df['Symptom_' + str(i)][idx]

            if isinstance(symptom, str):
                for char in symptom:
                    if char != '_':
                        input += char

                input += ' and '

            elif math.isnan(symptom):
                break
        
        input = input[:-5]
        output = "You must have a " + df['Disease'][idx] + '.'

        if idx != 4919:
            file.write('{"role": "user", "content": "' + input + '"},')
            file.write('\n')
            file.write('{"role": "assistant", "content": "' + output + '"},')
            file.write('\n')

        else:
            file.write('{"role": "user", "content": "' + input + '"},')
            file.write('\n')
            file.write('{"role": "assistant", "content": "' + output + '"}')
            file.write('\n')


    file.write(']')