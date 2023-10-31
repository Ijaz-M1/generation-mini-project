# generation-mini-project
Project Background

Client requirements

how to run the app
- Use the play/run button in VS code
- Otherwise in the terminal type 'py mini_project.py' on windows or 'python3 mini_project.py' on mac

how to run any unit tests
- First install pytest
- When this is done, type in the terminal "py -m pytest test_mini_project.py"
- This should then run 2 tests and successfully pass them

what do the unit tests do
- We start by looking at a function in our main file called produce_pretty_list.
- This function will return the list of dictionaries of products, couriers or orders (depending on which one is called) and print their index value with them.
- The first unit test takes in an expected code of the products list with its respective index value. We then have an actual value which also prints out the product list with indexes but through the function produce_pretty_list.
- We test equal actual to expected and the test should pass indicating that they produce the same thing.
- The second unit test does not take in any values for the list and is empty.
- From this, we assume that it would not print anything and the test should pass.


Project Reflections

How did your design go about meeting the project's requirements?
- I started by making a main loop which allowed me to choose between the product, courier or orders menu.
- Within each menu, i used if and elif statements to match what the user inputs.
- From this i was able to carry out the requirements under each if/elif statement and use break to end the loop.

How did you guarantee the project's requirements?
- I followed the pseudo code and checked over each line of it to make sure all the tasks were completed.
- I also asked the instructors when i did not understand a certain requirement and also demonstrated my code to check if there
were any mistakes.

If you had more time, what is one thing you would improve upon?
- One thing i would improve on is the use of more functions.
- I found that in my code, there were times where i was using the same code again but only changing one or two variables which
made my code look very long and hard to read.
- Therefore by adding more functions i would be able to shorten the length of my file while also making it more presentable.
This would also make it easier to do more unit testings.

What did you most enjoy implementing?
- I enjoyed reading/writing from/to csv files.
- This is because it allowed me to save data that was inputted throughout my code.
- It also gave an insight into how to manage data and keep them secure.