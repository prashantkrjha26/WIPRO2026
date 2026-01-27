import requests

# GET REQUEST
geturl = "http://127.0.0.1:5000/users"


headers={
    "Accept":"application/json",
    "User-Agent":"Python-Requests-Client"

}

response = requests.get(geturl, headers=headers, timeout=10)
print("get status code", response.status_code)
print(response.json())

# POST REQUEST
posturl = "http://127.0.0.1:5000/users"

body1= {
    "name":"Rahul"
}

r1 = requests.post(posturl, json=body1)
print("post status code", r1.status_code)
print(r1.json())

# PUT REQUEST
puturl = "http://127.0.0.1:5000/users/2"

body2= {
    "name":"Sita"
}

r2 = requests.put(puturl, json=body2)
print("put status code", r2.status_code)
print(r2.json())

# DELETE REQUEST
deleteurl = "http://127.0.0.1:5000/users"

r3 = requests.delete(deleteurl)
print("delete status code", r3.status_code)
