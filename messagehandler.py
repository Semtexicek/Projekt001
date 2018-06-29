import time
import requests
import json

# url
HOOKURL = "https://discordapp.com/api/webhooks/456596395927797771/Sc4Rv6p3Af8nDeH_ywV5uogdat3PU2NeUCuKNaPPON32FhgTk_aTpl9Cg02ejqId3ZeK"

'''post given message'''
def post_message(message):
    header = {"Content-Type" : "application/json"}
    messagejson = json.dumps({"content" : message})
    
    response = requests.post(HOOKURL, messagejson, headers = header)

    if response.ok:
        print ("OK!")
        return True
    
    print(response.reason)
    return False

