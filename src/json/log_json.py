
# import necessary libraries
import pandas as pd
import json


try:
    
        # Opening JSON file
    f = open('logs/Logs_2023_01_25.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    print(data)

    df = pd.read_json('logs/Logs_2023_01_25.json')

    # print the content
    print('Content:')
    print(df)

except NameError:
    print("*********** An exception occurred ***********" + NameError)
