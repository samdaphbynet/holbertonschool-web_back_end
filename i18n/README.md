# i18n
## Overview
This project focuses on internationalization and localization (i18n) in a Flask application. It involves setting up multilingual support, parametrizing templates for different languages, inferring the correct locale and timezone, and handling user preferences.

### Learning Objectives
This project aims to help you achieve the following learning objectives:

- Learn how to parametrize Flask templates to display different languages
- Understand how to infer the correct locale based on URL parameters, user settings, or request headers
- Learn how to localize timestamps

## Requirements
Ensure that your code meets the following requirements:

- Interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7)
- Follow the pycodestyle style (version 2.5)
- All files must end with a new line
- A README.md file, at the root of the project folder, is mandatory
- The first line of all files should be exactly #!/usr/bin/env python3
- All *.py files should be executable
- All modules, classes, functions, and methods should be documented
- Use type annotations for all functions and coroutines

### Tasks
The project consists of several tasks, each focusing on different aspects of internationalization and localization in a Flask application. Each task has specific requirements and scoring criteria.

- Task 0: Basic Flask app
Set up a basic Flask app with a single route and template to display a welcome message.

- Task 1: Basic Babel setup
Install the Babel Flask extension and configure it to support multiple languages.

- Task 2: Get locale from request
Implement a function to determine the user's preferred language based on request headers.

- Task 3: Parametrize templates
Parametrize templates using the _ or gettext function for internationalization.
Initialize translations and provide translations for message IDs in different languages.

- Task 4: Force locale with URL parameter
Implement a way to force a particular locale by passing a parameter in the app's URLs.

- Task 5: Mock logging in
Mock user login system by passing user information as URL parameters.
Display a welcome message based on the user's logged-in status.

- Task 6: Use user locale
Modify the function to use a user's preferred locale if available.

- Task 7: Infer appropriate time zone
Define a function to infer the appropriate time zone based on user preferences and request parameters.