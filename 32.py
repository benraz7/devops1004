import requests
response = requests.post("http://192.168.0.101:5001/whatismyname")
expected = "saved new car"
assert expected == response.text
