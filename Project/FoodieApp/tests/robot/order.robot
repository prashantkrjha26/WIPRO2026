*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
View Orders By Restaurant
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${response}

View Orders By User
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${response}
