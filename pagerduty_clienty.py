import requests
import json

API_TOKEN = 'y_NbAkKc66ryYTWUXYEu'

class PagerdutyClient:
  def http_get(url):

    base_url = 'https://api.pagerduty.com/'
    url = base_url + url
    # print(url)
    headers = {
      "User-Agent": "Mozilla/5.0",
      "Accept": "application/vnd.pagerduty+json;version=2",
      "Authorization": "Token token=" + API_TOKEN
    }
    # print(f"\nSending 'GET' request to URL : %s" %(url))
    response = requests.get(url, headers=headers)

    # print("Response Code : %s" %(response.status_code))
    # print(response)
    return response.text
    
  def get_input_line():
    return input()

data = PagerdutyClient.http_get('users')
parse_json = json.loads(data)

# Print list of Users - Names and IDs
for user in range(len(parse_json['users'])):
  print("Name: %s  ID: %s" % (parse_json['users'][user]['name'],parse_json['users'][user]['id']))

# Print list of Users and Contact Methods
for user in range(len(parse_json['users'])):
  print("Name: %s  ID: %s" % (parse_json['users'][user]['name'],parse_json['users'][user]['id']))
  userID = parse_json['users'][user]['id']
  cmData = PagerdutyClient.http_get('users/' + userID + '/contact_methods')
  cmparse_json = json.loads(cmData)
  for cm in range(len(cmparse_json['contact_methods'])):
    print("Contact Method Type: %s  Address: %s" % (cmparse_json['contact_methods'][cm]['type'],cmparse_json['contact_methods'][cm]['address']))
