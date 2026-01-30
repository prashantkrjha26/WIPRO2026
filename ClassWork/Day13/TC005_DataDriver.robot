*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    edge
${username}   Admin
${password}   admin123

*** Keywords ***
open orangehrm
     Open Browser    ${url}    ${browser}
     Maximize Browser Window

orangehrmlogin
     [Arguments]    ${username}    ${password}
     Wait Until Element Is Visible    name=username    10s
     Input Text    name=username    ${username}
     Input Text    name=password    ${password}
     Capture Page Screenshot    before_login_TCOO5_DataDriver.png
     Click Button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
     Wait Until Element Is Visible        xpath=//div[contains(@class,'orangehrm-dashboard-widget')]    20s
     Wait Until Element Is Not Visible    xpath=//div[contains(@class,'oxd-loading-spinner')]    20s
     Capture Page Screenshot    after_login_TC005_DataDriver.png
     Close Browser


*** Test Cases ***
TC005_DataDriver
    open orangehrm
    orangehrmlogin    Admin    admin123
