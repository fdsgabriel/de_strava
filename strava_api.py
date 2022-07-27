import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"

#Refresh token last forever
#So this first part get the access token
payload = {
    "client_id":"90242",
    "client_secret":"95c57adc7a471656289002bd6b4b224d50934ecc",
    "refresh_token":"425ce659ab3ef77e64b3713b04dace6b0b9e743f",
    "grant_type":"refresh_token",
    "f":'json'
}

res = requests.post(auth_url,data=payload,verify=False)

access_token = res.json()['access_token']

print('Access token is: {}'.format(access_token))

#Second part: get data itself
header = {"Authorization":'Bearer ' + access_token}
param = {"per_page":200,'page':1}

my_dataset = requests.get(activities_url,headers=header,params=param).json()

#Saving as a file
file = open('Documents/fromAPI/strava_data.json', 'w', encoding='utf-8')
for dic in my_dataset:
    json.dump(dic, file) 
    file.write("\n")

print("Done")