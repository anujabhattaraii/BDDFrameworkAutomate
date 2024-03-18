Feature: login functionality

    Scenario: Valid user name and password
        Given open browser
        When providing valid username and password
        Then Verifying home 