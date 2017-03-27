# The Secret Rule

*This is a [codecheck](https://app.code-check.io/openchallenges) challenge. To get started, [see the docs](https://code-check.github.io/docs/en)* :-)  

There is a secret method that returns the below results:

If this method receives '1', it should return '1'.
If it receives '2', it should return '11'.  
If it receives '3', it should return '21', and so on.
```
1 -> 1
2 -> 11
3 -> 21
4 -> 1211
5 -> 111221
6 -> 312211
7 -> 13112221
```

## Your Mission

Identify the rule of this sequence and implement the function.

## Implementation
#### CLI
Build the solution as a CLI application.  
Input parameters will be passed as an argument of CLI, and
the output should be written to stdout.
How to make a CLI application with each language is explained in [YOUR LANGUAGE].md

#### Rules
- This CLI app will receive only 1 arg consisting of an integer.
- The CLI app will never receive incorrect parameters.
- Process the integer based on the secret rule, and output the result in integer form to stdout.
- You are permitted to search online for the secret sequence.
- You may not use an external library for this challenge.

#### Sample I/O
```shell
$ secret_rule 2
11
```

For reference, some of the expected I/O can be seen in the [test/](./test/) directory.

#### More Homework!
As an additional task, find the initial 500 digits of the expected output, when the input is an integer of '10000'. Write this in the first line of [longOutput.txt](longOutput.txt).
If your implementation is too earnest, the last question will eat up all of your memory! :(
Try to find a way to optimize.

PS:
This secret test will run only when the challenge is submitted,
and the results are never shown in the WebEditor.

## Answer.md
In [answer.md](answer.md) write a brief explanation about:

- How your code works
- Problems faced while solving the challenge
- How you solved those problems
