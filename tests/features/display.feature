Feature: Display version
  In order to query a version
  As a user
  We'll implement displaying

  Scenario Outline: Dotted
    Given I have the version <version>
    When I display its dotted representation
    Then I see the string <result>

  Examples:
    | version | result |
    |   0.1.0 |  0.1.0 |
    |   1.0.0 |  1.0.0 |
    |   2.1.3 |  2.1.3 |

  Scenario Outline: Hex
    Given I have the version <version>
    When I display its hex representation
    Then I see the string <result>

  Examples:
    | version |   result |
    |   0.1.0 | 0x000100 |
    |   1.0.0 | 0x010000 |
    |   2.1.3 | 0x020103 |

  Scenario Outline: Libtool
    Given I have the version <version>
    When I display its libtool representation
    Then I see the string <result>

  Examples:
    | version | result |
    |   0.1.0 |   1:20 |
    |   1.0.0 |  10:20 |
    |   2.1.3 |  21:23 |
