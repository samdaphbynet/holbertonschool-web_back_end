# Unittests in JS

## Description

This project focuses on learning how to perform unit tests in JavaScript using Mocha, Chai, and Sinon. It covers various aspects such as writing test suites, using different assertion libraries, presenting long test suites, utilizing spies and stubs, understanding hooks, handling async functions, and writing integration tests with a small node server.

## Resources

- [Mocha documentation](https://mochajs.org/)
- [Chai](https://www.chaijs.com/)
- [Sinon](https://sinonjs.org/)
- [Express](https://expressjs.com/)
- [Request](https://www.npmjs.com/package/request)
- [How to Test NodeJS Apps using Mocha, Chai and SinonJS](https://www.codementor.io/@davidtang/how-to-test-node-js-apps-using-mocha-chai-and-sinonjs-du107rmn7)

## Learning Objectives

By the end of this project, you will be able to:

- Explain how to use Mocha to write a test suite
- Use different assertion libraries (Node or Chai)
- Present long test suites effectively
- Understand when and how to use spies and stubs
- Understand hooks and their usage
- Perform unit testing with Async functions
- Write integration tests with a small node server

## Requirements

- OS: Ubuntu 18.04
- Node version: 12.x.x
- Editors: vi, vim, emacs, Visual Studio Code
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Code files should have the `.js` extension
- Running tests with `npm run test *.test.js` should pass without any warnings or errors

## Tasks

### 0. Basic test with Mocha and Node assertion library

- Install Mocha using npm
- Set up a script in `package.json` to run Mocha using `npm test`
- Use assert
- Create a function named `calculateNumber` in a file named `0-calcul.js`, which accepts two arguments and returns the sum after rounding them

#### Test cases

- Create a file `0-calcul.test.js` containing test cases for the `calculateNumber` function
- Tests should focus on the "rounded" part

#### Tips

- Ensure to consider edge cases in your tests

#### Expected output

```
> const calculateNumber = require("./0-calcul.js");
> calculateNumber(1, 3)
4
> calculateNumber(1, 3.7)
5
> calculateNumber(1.2, 3.7)
5
> calculateNumber(1.5, 3.7)
6
>
```

Run test

```
bob@dylan:~$ npm test 0-calcul.test.js

> task_0@1.0.0 test /root
> ./node_modules/mocha/bin/mocha "0-calcul.test.js"

  calculateNumber
    ✓ ...
    ✓ ...
    ✓ ...
    ...

  130 passing (35ms)
bob@dylan:~$
```
