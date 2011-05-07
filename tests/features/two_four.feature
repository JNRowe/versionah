Feature: Support two and four component versions
    In order to support two and four component versions
    As a user
    We'll implement variable component ranges

    Scenario Outline: Two component major bump
        Given I have the version <version>
        When I bump its major version
        Then I see the version <result>

        Examples:
            | version | result |
            |     0.1 |    1.0 |
            |     1.0 |    2.0 |
            |     2.1 |    3.0 |

    Scenario Outline: Two component minor bump
        Given I have the version <version>
        When I bump its minor version
        Then I see the version <result>

        Examples:
            | version | result |
            |     0.1 |    0.2 |
            |     1.0 |    1.1 |
            |     2.1 |    2.2 |

    Scenario Outline: Four component major bumps
        Given I have the version <version>
        When I bump its major version
        Then I see the version <result>

        Examples:
            | version |  result |
            | 0.1.0.0 | 1.0.0.0 |
            | 1.0.0.4 | 2.0.0.0 |
            | 2.1.3.0 | 3.0.0.0 |

    Scenario Outline: Four component minor bumps
        Given I have the version <version>
        When I bump its minor version
        Then I see the version <result>

        Examples:
            | version | result |
            |   0.1.0.0  |  0.2.0.0 |
            |   1.0.0.4 |  1.1.0.0  |
            |   2.1.3.0 |  2.2.0.0 |

    Scenario Outline: Four component micro bumps
        Given I have the version <version>
        When I bump its micro version
        Then I see the version <result>

        Examples:
            | version |  result |
            | 0.1.0.0 | 0.1.1.0 |
            | 1.0.0.4 | 1.0.1.0 |
            | 2.1.3.0 | 2.1.4.0 |

    Scenario Outline: Four component patch bumps
        Given I have the version <version>
        When I bump its patch version
        Then I see the version <result>

        Examples:
            | version |  result |
            | 0.1.0.0 | 0.1.0.1 |
            | 1.0.0.4 | 1.0.0.5 |
            | 2.1.3.0 | 2.1.3.1 |
