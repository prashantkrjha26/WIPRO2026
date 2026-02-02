*** Test Cases ***
Print Names
    FOR    ${name}    IN    Ram    Ravi    Taj
        Log To Console    ${name}
    END

Print Names Using While Loop
    ${count}    Set Variable    1
    WHILE    ${count}<=5
        Log To Console    ${count}
        ${count}    Evaluate    ${count} + 1
    END


#1️⃣ IF condition (basic)
*** Test Cases ***
IF Condition Example
    ${age}=    Set Variable    20
    IF    ${age} >= 18
        Log    Eligible to vote
    END


#2️⃣ IF – ELSE
*** Test Cases ***
IF ELSE Example
    ${num}=    Set Variable    5
    IF    ${num} > 10
        Log    Greater than 10
    ELSE
        Log    Less than or equal to 10
    END


#3️⃣ IF – ELSE IF – ELSE
*** Test Cases ***
IF ELSE IF Example
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log    Grade A
    ELSE IF    ${marks} >= 75
        Log    Grade B
    ELSE
        Log    Grade C
    END


#4️⃣ Inline IF (short condition)
*** Test Cases ***
Inline IF Example
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'    Log    Test Passed


#🔁 LOOP STATEMENTS IN ROBOT FRAMEWORK

#5️⃣ FOR loop (basic list)
*** Test Cases ***
FOR Loop Basic
    FOR    ${item}    IN    one    two    three
        Log    Item: ${item}
    END


#6️⃣ FOR loop with list variable
*** Variables ***
@{COLORS}    Red    Green    Blue

*** Test Cases ***
FOR Loop With List
    FOR    ${color}    IN    @{COLORS}
        Log    Color: ${color}
    END


#7️⃣ FOR loop – IN RANGE
*** Test Cases ***
FOR Loop Range
    FOR    ${i}    IN RANGE    1    6
        Log    Number: ${i}
    END


#8️⃣ FOR loop – with step
*** Test Cases ***
FOR Loop With Step
    FOR    ${i}    IN RANGE    0    10    2
        Log    Value: ${i}
    END


#9️⃣ FOR loop – ENUMERATE
*** Test Cases ***
FOR Loop Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log    ${index} = ${value}
    END


#🔟 FOR loop – ZIP (multiple lists)
*** Variables ***
| @{USERS} | admin | user |
| @{PWDS}  | admin123 | user123 |

*** Test Cases ***
FOR Loop Zip
    FOR    ${u}    ${p}    IN ZIP    @{USERS}    @{PWDS}
        Log    ${u} / ${p}
    END


#1️⃣1️⃣ Nested FOR loop
*** Test Cases ***
Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log    i=${i}, j=${j}
        END
    END


#1️⃣2️⃣ FOR loop with IF condition
*** Test Cases ***
FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log    Found 3
        END
    END


#1️⃣3️⃣ BREAK (exit loop)
*** Test Cases ***
BREAK Example
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log    ${i}
    END


#1️⃣4️⃣ CONTINUE (skip iteration)
*** Test Cases ***
CONTINUE Example
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log    ${i}
    END

#1️⃣5️⃣ WHILE loop (Robot Framework 4+)
*** Test Cases ***
WHILE Loop Example
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END

#1️⃣6️⃣ WHILE with BREAK
*** Test Cases ***
WHILE Loop With BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log    ${i}
        ${i}=    Evaluate    ${i} + 1
    END


#⚠️ ERROR HANDLING (Control Structure)
#1️⃣7️⃣ TRY / EXCEPT / FINALLY
*** Test Cases ***
Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log    Error handled
    FINALLY
        Log    Always executed
    END


#🔁 CONDITIONAL KEYWORD EXECUTION
#1️⃣8️⃣ Run Keyword If
*** Test Cases ***
Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log    Test Passed


#1️⃣9️⃣ Run Keyword Unless
*** Test Cases ***
Run Keyword Unless Example
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log    Test Failed





