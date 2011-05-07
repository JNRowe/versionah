Feature: Compare versions with foreign objects
    In order to compare versions
    As a user
    We'll implement comparison operators against foreign objects

    Scenario Outline: Tuple comparison
        Given I have the Version object for <version1> and tuple <version2>
        When I compare them for equality
        Then I see the comparison <result>

        Examples:
            | version1 | version2 | result |
            |    0.1.0 |    0.1.0 | True   |
            |    1.0.0 |    1.0.0 | True   |
            |    1.0.0 |    2.0.0 | False  |
            |    2.1.3 |    3.0.0 | False  |

    Scenario Outline: String comparison
        Given I have the Version object for <version1> and string <version2>
        When I compare them for equality
        Then I see the comparison <result>

        Examples:
            | version1 | version2 | result |
            |    0.1.0 |    0.1.0 | True   |
            |    1.0.0 |    1.0.0 | True   |
            |    1.0.0 |    2.0.0 | False  |
            |    2.1.3 |    3.0.0 | False  |

    Scenario Outline: List comparison
        Given I have the Version object for <version1> and list <version2>
        When I compare them for equality
        Then I see the comparison <result>

        Examples:
            | version1 | version2 | result |
            |    0.1.0 |    0.1.0 | True   |
            |    1.0.0 |    1.0.0 | True   |
            |    1.0.0 |    2.0.0 | False  |
            |    2.1.3 |    3.0.0 | False  |

    Scenario: Unsupported object comparison
        Given I have the Version object for 0.2.0 and RegExp matcher for 0.2.0
        When I compare them for equality
        Then I receive NotImplementedError
