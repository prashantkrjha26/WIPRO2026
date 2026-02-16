*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
User Registration
    Create Session    foodie    ${BASE_URL}
    ${user}=    Create Dictionary    name=UserX    email=ux@mail.com    password=123
    ${response}=    POST On Session    foodie    /api/v1/users/register    json=${user}
    Status Should Be    201    ${response}

Give Rating
    Create Session    foodie    ${BASE_URL}
    ${restaurant}=    Create Dictionary    name=RateRest    category=Indian    location=Delhi    images=img    contact=1
    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${restaurant}
    ${rid}=    Get From Dictionary    ${r.json()}    id
    ${user}=    Create Dictionary    name=RateUser    email=rate@mail.com    password=123
    ${u}=    POST On Session    foodie    /api/v1/users/register    json=${user}
    ${uid}=    Get From Dictionary    ${u.json()}    id
    ${list}=    Create List
    ${order}=    Create Dictionary    user_id=${uid}    restaurant_id=${rid}    dishes=${list}
    ${o}=    POST On Session    foodie    /api/v1/orders    json=${order}
    ${oid}=    Get From Dictionary    ${o.json()}    id
    ${rating}=    Create Dictionary    order_id=${oid}    rating=${5}    comment=Good
    ${response}=    POST On Session    foodie    /api/v1/ratings    json=${rating}
    Status Should Be    201    ${response}

View Orders By User API
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${response}
