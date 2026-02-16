*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Add Dish - Success
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary
    ...    name=Paneer
    ...    type=Veg
    ...    price=200
    ...    available_time=Lunch
    ...    image=img.jpg
    ${response}=    POST On Session    foodie    /api/v1/restaurants/1/dishes    json=${body}
    Status Should Be    201    ${response}

Update Dish - Success
    ${update}=    Create Dictionary    price=250
    ${response}=    PUT On Session    foodie    /api/v1/dishes/1    json=${update}
    Status Should Be    200    ${response}

Update Dish Status
    ${status}=    Create Dictionary    enabled=${False}
    ${response}=    PUT On Session    foodie    /api/v1/dishes/1/status    json=${status}
    Status Should Be    200    ${response}

Delete Dish
    ${response}=    DELETE On Session    foodie    /api/v1/dishes/1
    Status Should Be    200    ${response}
