*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Approve Restaurant
    Create Session    foodie    ${BASE_URL}
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/approve
    Status Should Be    200    ${response}

Admin Disable Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/disable
    Status Should Be    200    ${response}

View Feedback
    ${response}=    GET On Session    foodie    /api/v1/admin/feedback
    Status Should Be    200    ${response}

View Orders
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${response}
