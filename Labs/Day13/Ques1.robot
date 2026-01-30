#Question 3 – Writing a Simple Test Case Using RIDE (Coding)

#Topics Covered: RIDE, Simple test case

#Using RIDE, create a Robot Framework test case that:

#1. Opens a browser

#2. Navigates to a given URL

#3. Verifies the page title

#4. Captures a screenshot

#5. Closes the browser

#(Export and run the generated .robot file from command line)

*** Settings ***
Library    SeleniumLibrary
# SeleniumLibrary is used to perform browser automation

*** Variables ***
${URL}        https://www.google.com
${BROWSER}    edge
${TITLE}      Google

*** Test Cases ***
Simple Test Case Using RIDE
    # 1. Opens a browser
    Open Browser    ${URL}    ${BROWSER}

    # Maximizes the browser window
    Maximize Browser Window

    # 2. Navigates to a given URL
    # (URL is already opened using Open Browser keyword)

    # 3. Verifies the page title
    Title Should Be    ${TITLE}

    # 4. Captures a screenshot
    Capture Page Screenshot    Ques1_screenshot.png

    # 5. Closes the browser
    Close Browser
