Feature: Guess file type
    In order to pick a default file type
    As a user
    We'll implement file name checking

    Scenario Outline: Type from file name
        Given I have the file <name>
        When I pass it to process_command_line
        Then I see the file type <type>

        Examples:
            | name    | type |
            | test.py | py   |
            | test.rb | rb   |
            | test    | text |

    Scenario Outline: Override type guessing
        Given I have the file <name>
        When I pass type argument <argument> to process_command_line
        Then I see the file type <type>

        Examples:
            | name    | argument | type |
            | test.py | py       | py   |
            | test.rb | text     | text |
            | test    | c        | c    |
