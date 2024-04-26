Lets understand this with an example

Q. Imagine a classroom of 100 students in which you gave your pen to one person. You have to find that pen without knowing to whom you gave it.

Here are some ways to find the pen and what the O order is.

    O(n2): You go and ask the first person in the class if he has the pen. Also, you ask this person about the other 99 people in the classroom if they have that pen and so on,
    This is what we call O(n2).
    O(n): Going and asking each student individually is O(N).
    O(log n): Now I divide the class into two groups, then ask: “Is it on the left side, or the right side of the classroom?” Then I take that group and divide it into two and ask again, and so on. Repeat the
        process till you are left with one student who has your pen. This is what you mean by O(log n).

The above O -> is called Big – Oh which is an asymptotic notation. There are other asymptotic notations like theta and Omega.

NOTE: We are interested in the rate of growth over time with respect to the inputs taken during the program execution.

Is the Time Complexity of an Algorithm/Code the same as the Running/Execution Time of Code?
The Time Complexity of an algorithm/code is not equal to the actual time required to execute a particular code, but the number of times a statement executes. We can prove this by using the time command.

you will get different timings on different machines. Even if you will not get the same timings on the same machine for the same code, the reason behind that is the current network load.
we can say that the actual time required to execute code is machine-dependent (whether you are using Pentium 1 or Pentium 5) and also it considers network load if your machine is in LAN/WAN.

What is meant by the Time Complexity of an Algorithm?
Instead of measuring actual time required in executing each statement in the code, Time Complexity considers how many times each statement executes.

How to Compare Algorithms?

To compare algorithms, let us define a few objective measures:

    1. Execution times: Not a good measure as execution times are specific to a particular computer.
    2. The number of statements executed: Not a good measure, since the number of statements varies with the programming language as well as the style of the individual programmer.
    3. Ideal solution:  Let us assume that we express the running time of a given algorithm as a function of the input size n (i.e., f(n)) and compare these different functions corresponding to running times.
        This kind of comparison is independent of machine time, programming style, etc. Therefore, an ideal solution can be used to compare algorithms.
