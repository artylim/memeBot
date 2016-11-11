import json
from pip._vendor import requests

testerId = "09627250596d98c0f84afe710d"
mainId = "708ba9d473b9e167294f4eb234"

data = {
  "testerId"  : botId,
  "text"    : "go fuck yourself"
}

req = requests.post('https://api.groupme.com/v3/bots/post', data)