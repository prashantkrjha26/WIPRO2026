*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Approve Restaurant
    Create Session    foodie    ${BASE_URL}
    ${restaurant}=    Create Dictionary    name=AdminRest    category=Indian    location=Delhi    images=img    contact=1
    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${restaurant}
    ${rid}=    Get From Dictionary    ${r.json()}    id
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/${rid}/approve
    Status Should Be    200    ${response}

Admin Disable Restaurant
    Create Session    foodie    ${BASE_URL}
    ${restaurant}=    Create Dictionary    name=AdminRest2    category=Indian    location=Delhi    images=img    contact=1
    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${restaurant}
    ${rid}=    Get From Dictionary    ${r.json()}    id
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/${rid}/disable
    Status Should Be    200    ${response}

View Customer Feedback
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /api/v1/admin/feedback
    Status Should Be    200    ${response}

View Order Status
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${response}
