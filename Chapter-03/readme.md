# Finite Markov Decision Processes
This chapter covers a central idea of reinforcement learning which is markov decision process.

### Markov Property
> The future is independent of the past, given the present

This property states that the, 
* State ```s``` captures the all information about history
* Once state ```s``` is known all the history can be thrown away

![Wikipedia](https://wikimedia.org/api/rest_v1/media/math/render/svg/42ea39e3455c78fb327846f28a47c1c45aef6719)
*state transition equation*

## Markov  Reward Process 
Markov reward process is a markov process which has an insentive about rewards. Just like we put forward a probability of a state occuring, we add another value to represent the expected reward we've accumilated while achieveing the till the given state.