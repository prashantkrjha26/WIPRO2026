*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Place Order - Success
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary
    ...    user_id=1
    ...    restaurant_id=1
    ...    dishes=${[1]}
    ${response}=    POST On Session    foodie    /api/v1/orders    json=${body}
    Status Should Be    201    ${response}

View Orders By Restaurant
    ${response}=    GET On Session    foodie    /api/v1/restaurants/1/orders
    Status Should Be    200    ${response}

View Orders By User
    ${response}=    GET On Session    foodie    /api/v1/users/1/orders
    Status Should Be    200    ${response}
