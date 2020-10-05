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

MRP state that given the state ```s``` the probably of state ```S``` being ```s(t+1)``` is ```p``` and the **expected** reward is ```r```. We use gamma ```𝛾``` as a discount factor to keep the **returns** finite. Returns is the cumulative reward over an episode.

> 𝛾 = { 𝛾 ⊂ ℝ+; 0 < 𝛾 <= 1 }

## Value Function
Value function ```v(s)``` gives the long-term value of the state ```s```. This simply states that the amount of exptected return you would get if you proceed from state ```s```.

> v(s) = 𝔼[G(t)|S(t)=s]


### Bellman Equation
![Bellman Equation](https://miro.medium.com/max/5032/1*CiDCpUjj_3mGm3vdGrxu4g.png)

## Markov Decision Process
Markov decision process is the process which incorporates state and reward probabilities with given state and action.

- Policy - distribution over actions given states
- State-value = given the state ```s```, expected return ```G(t)``` if we follow policy ```π```
![State Value](https://miro.medium.com/max/992/1*xOoMVLcOBYZe1Q-6tApTmA.png)
- Action-value = given the state ```s``` and action ```a```, expected return ```G(t)``` if we follow policy ```π```
![Action Value](https://miro.medium.com/max/1016/1*2US_ypm-938cBNH8UmA2UA.png)


### References
- [RL Course by David Silver - Lecture 2: Markov Decision Process](https://www.youtube.com/watch?v=lfHX2hHRMVQ&t=849s)