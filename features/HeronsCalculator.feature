Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

Scenario: I can calculate the area of a triangle
Given I open the url "https://byjus.com/herons-calculator/"
When I enter "3" in the text feild "a"
and I enter "4" in the text feild "b"
and I enter "3" in the text feild "c"
and I click on the button "clcbtn"
Then I should see "4.472" in "_d"

