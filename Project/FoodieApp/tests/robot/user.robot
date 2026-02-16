*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
User Registration - Success
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary
    ...    name=Prashant
    ...    email=test@mail.com
    ...    password=1234
    ${response}=    POST On Session    foodie    /api/v1/users/register    json=${body}
    Status Should Be    201    ${response}

User Registration - Duplicate
    ${body}=    Create Dictionary
    ...    name=Prashant
    ...    email=test@mail.com
    ...    password=1234
    ${response}=    POST On Session    foodie    /api/v1/users/register    json=${body}
    Status Should Be    409    ${response}
