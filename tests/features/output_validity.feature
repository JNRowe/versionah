@execute
Feature: Output validity
    In order to catch template errors
    As a developer
    We'll implement output validity checks

    Scenario Outline: Output validity
        Given I have the version <version>
        When I process <file> with <linter>
        Then the linter returns 0

        Examples:
            | version | file       | linter        |
            |   1.0.1 | test_wr.c  | splint        |
            |   1.0.1 | test_wr.m4 | m4 -P -E -E   |
            |   1.0.1 | test_wr.py | python -W all |
            |   1.0.1 | test_wr.rb | ruby -c       |
