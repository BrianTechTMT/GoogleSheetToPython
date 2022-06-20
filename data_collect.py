import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def TtoDict():
    #Create Dataframe from excel using pandas
    df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vTQr39fyluen76s_gIE4_9E6jcTak1CksY8igZ8qlnvGzlm9TACmW0wcVpLViNDDvotluBmk4e8HVNg/pub?output=xlsx")
    #Create a list of headers from dataframe
    header_columns = df.columns
    #Convert the Dataframe into dictionary of dictionaries
    user_dict = df.set_index(header_columns[0]).T.to_dict('dict') # Return Table into a list of dictionaries
    return user_dict

#Iterate the dictionaries from the main dictionary
list=[]
testDict = TtoDict() # Acquiring Data collected Table
for k,v in testDict.items(): 
    list.append(v) # Put all the data in list of dictionaries
for records in list: # Iterate through each dictionary
        obj_list=[]
        for x,y in records.items():
            print(x,":",y) # Print out each value
                                       