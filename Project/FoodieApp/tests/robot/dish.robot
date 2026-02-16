*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Add Dish
    Create Session    foodie    ${BASE_URL}

    ${restaurant}=    Create Dictionary
    ...    name=DishRestA
    ...    category=Indian
    ...    location=Delhi
    ...    images=img
    ...    contact=123

    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${restaurant}
    ${rdata}=    Set Variable    ${r.json()}
    ${rid}=    Get From Dictionary    ${rdata}    id

    ${dish}=    Create Dictionary
    ...    name=Paneer
    ...    type=Veg
    ...    price=${200}
    ...    available_time=Lunch
    ...    image=img.jpg

    ${response}=    POST On Session    foodie    /api/v1/restaurants/${rid}/dishes    json=${dish}
    Status Should Be    201    ${response}


Update Dish
    Create Session    foodie    ${BASE_URL}

    ${restaurant}=    Create Dictionary
    ...    name=DishRestB
    ...    category=Indian
    ...    location=Mumbai
    ...    images=img
    ...    contact=456

    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${restaurant}
    ${rid}=    Get From Dictionary    ${r.json()}    id

    ${dish}=    Create Dictionary
    ...    name=Dosa
    ...    type=Veg
    ...    price=${100}
    ...    available_time=Breakfast
    ...    image=img.jpg

    ${d}=    POST On Session    foodie    /api/v1/restaurants/${rid}/dishes    json=${dish}
    ${did}=    Get From Dictionary    ${d.json()}    id

    ${update}=    Create Dictionary
    ...    price=${150}

    ${response}=    PUT On Session    foodie    /api/v1/dishes/${did}    json=${update}
    Status Should Be    200    ${response}


Enable Disable Dish
    Create Session    foodie    ${BASE_URL}

    ${restaurant}=    Create Dictionary
    ...    name=DishRestC
    ...    category=Indian
    ...    location=Delhi
    ...    images=img
    ...    contact=789

    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${restaurant}
    ${rid}=    Get From Dictionary    ${r.json()}    id

    ${dish}=    Create Dictionary
    ...    name=Idli
    ...    type=Veg
    ...    price=${80}
    ...    available_time=Breakfast
    ...    image=img.jpg

    ${d}=    POST On Session    foodie    /api/v1/restaurants/${rid}/dishes    json=${dish}
    ${did}=    Get From Dictionary    ${d.json()}    id

    ${status}=    Create Dictionary
    ...    enabled=${False}

    ${response}=    PUT On Session    foodie    /api/v1/dishes/${did}/status    json=${status}
    Status Should Be    200    ${response}


Delete Dish
    Create Session    foodie    ${BASE_URL}

    ${restaurant}=    Create Dictionary
    ...    name=DishRestD
    ...    category=Indian
    ...    location=Chennai
    ...    images=img
    ...    contact=999

    ${r}=    POST On Session    foodie    /api/v1/restaurants    json=${restaurant}
    ${rid}=    Get From Dictionary    ${r.json()}    id

    ${dish}=    Create Dictionary
    ...    name=Vada
    ...    type=Veg
    ...    price=${60}
    ...    available_time=Evening
    ...    image=img.jpg

    ${d}=    POST On Session    foodie    /api/v1/restaurants/${rid}/dishes    json=${dish}
    ${did}=    Get From Dictionary    ${d.json()}    id

    ${response}=    DELETE On Session    foodie    /api/v1/dishes/${did}
    Status Should Be    200    ${response}
