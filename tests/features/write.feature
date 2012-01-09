@write
Feature: Write version
    In order to maintain a version file
    As a user
    We'll implement writing

    Scenario Outline: Write version
        Given I have the version <version>
        When I write its value to <file>
        Then I see the version <result>

        Examples:
            | version | file      | result |
            |   0.1.0 | test_wr_a |  0.1.0 |
            |   1.0.0 | test_wr_b |  1.0.0 |
            |   2.1.3 | test_wr_c |  2.1.3 |
