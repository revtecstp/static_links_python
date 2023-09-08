import base64, requests, sys, io
import pandas as pd


CLIENT_ID = "4feb4478-d03a-4b8f-857f-fa473a23c8ac"
CLIENT_SECRET = "6Gq-1cIEuZC1tQHnkxPuU8kjpYSJmwQB3pkpZowhAX8"
ENVIRONMENT = "mypurecloud.com"
STATIC_LINK_URL = "https://apps.mypurecloud.com/platform/api/v2/downloads/ed3eafaa66474941"


response = requests.post(f"https://login.{ENVIRONMENT}/oauth/token", data={
  "grant_type": "client_credentials"
}, headers={
  "Authorization": f'Basic {base64.b64encode(bytes(CLIENT_ID + ":" + CLIENT_SECRET, "ISO-8859-1")).decode("ascii")}',
  "Content-Type": "application/x-www-form-urlencoded"
})




if response.status_code != 200:
  sys.exit(response.status_code)


token_response_json = response.json()
response = requests.get(STATIC_LINK_URL, headers={
  "Authorization": f"{ token_response_json['token_type'] } { token_response_json['access_token']}"
})

print(f"{ token_response_json['token_type'] } { token_response_json['access_token']}")



if response.status_code != 200:
  sys.exit(response.status_code)
export=pd.read_csv(io.StringIO(response.content.decode('utf-8')))
print(export)