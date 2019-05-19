# This lambda function written in python will query Cricapi.com's api to fetch cricket score and post it in Slack using webhook. 
# Note that the variables unique_id, webhook_url and url are unique to your environment and should be changed as required.

from botocore.vendored import requests
from pprint import pprint
import json

def print_out_statment(inputdata):
      for datas in (inputdata['data']):
          if ((datas['unique_id']) == '*****'):
               return (datas['description'])
               
def lambda_cric(event, context):
   webhook_url = "https://hooks.slack.com/services/**********"
   url = "https://cricapi.com/api/cricket?apikey=**********"
   res = requests.get(url)
   data = res.json()
   message = print_out_statment(data)
   slack_message = {'text': message}
   lambda_score = requests.post(webhook_url,data=json.dumps(slack_message))
