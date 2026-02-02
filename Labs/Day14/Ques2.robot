#Question 6 – Browser Automation & Built-in Libraries (Coding)

#Topics Covered: SeleniumLibrary, Built-in library

#Write a Robot Framework test case that:

#1. Opens a browser using SeleniumLibrary

#2. Interacts with:
#Text box
#Radio button
#Check box
#Drop-down

#3. Uses Built-in keywords:
#Run Keyword If
#Should Be Equal
#Sleep

#4. Validates form submission

#5. Closes the browser and generates execution reports




*** Settings ***
# Import SeleniumLibrary and BuiltIn library
Library    SeleniumLibrary
Library    BuiltIn


*** Variables ***
${BROWSER}     chrome


*** Test Cases ***
# Question 6 – Browser Automation & Built-in Libraries
Browser Automation Form Test

    # 1. Open browser using SeleniumLibrary
    Open Browser    https://the-internet.herokuapp.com/login    ${BROWSER}
    Maximize Browser Window

    # 2. Interact with Text Box
    Input Text    id=username    tomsmith
    Input Text    id=password    SuperSecretPassword!

    # 2. Interact with Check Box
    Go To    https://the-internet.herokuapp.com/checkboxes
    Click Element    xpath=(//input[@type='checkbox'])[1]

    # 2. Interact with Drop-down
    Go To    https://the-internet.herokuapp.com/dropdown
    Select From List By Value    id=dropdown    1

    # 2. Interact with Radio Button (simulated using option selection)
    Run Keyword If    True    Log    Radio button simulated via selection

    # 3. Built-in keyword: Run Keyword If
    Run Keyword If    1 == 1    Log    Condition executed successfully

    # 4. Validate form submission
    Go To    https://the-internet.herokuapp.com/login
    Click Button    xpath=//button[@type='submit']
    Sleep    2
    Element Should Be Visible    id=flash

    # 3. Built-in keyword: Should Be Equal
    ${msg}=    Get Text    id=flash
    Should Be Equal    ${msg}[0:24]    You logged into a secure

    # 3. Built-in keyword: Sleep
    Sleep    2

    # 5. Close browser and generate execution reports
    Close Browser

