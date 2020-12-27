import requests
import pandas as pd

'''according to the website instructions for pulling season averages from api, you can only 
    pull individual averages. we must concatenate string to get all players according to id'''
query = ""

for i in range(1,493):
    query+= "&player_ids[]=" + str(i)

'''add query to command url and use results.get() to pull data from api'''
curl = "https://www.balldontlie.io/api/v1/season_averages?season=2017" + query
response = requests.get(curl)

'''to understand how to parse the json file, print the response in json format using 
result.json(). use json.dumps() for better format. comment it when finished'''
#import json
#print(json.dumps(response.json(),indent=2))

'''since the json file is a list of dictionaries, you can simply pass it into a pandas df. 
    Now change player ids to player names using the csv file created earlier. Since the
    dataframes are offset, use a variable to account for it'''
stats = pd.DataFrame(response.json()['data'])
name = list(pd.read_csv(r"C:\Users\AJ Advincula\python-workspace\pycharm\name.csv"))
offset=0

for i in range(len(stats.index)):
    if i+offset+1!=stats.loc[i, 'player_id']:
        offset+=1

    stats.loc[i, 'player_id'] = name[i + offset]

'''the following is from https://www.basketball-reference.com/contracts/players.html and there is an option to 
    get salary table as csv. We will be using the 2017 salaries. Before merging stats with salary, make sure 
    columns are the same'''
salary = pd.read_csv(r"C:\Users\AJ Advincula\python-workspace\pycharm\NBA_season1718_salary.csv")
stats.rename(columns={'player_id': 'Player'}, inplace=True)
player_info = pd.merge(stats, salary, on='Player')

'''now save the df to mySQL. To save a pandas df to mySQL, you must use sqlaclhemy and create_engine 
    method. The string must be as follows: 'mysql+pymysql://(user):(pw)@(server)/(schema)'. I won't
    sow this due to sensitive info'''
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://(user):(pw)@(server)/(schema)')
player_info.to_sql(name='player_info',con=engine,index=False,if_exists='replace')
