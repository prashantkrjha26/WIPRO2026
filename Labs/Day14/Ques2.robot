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
Library    SeleniumLibrary

# Part 1: Opens a browser using SeleniumLibrary
Suite Setup     Open Test Browser

# Part 5: Closes the browser and generates execution reports
Suite Teardown  Close All Browsers


*** Variables ***
${URL}      https://testautomationpractice.blogspot.com/
${BROWSER}  edge


*** Test Cases ***
Form Automation Test

    # Part 2: Interacts with Text box
    Input Text    id=name      Prashant
    Input Text    id=email    prashantkumarjha1@gmail.com

    # Part 2: Interacts with Radio button
    Click Element    id=male

    # Part 2: Interacts with Check box
    Click Element    id=monday

    # Part 2: Interacts with Drop-down
    Select From List By Label    id=country    India

    # Part 3: Uses Built-in keyword Run Keyword If
    Run Keyword If    '${BROWSER}' == 'edge'    Log    Running test on Edge browser

    # Part 3: Uses Built-in keyword Sleep
    Sleep    2s

    # Part 4: Validates form submission
    ${selected}=    Get Selected List Label    id=country
    Should Be Equal    ${selected}    India

    Click Button    xpath=//button[text()='Submit']
    Sleep    2s


*** Keywords ***
Open Test Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
