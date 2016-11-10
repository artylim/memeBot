import json
from pip._vendor import requests

botId = "09627250596d98c0f84afe710d"

data = {
  "bot_id"  : botId,
  "text"    : "Posting in Python is working"
}

req = requests.post('https://api.groupme.com/v3/bots/post', data)