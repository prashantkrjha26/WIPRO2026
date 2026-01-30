*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=tutorialsninja.xlsx    sheet_name=Sheet1
Test Template    TutorialsNinja Login With Excel
Test Setup    Open TutorialsNinja
Test Teardown    Close TutorialsNinja Browser

*** Variables ***
${URL}        https://tutorialsninja.com/demo/index.php?route=account/login
${BROWSER}    edge

*** Keywords ***
Open TutorialsNinja
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=input-email    20s

TutorialsNinja Login With Excel
    [Arguments]    ${username}    ${password}

    Input Text    id=input-email       ${username}
    Input Text    id=input-password    ${password}
    Capture Page Screenshot    TC008_tutorialsninja_before_login_${username}.png
    Click Button    xpath=//input[@value='Login']

    Wait Until Element Is Visible    xpath=//h2[text()='My Account']    15s
    Capture Page Screenshot    TC008_tutorialsninja_after_login_${username}.png

    Click Element    xpath=//a[@title='My Account']
    Wait Until Element Is Visible    xpath=//a[text()='Logout']    10s
    Click Element    xpath=//a[text()='Logout']

Close TutorialsNinja Browser
    Close Browser

*** Test Cases ***
TC008_DataDriver_TutorialsNinja
    ${username}    ${password}
