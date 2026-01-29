*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    edge
${username}   Admin
${password}   admin123

*** Test Cases ***
TC004_Login_Edge
    Open Browser    ${url}    ${browser}
    Wait Until Element Is Visible    name=username    60s

    Input Text    name=username    ${username}
    Input Text    name=password    ${password}

    Capture Page Screenshot    before_login.png

    Click Button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button

    Wait Until Page Contains Element    xpath=//*[@id="app"]    60s
    Capture Page Screenshot    after_login.png

    Close Browser
