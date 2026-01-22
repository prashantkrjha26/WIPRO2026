import requests

geturl = "http://127.0.0.1:5000/users"


response = requests.get(geturl)

print("get status code", response.status_code)
print(response.json())


posturl = "http://127.0.0.1:5000/users"

body1= {
    "name":"Rahul"
}

r1 = requests.post(posturl, json=body1)
print("post status code", r1.status_code)
print(r1.json())


puturl = "http://127.0.0.1:5000/users/2"

body2= {
    "name":"Sita"
}

r2 = requests.put(puturl, json=body2)
print("put status code", r2.status_code)
print(r2.json())


deleteurl = "http://127.0.0.1:5000/users"

r3 = requests.delete(deleteurl)
print("delete status code", r3.status_code)

