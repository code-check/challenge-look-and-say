# Look and Say!

This challenge is to make a function which returns a number according to some secret rule.

Pass '1' to this function, it returns '1'.
Pass '2' to this function, it returns '11'.

Pass '3' to '7' returns following.

```
3=21
4=1211
5=111221
6=312211
7=13112221
```

Find the rule of this sequence and implement the function.
(The result should be written to stdout.)

You can use following languages.

- NodeJS
- Ruby
- Python3
- Go
- Java

## Secret Test
This challenge has 7 testcases. You can see these in [testcase.js](test/testcase.js)  
However, this challenge has more 3 testcases. These are hidden.

- Secret1. Pass '8' to this function, it should return collect answer.
- Secret2. Pass '20' to this function, it should return collect answer.
- Secret3. If the input number is '1000', how long length the result number is? Write the answer at the top line of [answer.md](answer.md). Also, explain how to solve this problem below.

If your function is implemented correctly, first 2 test will pass.

However, if your function is implemented very simple way, the last question eat all your memory.  
Try to find some optimization.
