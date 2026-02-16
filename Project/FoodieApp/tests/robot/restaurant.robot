*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Register Restaurant - Success
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary
    ...    name=Food Hub
    ...    category=Indian
    ...    location=Delhi
    ...    images=image.jpg
    ...    contact=9999999999
    ${response}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    Status Should Be    201    ${response}

Register Restaurant - Duplicate
    ${body}=    Create Dictionary
    ...    name=Food Hub
    ...    category=Indian
    ...    location=Delhi
    ...    images=image.jpg
    ...    contact=9999999999
    ${response}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    Status Should Be    409    ${response}

View Restaurant - Success
    ${response}=    GET On Session    foodie    /api/v1/restaurants/1
    Status Should Be    200    ${response}

Update Restaurant - Success
    ${update}=    Create Dictionary    name=Food Hub Updated
    ${response}=    PUT On Session    foodie    /api/v1/restaurants/1    json=${update}
    Status Should Be    200    ${response}

Disable Restaurant - Success
    ${response}=    PUT On Session    foodie    /api/v1/restaurants/1/disable
    Status Should Be    200    ${response}

Search Restaurant
    ${response}=    GET On Session    foodie    /api/v1/restaurants/search?name=Food
    Status Should Be    200    ${response}
