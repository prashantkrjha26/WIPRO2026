#Question 5 – Command Line Execution, Setup & Teardown (Coding)


#Topics Covered: Command line, Setup & Teardown

#Write a Robot Framework test suite that:

#1. Uses Suite Setup and Suite Teardown

#2. Uses Test Setup and Test Teardown

#3. Executes from the command line using:
#Tags
#Output directory

#4. Generates log.html and report.html

#5. Includes at least one tagged test case





*** Settings ***
# Part 1: Suite Setup and Suite Teardown
Suite Setup       Suite Level Setup
Suite Teardown    Suite Level Teardown

# Part 2: Test Setup and Test Teardown
Test Setup        Test Level Setup
Test Teardown     Test Level Teardown

Library           BuiltIn


*** Variables ***
${APP_NAME}       Robot Framework Demo


*** Keywords ***
Suite Level Setup
    Log    Suite setup executed

Suite Level Teardown
    Log    Suite teardown executed

Test Level Setup
    Log    Test setup executed

Test Level Teardown
    Log    Test teardown executed


*** Test Cases ***
# Part 5: Tagged test case
Sample Tagged Test
    [Tags]    smoke
    Log    Running tagged test for ${APP_NAME}
    Should Be Equal    ${APP_NAME}    Robot Framework Demo

Another Test Case
    Log    Running untagged test
    Should Be True    ${True}


# Part 3 & Part 4: Command line execution with tags, output directory, log and report
# robot -d results -i smoke Ques1.robot
