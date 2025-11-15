*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  kissaistuupuussa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  aa  salasana12345
    Output Should Contain  Username has to be more than 2 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  666  salasana1234567890
    Output Should Contain  Username should only contain characters from a to z

Register With Valid Username And Too Short Password
    Input Credentials  maksalaatikko  asd
    Output Should Contain  Password has to be more than 7 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  maksalaatikko  asdasdasdasdasd
    Output Should Contain  Password can not only contain letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command