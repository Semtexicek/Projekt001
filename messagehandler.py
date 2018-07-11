import time
import requests
import json

# url

# '''post given message'''
# def post_message(message):
#     header = {"Content-Type" : "application/json"}
#     messagejson = json.dumps({"content" : message})
    
#     response = requests.post(HOOKURL, messagejson, headers = header)

#     if response.ok:
#         print ("OK!")
#         return True
    
#     print(response.reason)
#     return False

def post_message(message):
    print(message)
