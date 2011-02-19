Feature: Valid version
  In order to catch version errors
  As a user
  We'll implement validity checks

  Scenario: Version with one component
    Given I have the invalid version 1
    Then I receive ValueError

  Scenario: Version with five components
    Given I have the invalid version 1.2.3.4.5
    Then I receive ValueError

  Scenario: Version with negative component
    Given I have the invalid version 1.2.-1.0
    Then I receive ValueError
