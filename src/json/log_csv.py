
# import necessary libraries
import pandas as pd
import os
import glob
  
  
# use glob to get all the csv files 
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "logs/*.log"))
  
  
# loop over the list of csv files
for f in csv_files:
      
    # read the csv file
    df = pd.read_csv(f, sep = '|', index_col=False , names=["tiempo", "hora", "ip", "host", "method", "baseUrl",  "content", "agent", "originalUrl", "body", "query", "params", "route", "response" ])
      
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
      
    # print the content
    print('Content:')    
    info = df[["tiempo", "hora", "ip", "host", "method"]]
    print(info)
 