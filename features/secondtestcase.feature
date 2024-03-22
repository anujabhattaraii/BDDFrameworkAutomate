Feature: Validation on login page
    Background : 
        Given Opening browser
    @smoke
    Scenario: verifying login page with valid username and password
        When Provide valid "mercury" and "mercury"
        Then Verify title of the page 

        @regression
        Scenario Outline:
            When Provide valid "<userName>" and "<password>"
            Then Verify success message 
            Examples:
            |userName | password|
            |mercury  | mercury |
            |aafas    | aDAFSA  |

