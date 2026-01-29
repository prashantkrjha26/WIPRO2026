*** Settings ***
Library          SeleniumLibrary

*** Keywords  ***
open application

     Open Browser   https://www.google.com/     chrome
     Maximize Browser Window


*** Test Cases ***
TC002_Keywords.robot

      open application
      Title Should Be   Google
      Close Browser
