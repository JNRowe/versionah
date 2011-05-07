Feature: Shtool import
    In order to import from shtool
    As a user
    We'll implement shtool importing

    Scenario Outline: Reading shtool output
        Given I have the file <name>
        When I read its content
        Then I see the version <result>

        Examples:
            | name               | result |
            | shtool/test.c      |  1.2.3 |
            | shtool/test.m4     |  1.2.3 |
            | shtool/test.perl   |  1.2.3 |
            | shtool/test.python |  1.2.3 |
            | shtool/test.txt    |  1.2.3 |
