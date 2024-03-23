# NodeJS Basics

## Description

This project covers the fundamentals of NodeJS, providing exercises to get started with executing JavaScript, using NodeJS modules, working with processes, creating HTTP servers, and more. Each task comes with specific requirements to fulfill.

## Resources

Read or watch:

- [Node JS getting started](https://nodejs.org/en/docs/guides/getting-started-guide/)
- [Process API documentation](https://nodejs.org/dist/latest-v14.x/docs/api/process.html)
- [Child process](https://nodejs.org/dist/latest-v14.x/docs/api/child_process.html)
- [Express getting started](https://expressjs.com/en/starter/installing.html)
- [Mocha documentation](https://mochajs.org/)
- [Nodemon documentation](https://nodemon.io/)

## Learning Objectives

- Execute JavaScript using NodeJS
- Utilize NodeJS modules
- Use specific NodeJS modules to read files
- Access command line arguments and the environment using process
- Create a small HTTP server using NodeJS
- Create a small HTTP server using ExpressJS
- Create advanced routes with ExpressJS
- Use ES6 with NodeJS with Babel-node
- Develop faster using Nodemon

## Requirements

- Allowed editors: vi, vim, emacs, Visual Studio Code
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using node (version 12.x.x)
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Code files should use the .js extension
- Code will be tested using Jest with the command `npm run test`
- Code will be verified against lint using ESLint
- All functions/classes must be exported using the format: `module.exports = myFunction;`
- Ensure to run `npm install` when you have the package.json

## Tasks

### 0. Executing basic JavaScript with NodeJS

In the file `0-console.js`, create a function named `displayMessage` that prints the string argument to STDOUT.

Example:

```
$ cat 0-main.js
const displayMessage = require('./0-console');

displayMessage("Hello NodeJS!");

$ node 0-main.js
Hello NodeJS!
```

## Tasks

### 2. Reading a file synchronously with Node JS

In the file `2-read_file.js`, create a function named `countStudents` that reads the database file synchronously and logs the number of students in each field.

- Create a function named `countStudents` that accepts a path as an argument.
- Attempt to read the database file synchronously.
- If the database is not available, throw an error with the text "Cannot load the database".
- If the database is available, log the number of students in each field along with their first names.

Example:

```
$ cat 2-main_0.js
const countStudents = require('./2-read_file');

countStudents("nope.csv");

$ node 2-main_0.js
2-read_file.js:9
    throw new Error('Cannot load the database');
    ^

Error: Cannot load the database
...

$ cat 2-main_1.js
const countStudents = require('./2-read_file');

countStudents("database.csv");

$ node 2-main_1.js
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
```

### 3. Reading a file asynchronously with Node JS

In the file 3-read_file_async.js, create a function named countStudents that reads the database file asynchronously and returns a Promise.

Create a function named countStudents that accepts a path as an argument (same as in 2-read_file.js).
Attempt to read the database file asynchronously.
Return a Promise.
If the database is not available, reject the Promise with an error with the text "Cannot load the database".
If the database is available, log the number of students in each field along with their first names.
Example:

```
$ cat 3-main_0.js
const countStudents = require('./3-read_file_async');

countStudents("nope.csv")
    .then(() => {
        console.log("Done!");
    })
    .catch((error) => {
        console.log(error);
    });

$ node 3-main_0.js
Error: Cannot load the database
...

$ cat 3-main_1.js
const countStudents = require('./3-read_file_async');

countStudents("database.csv")
    .then(() => {
        console.log("Done!");
    })
    .catch((error) => {
        console.log(error);
    });
console.log("After!");

$ node 3-main_1.js
After!
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Done!
```

### 4. Create a small HTTP server using Node's HTTP module

In a file named 4-http.js, create a small HTTP server using the http module:

Assign it to the variable app and export it.
The HTTP server should listen on port 1245.
It should display "Hello Holberton School!" in the page body for any endpoint as plain text.
Example:

Terminal 1:

```
$ node 4-http.js
```

Terminal 2:

```

$ curl localhost:1245 && echo ""
Hello Holberton School!

$ curl localhost:1245/any_endpoint && echo ""
Hello Holberton School!

```
