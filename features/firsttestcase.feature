Feature: login functionality
    Background : 
        Given Open browser
        Scenario: Valid user name and password
            When providing valid username and password
            Then Verifying home 