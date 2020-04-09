# The Bug Game, solver!

This implementation is more efficient (solves in 0.008 seconds), but it's ugglier as it just spews the solutions in the terminal.

## Recursion

We write a function that it's only job is just to check:
1. If I can still move to another square.
2. If we cant, we check if I've stepped on all squares with bugs.
3. If we're on square No. 16

if we can still move, we call this same function, which checks everything again but from a new square's perspective!

**For a prettier (but a lot less efficient) version of this, check out my codepen:**

https://codepen.io/jpaulmora/pen/vYNBMbB

