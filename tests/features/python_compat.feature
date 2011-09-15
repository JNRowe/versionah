Feature: Python version compatibility
  In order to maintain Python version files
  As a user
  We'll want multiple version compatibility

  Scenario Outline: Read version
    Given I have the version <version>
    When I process <file> with <interpreter>
    Then the interpreter returns 0

  Examples:
    | version | file       | interpreter      |
    |   1.0.1 | test_wr.py | python2.4 -W all |
    |   1.0.1 | test_wr.py | python2.5 -W all |
    |   1.0.1 | test_wr.py | python2.6 -W all |
    |   1.0.1 | test_wr.py | python2.7 -W all |
    |   1.0.1 | test_wr.py | python3.1 -W all |
    |   1.0.1 | test_wr.py | python3.2 -W all |
