*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Register Restaurant
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary
    ...    name=RestA
    ...    category=Indian
    ...    location=Delhi
    ...    images=img.jpg
    ...    contact=1111
    ${response}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    Status Should Be    201    ${response}

Update Restaurant
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary    name=RestB    category=Indian    location=Mumbai    images=img.jpg    contact=2222
    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    ${rid}=    Get From Dictionary    ${r.json()}    id
    ${update}=    Create Dictionary    name=RestBUpdated
    ${response}=    PUT On Session    foodie    /api/v1/restaurants/${rid}    json=${update}
    Status Should Be    200    ${response}

Disable Restaurant
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary    name=RestC    category=Indian    location=Delhi    images=img.jpg    contact=3333
    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    ${rid}=    Get From Dictionary    ${r.json()}    id
    ${response}=    PUT On Session    foodie    /api/v1/restaurants/${rid}/disable
    Status Should Be    200    ${response}

View Restaurant
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary    name=RestD    category=Indian    location=Delhi    images=img.jpg    contact=4444
    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    ${rid}=    Get From Dictionary    ${r.json()}    id
    ${response}=    GET On Session    foodie    /api/v1/restaurants/${rid}
    Status Should Be    200    ${response}

Search Restaurants
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary    name=SearchRest    category=Indian    location=Delhi    images=img.jpg    contact=5555
    POST On Session    foodie    /api/v1/restaurants    json=${body}
    ${response}=    GET On Session    foodie    /api/v1/restaurants/search    params=name=SearchRest
    Status Should Be    200    ${response}
