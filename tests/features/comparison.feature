Feature: Compare versions
  In order to compare versions
  As a user
  We'll implement comparison operators

  Scenario Outline: Equal versions
    Given I have the versions <version1> and <version2>
    When I compare them for equality
    Then I see the comparison <result>

  Examples:
    | version1 | version2 | result |
    |    0.1.0 |    0.1.0 | True   |
    |    1.0.0 |    1.0.0 | True   |
    |    1.0.0 |    2.0.0 | False  |
    |    2.1.3 |    3.0.0 | False  |

  Scenario Outline: Version ordering
    Given I have the versions <version1> and <version2>
    When I search for the greatest
    Then I see the version <result>

  Examples:
    | version1 | version2 | result |
    |    2.1.1 |    2.1.4 |  2.1.4 |
    |    2.1.3 |    3.0.0 |  3.0.0 |
    |    3.0.0 | 2.9.99.9 |  3.0.0 |

  Scenario Outline: Version equivalence
    Given I have the versions <version1> and <version2>
    When I compare them for equality
    Then I see the comparison <result>

  Examples:
    | version1 | version2 | result |
    |    0.1.0 |      0.1 | True   |
    |      0.1 |    0.1.0 | True   |
    |  0.1.0.0 |    0.1.0 | True   |
    |  0.1.0.0 |      0.1 | True   |
    |      0.1 |  0.1.0.1 | False  |
    |  0.1.1.1 |    0.1.1 | False  |
