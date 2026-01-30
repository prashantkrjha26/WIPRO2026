*** Settings **
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    orangehrmlogin
Suite Setup    open orangehrm
Suite Teardown    close orangehrm

Resource    TC006_DataDriver_Excel.robot

*** Variables ***
${url}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    edge


*** Keywords ***
open orangehrm
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

orangehrmlogin
    [Arguments]    ${username}    ${password}
    Wait Until Element Is Visible    name=username    10s
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Capture Page Screenshot    before_login_TC006_DataDriver_Excel.png
    Click Button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
    Wait Until Element Is Visible        xpath=//div[contains(@class,'orangehrm-dashboard-widget')]    20s
    Wait Until Element Is Not Visible    xpath=//div[contains(@class,'oxd-loading-spinner')]    20s
    Capture Page Screenshot    after_login_TC006_DataDriver_Excel.png

close orangehrm
    Close Browser


*** Test Cases ***
TC006_DataDriver_Excel
    ${username}    ${password}
