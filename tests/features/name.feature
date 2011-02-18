Feature: Version names
  In order to associate versions
  As a user
  We'll implement package names for versions

  Scenario Outline: Name version
    Given I have the package <pkg> version <version>
    When I display its string representation
    Then I see the string <result>

  Examples:
    | pkg  | version | result      |
    | cat  |   0.1.0 | cat v0.1.0  |
    | dog  |   1.0.0 | dog v1.0.0  |
    | fish |   2.1.3 | fish v2.1.3 |

  Scenario Outline: Names with dashes and underscores
    Given I have the package <pkg> version <version>
    When I display its string representation
    Then I see the string <result>

  Examples:
    | pkg         | version | result             |
    | cat-meow    |   0.1.0 | cat-meow v0.1.0    |
    | dog-bark    |   1.0.0 | dog-bark v1.0.0    |
    | fish-bubble |   2.1.3 | fish-bubble v2.1.3 |
