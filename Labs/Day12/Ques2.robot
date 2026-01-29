#Question 2 – Environment Setup Verification (Coding)

#Write a Robot Framework test case that:

#1. Verifies Python installation

#2. Verifies Robot Framework installation

#3. Imports SeleniumLibrary

#4. Prints the Robot Framework version

#5. Fails gracefully with meaningful logs if any dependency is missing



# Ques2.robot

# Question 2 – Environment Setup Verification (Coding)

# Ques2.robot

# Question 2 – Environment Setup Verification (Coding)

*** Settings ***
# 3. Imports SeleniumLibrary
Library    SeleniumLibrary
Library    BuiltIn
Library    Process

*** Test Cases ***
Environment_Setup_Verification

    # 1. Verifies Python installation
    ${python_result}=    Run Process    python    --version    stdout=PIPE    stderr=PIPE
    Run Keyword If    ${python_result.rc} != 0    Fail    Python is not installed
    Log To Console    Python Version: ${python_result.stdout}${python_result.stderr}

    # 2. Verifies Robot Framework installation
    ${robot_result}=    Run Process    python    -m    robot    --version    stdout=PIPE    stderr=PIPE
    Run Keyword If    ${robot_result.rc} != 0    Fail    Robot Framework is not installed

    # 4. Prints the Robot Framework version
    Log To Console    Robot Framework Version: ${robot_result.stdout}${robot_result.stderr}
    Log    ${robot_result.stdout}${robot_result.stderr}

    # 5. Fails gracefully with meaningful logs if any dependency is missing
    Log To Console    Environment verification completed successfully
