Feature: Check login page
Background : 
        Given Opening browser
Scenario: Testing table format
    When Verify login by using below query
     |userName | password|
     |mercury  | mercury |
    Then Verify title of the page 