# Math-Series

**Author**: Terrell Douglas

**Version**: 1.0.0

## Overview
The purpose was to create a function called fibonacci. The function should have one parameter and return the nth value in the fibonacci series. Implement the function using recursion or iteration.

After that write a function called lucas that returns the nth value in the lucas numbers.

Then write a third function called sum_series with one required parameter and two optional parameters. The two optional parameters should have default values of 0 and 1 and will determine the first two values for the series to be produced.

## Getting Started
For the fibonacci function I passed a param of n. I then went into an if statement declaring that if n were less than or equil to 1 then return the value of n. Otherwise I want to return the value of n-1 plus the value of n-2.

For the lucas function I passed the param of r. I then went into an if statement and said that if value of r is equil to zero I want it to return two. Also, if r equils one then return one. Otherwise return the value of r-1 plus the value of r-2.

For the sum_series function I inserted 3 params (one mandatory, 2 optional). I passed in x, y, and z. I then said that if x equils 2 then return the value of y and if x equils one then return the value of z. Otherwise return the value of (x-1, y, z) and the value of (x-2, y, z).
