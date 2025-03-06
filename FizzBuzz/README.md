## Documentation

I started by asking chat gpt this : 

Write a JavaScript program that prints all the integers between 1 and 100, except in three situations:

If an integer in the counter is divisible by 3, print "Fizz";

if an integer in the counter is divisible by 5, print "Buzz";

if an integer in the counter is divisible by both 3 and 5, print "FizzBuzz". in javascript


It spit out this code:

for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}

I ran it through and it worked so I decided to break it down:
First line: 
i represents the start of the loop and ' i <= 100 ' means to run until it hits 100

i++ means to add one. If I run the first line of code without it, it errors because it means there is no ending, it just endlessly repeats 1 without ever reaching 100

Moving onto the 2nd line
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
'If' sets a conditional

'i % 3 === 0 && i % 5 === 0' means that i has to be divisable by 3 and 5

&& means a command can only run if both statments are true [source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)

console.log("FizzBuzz") - this says to print this string if the prior conditional is met.

Moving on to this:

	else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
else is used in a block of code after an 'if' statement. Stating what do do if the previous statment is deemed false [source](https://www.w3schools.com/js/js_if_else.asp)

Importat thing I'm noting for myself: console.log has to be in {}

Lastly breaking down:
else {
        console.log(i);
		}

This means that if the number (i) is neither divisable by 3, 5 or both- then just print i as normal.