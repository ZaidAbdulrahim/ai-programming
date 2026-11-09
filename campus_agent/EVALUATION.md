# Agent Lab 4 - Evaluation

## Part 1: Automated Testing
We created the five automated tests instead of just opening the application and asking it questions because we wanted to make sure everything was working properly. The tests allowed us to check whether the program returned the correct information for different requests and handled situations where a resource could not be found. This helped us identify problems before relying on the application.

### Test Results and Reliability

After seeing all five tests pass, I believe the reliability of my Campus Resource Assistant has improved, but that does not mean the application is perfect or completely free of errors. I have still experienced server errors when trying to run the application. I understand that some problems are within my control to correct, while others may involve external servers or services that I do not manage.

The five passing tests give me more confidence that the resource lookup functions are working properly. However, there may still be other problems that the tests do not cover. My goal is to continue improving the parts of the application that I have control over, one step at a time.

### Summary of the Five Automated Tests

We created five automated tests to make sure the Campus Resource Assistant was working properly. The first test checked whether the application could find the library in its resources. The second test checked whether it could find the Tutoring Center. The third test used uppercase letters in LIBRARY to make sure the application could recognize a resource regardless of capitalization.

The fourth test searched for a dental office, which was not included in the resources, to make sure the application would return an appropriate error message and identify available resources. The fifth test used "all" to make sure the application could return a list of the available campus resources.

All five tests passed successfully when we ran them through GitHub Actions.

## Part 2: GitHub Actions and CI
When we first ran GitHub Actions, I was having repeated problems with the YAML file because of indentation errors. I learned that indentation is important in YAML because it separates the different sections and tells GitHub Actions which instructions belong together. I had to go back several times to correct the spacing before the workflow would run properly. Once the indentation was corrected, GitHub Actions successfully ran all five tests.
Repeatedly correcting the YAML indentation errors actually helped me better understand how indentation works. I began connecting it to concepts I had already learned in programming, such as loops and nested loops, where statements must be organized properly. Although the repeated errors were frustrating at times, correcting them helped reinforce the importance of indentation and how instructions are structured. This experience also helped me understand that small formatting mistakes can prevent a program or workflow from running correctly.
The GitHub Actions workflow was set up to automatically run the five Python tests whenever changes were pushed to the main branch of my GitHub repository. The workflow uses Python 3.11, installs the required dependencies, and runs the tests using pytest. This allows the tests to be checked automatically without having to run them manually every time I make a change.

## Part 3: Continuous Deployment
I learned that automatic deployment also needed to be tested to make sure changes made in GitHub were being transferred properly to Streamlit Cloud. We made a small change to the application and pushed it to GitHub to see whether Streamlit would automatically update. I also learned that Streamlit keeps logs in the Manage App section, which allowed me to see when the application pulled the changes from GitHub and completed the update. This helped me verify that the automatic deployment was working properly.

## Part 4: AI Evaluation and Reflection

I believe AI is capable of making errors and hallucinations, as I have experienced numerous times while working on assignments. Sometimes I had to clarify what I was asking, and even when I uploaded screenshots, the AI did not always interpret exactly what was on the screen. However, I found AI helpful in explaining problems and helping me work through them, even when we had to revisit the same issue several times. Sometimes the initial solution was not the best one, or correcting one error would lead to another problem that had been overlooked.

One of the benefits I found was that AI helped me keep track of where I was in the project, making it easier to continue without having to scroll through numerous pages of instructions. I also prefer using AI in a way that allows me to attempt the work myself first. Instead of immediately giving me the answer, AI asks me questions, allows me to respond, and then helps correct my understanding. I believe this approach is more beneficial because it allows me to learn the material rather than simply depend on AI to complete the work.

### Improving My Use of AI

I do not believe there is much I would change about the way I prompted AI during this assignment. I think many of the repeated errors and corrections are also related to my own level of experience. As I continue learning programming and become more familiar with the different languages and their syntax, I believe I will become less dependent on AI, especially for basic tasks.

My goal is to continue developing my own understanding so that I can recognize errors more easily and make corrections myself. I believe that as my knowledge improves, I will also become better at evaluating the suggestions AI provides rather than relying on every answer being correct.

## Part 5: Benefits to JCC Students

The resources provided by the Campus Resource Assistant are important to the success of a student's education. Students need accurate and timely information because they are often working against deadlines and may need to use resources such as tutoring or the library before an assignment is due. If the application provides incorrect or outdated information, it could delay students in getting the help they need, which could affect their assignments, grades, and overall performance. Automated testing helps make sure the application returns the expected information, while automatic deployment makes it easier to provide updates when changes are made.

## Part 6: How I Used AI and ### AI Prompts Used for Testing and GitHub ActionsPrompting


When I use AI, I am mainly looking for a framework or formula that helps me understand how to complete a task rather than just being given the exact code. I like to go over the steps repeatedly until the process becomes more familiar to me. I also prefer typing the code myself because I believe that helps reinforce what I am learning.

This semester I am working with Java, Python, and SQL, so I understand that I cannot memorize every command or the exact syntax for each language. My main goal is to understand the logic behind the programming. When working on the automated tests and GitHub Actions workflow, I used AI to help me understand the steps, identify errors, and make corrections. I wanted to understand why the code was written a certain way instead of simply copying it.

I believe that understanding the logic will help me apply what I learn to other programming languages and future assignments.
When creating the Python tests, I preferred typing the code myself while following the instructions provided by AI. I believe typing the code helps reinforce what I am learning and makes the syntax more familiar. I also wanted to understand the purpose of each test rather than simply copy and paste the code. This approach allowed me to practice writing Python while learning how automated testing works.
When working on the automated tests and GitHub Actions workflow, I used AI as a step-by-step learning tool. My AI instructions are set up so that it asks me to attempt each step before providing corrections. I used this approach to understand how to create the five Python tests and configure the GitHub Actions YAML file. When errors occurred, I shared the results and screenshots with AI to help identify the problems. I then made the corrections myself and repeated the process until the tests and workflow passed successfully.