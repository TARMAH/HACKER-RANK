'''
After thinking like that i also understood the logic the solution.

Let's think our summing part input like that {A B S} = {1 3 100} {2 5 150} {3 4 110} {2 4 160}

Instead of writing all elements of array we can write maximum value at just starting and ending indexes to have less writing operation. So, after first input row, array can be something like that.

0 100 0 100 0 0 0 0 0

But the problem is here that even we didn't write anything, value of index 2 is also 100. When we wanted to continue with second step we have to check whether index 2 is between indexes of first row operation or not.

Instead of doing like that we can write S value to index A and -S value to B+1, so it is still similar logic. Starting from A to B all indexes have S value and rest of them have less than these indexes as S as. Now the array is like that:

0 100 0 0 -100 0 0 0 0

While calculating second row, we are writing 150 to index 2 and -150 to index 6. It will be like that: 0 100 150 0 -100 0 -150 0 0

If we write array with old method, which means that all numbers calculated one, it will be: 0 100 250 250 150 150 0 0 0

It shows that value of index 2 is : 100+150 = 250. Value of index 5: 100 + 150 + (-100) = 150. So by calculating with the solution written above, instead of writing all numbers, we are writing changes at edge indexes.
'''




n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
max = x = 0
for i in list:
   x=x+i;
   if(max<x): max=x;
print(max)