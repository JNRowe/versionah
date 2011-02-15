Feature: Read version
  In order to maintain a version file
  As a user
  We'll implement reading

  Scenario Outline: Read version
    Given I have the file <name>
    When I read its content
    Then I see the version <result>

  Examples:
    | name   | result |
    | test_a |  0.1.0 |
    | test_b |  1.0.0 |
    | test_c |  2.1.3 |
