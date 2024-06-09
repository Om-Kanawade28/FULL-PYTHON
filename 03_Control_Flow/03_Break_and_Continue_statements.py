# 1) Break:-
for i in range(1, 11):
    if i == 5:
        break
    print(i)


#   - Output:

'''
1
2
3
4
'''

#   - Explanation:

#     - The loop iterates from 1 to 10.
#     - When `i` reaches 5, the `if` condition becomes true, and the `break` statement is executed.
#     - The loop terminates immediately, and the remaining iterations are skipped.

# 2. `continue` Statement:

#   - The `continue` statement is used to skip the current iteration of the loop and jump to the next iteration. It does not terminate the loop; it simply moves to the next iteration.

#   - Example:


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


#   - Output:

'''
1
3
5
7
9
'''
#   - Explanation:

#     - The loop iterates from 1 to 10.
#     - For each iteration, the `if` condition checks if `i` is divisible by 2 (even).
#     - If `i` is even, the `continue` statement is executed, which skips the rest of the code in the current iteration and jumps to the next iteration.
#     - If `i` is odd, the `print(i)` statement is executed.

# 3. `break` and `continue` in Nested Loops:

#   - You can use `break` and `continue` statements within nested loops to control the flow of execution in both the inner and outer loops.

#   - Example:

for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            break
        print(f"i: {i}, j: {j}")
    print("-" * 10)


#   - Output:

'''
i: 1, j: 1
i: 1, j: 2
----------
i: 2, j: 1
i: 2, j: 2
----------
i: 3, j: 1
i: 3, j: 2
----------
'''

#   - Explanation:

#     - The outer loop iterates from 1 to 3.
#     - The inner loop iterates from 1 to 5.
#     - When `j` reaches 3, the `break` statement is executed, which terminates the inner loop.
#     - The outer loop continues to its next iteration.

# 4. `break` and `continue` with `else` Block:

#   - You can use an `else` block with `for` and `while` loops. The `else` block is executed only if the loop completes normally (without encountering a `break` statement).

#   - Example:

for i in range(1, 11):
    if i == 5:
        break
    print(i)
else:
    print("The loop completed normally.")


#   - Output:

'''
1
2
3
4
'''

#   - Explanation:

#     - The loop iterates from 1 to 10.
#     - When `i` reaches 5, the `break` statement is executed, and the loop terminates prematurely.
#     - The `else` block is not executed because the loop did not complete normally.



# Remember that `break` and `continue` statements are powerful tools for controlling the flow of execution in loops. Use them judiciously to make your code more efficient and readable.
#
#
#
