import requests
import time
import csv

'''We need to use a for loop in order to get player first and last names. To bypass the rate limit 
of 60 requests per minute, use the time.sleep() method. Upload the results to a csv file'''
name = []

for i in range(1,493):
    curl = "https://www.balldontlie.io/api/v1/players/" + str(i)
    response = requests.get(curl)
    player_name = response.json()['first_name'] +" "+ response.json()['last_name']
    name.append(player_name)
    time.sleep(1.05)

with open('name.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(name)




