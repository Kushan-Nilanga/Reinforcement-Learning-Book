# Dynamic Programming 
Dynamic programming is sequential or temporal method of optimising a ```policy```. 

By using dynamic programming,
- We can solve complex problems
- Break down complex problems to sub problems and solve them

In order for dynamic programming solution to exist,
- There should be an optimal substructure - Means that this is infact can be solved by solving the subproblems.
- Overlapping subproblems - Subproblems that occur, will occur again and again.

Markov decision processes satisfies both of the above conditions,
- Bellman equation gives recursive decomposition
- Value function stores and reuses solutions

## References
[RL Course by David Silver - Lecture 3: Planning by Dynamic Programming](https://www.youtube.com/watch?v=Nd1-UUMVfz4)