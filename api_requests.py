import requests
import json
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

print(pokemon_req.content)

# print(post_codes_req)
#
# print(post_codes_req.status_code)
# #headers - extra information provided by a client
# #print(post_codes_req.headers)
#
#  print(post_codes_req.content)
# print(post_codes_req.json())

# post - post requests are very api dependent

#json.dumps -. method to turn a python object (collection, variable, boolean, None) into JSON string
# json_body = json.dumps({"postcodes": ["SM1 4BU", "M45 6GN", "EX16 5BL"]})
#
# #json.dump -> writes to a json file
#
# headers = {"Content-Type": "application/json"}
#
# post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)
#
# print(post_multi_req.json())

