#Question 1 – Robot Framework Basics (Coding)

#Topics Covered: Introduction to Robot Framework

#Write a Robot Framework test suite (.robot file) that:
#1. Uses the BuiltIn library

#2. Contains at least two test cases

#3. Logs messages using Log and Log To Console

#4. Demonstrates the use of variables (scalar and list)

#5. Executes successfully using the robot command



*** Settings ***
# 1. Uses the BuiltIn library
Library    BuiltIn

*** Variables ***
# 4. Demonstrates the use of variables (scalar and list)
${name}        Robot Framework
@{numbers}     1    2    3

*** Test Cases ***
# 2. Contains at least two test cases
Log_Message
    # 3. Logs messages using Log and Log To Console
    Log    Hello ${name}
    Log To Console    Numbers list: ${numbers}

Second_Test
    Log    Second test case executed successfully
    Log To Console    Robot Framework execution done

# 5. Executes successfully using the robot command

# robot Ques1.robot

