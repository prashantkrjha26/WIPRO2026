*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***

Create New User
    Create Session    api    ${BASE_URL}
    ${data}=    Create Dictionary    name=varsha
    ${response}=    POST On Session    api    /users    json=${data}
    Status Should Be    201    ${response}
    Log    ${response.json()}    console=True


Update User Using PUT
    Create Session    api    ${BASE_URL}
    ${data}=    Create Dictionary    name=Pooja
    ${response}=    PUT On Session    api    /users/2    json=${data}
    Status Should Be    200    ${response}
    Log    ${response.json()}    console=True


Patch User Using PATCH
    Create Session    api    ${BASE_URL}
    ${data}=    Create Dictionary    name=Pooja patched
    ${response}=    PATCH On Session    api    /users/2    json=${data}
    Status Should Be    200    ${response}
    Log    ${response.json()}    console=True


Verify Get All Users
    Create Session    api    ${BASE_URL}
    ${response}=    GET On Session    api    /users
    Status Should Be    200    ${response}
    Log    ${response.json()}    console=True


Verify Get Single User
    Create Session    api    ${BASE_URL}
    ${response}=    GET On Session    api    /users/2
    Status Should Be    200    ${response}
    Log    ${response.json()}    console=True


Verify Get Single User Not Found
    Create Session    api    ${BASE_URL}
    ${response}=    GET On Session    api    /users/99999    expected_status=404
    Status Should Be    404    ${response}
    Log    ${response.json()}    console=True


Verify Delete User By UserId
    Create Session    api    ${BASE_URL}
    ${response}=    DELETE On Session    api    /users/2
    Status Should Be    200    ${response}
    Log    ${response.json()}    console=True

    ${response}=    GET On Session    api    /users/2    expected_status=404
    Status Should Be    404    ${response}



Verify Get All User Again
    Create Session    api    ${BASE_URL}
    ${response}=    GET On Session    api    /users
    Status Should Be    200    ${response}
    Log    ${response.json()}    console=True