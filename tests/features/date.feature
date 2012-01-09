@write
Feature: Version date
    In order to judge package freshness
    As a user
    We'll implement dates for versions

    Scenario Outline: Date version
        Given I have the version <version>
        When I write its value to <file>
        Then I find today's date

        Examples:
            | version | file      |
            |   0.1.0 | test_wr_a |
            |   1.0.0 | test_wr_b |
            |   2.1.3 | test_wr_c |
