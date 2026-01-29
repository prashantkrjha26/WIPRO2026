*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    edge
${username}   Admin
${password}   admin123

*** Test Cases ***
TC003_Login_Edge
    Open Browser    ${url}    ${browser}
    Wait Until Element Is Visible    name=username    90s
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
    Close Browser
