Feature: Bump version
  In order to bump a version
  As a user
  We'll implement bumping

  Scenario Outline: Major bumps
    Given I have the version <version>
    When I bump its major version
    Then I see the version <result>

  Examples:
    | version | result |
    |   0.1.0 |  1.0.0 |
    |   1.0.0 |  2.0.0 |
    |   2.1.3 |  3.0.0 |

  Scenario Outline: Minor bumps
    Given I have the version <version>
    When I bump its minor version
    Then I see the version <result>

  Examples:
    | version | result |
    |   0.1.0 |  0.2.0 |
    |   1.0.0 |  1.1.0 |
    |   2.1.3 |  2.2.0 |

  Scenario Outline: Micro bumps
    Given I have the version <version>
    When I bump its micro version
    Then I see the version <result>

  Examples:
    | version | result |
    |   0.1.0 |  0.1.1 |
    |   1.0.0 |  1.0.1 |
    |   2.1.3 |  2.1.4 |
