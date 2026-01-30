#Question 4 – Keyword-Driven & Data-Driven Test Cases (Coding)


#Topics Covered: Keyword-driven & Data-driven testing

#Create a Robot Framework test suite that:

#1. Defines custom user keywords

#2. Implements keyword-driven testing

#3. Implements data-driven testing using:



#Test Template

#External CSV file

#4. Executes test cases for multiple data sets

#5. Reports pass/fail status for each data row



*** Settings ***

# Question 4 – Keyword-Driven & Data-Driven Test Cases
# Topics: Keyword-Driven & Data-Driven Testing


Library    SeleniumLibrary
Library    DataDriver    file=Ques2.xlsx    sheet_name=Sheet1
Test Template    Login Test Using Keywords
Suite Setup    Open Application
Suite Teardown    Close Browser


*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    edge


*** Test Cases ***

# Part 4:
# Executes test cases for multiple data sets
# Data comes from external excel file

Login with multiple users using Excel


*** Keywords ***

# Part 1:
# Custom user keywords


Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s


Input Username
    [Arguments]    ${username}
    Input Text    name=username    ${username}


Input Password
    [Arguments]    ${password}
    Input Text    name=password    ${password}


Click Login
    Click Button    xpath=//button[@type='submit']


Verify Login Result
    [Arguments]    ${expected}
    Run Keyword If    '${expected}' == 'PASS'
    ...    Wait Until Element Is Visible    xpath=//h6[text()='Dashboard']    10s
    ...    ELSE
    ...    Page Should Contain Element    xpath=//p[contains(@class,'oxd-alert-content-text')]


Logout Application
    Run Keyword And Ignore Error
    ...    Click Element    xpath=//span[@class='oxd-userdropdown-tab']
    Run Keyword And Ignore Error
    ...    Click Element    xpath=//a[text()='Logout']
    Wait Until Element Is Visible    name=username    10s



# Part 2 & 3:
# Keyword-Driven + Data-Driven testing
# Using Test Template and External CSV

Login Test Using Keywords
    [Arguments]    ${username}    ${password}    ${expected}
    Input Username    ${username}
    Input Password    ${password}
    Click Login
    Verify Login Result    ${expected}
    Logout Application
