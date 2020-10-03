import numpy
import matplotlib.pyplot as plt

# arms(actions) if the problem
# this simple bandit has 10 possible actions
arms = [i for i in range(10)]

# placeholder Q value for each of the actions
Q = [0 for i in range(10)]

# epsilon value
e = 0.005

N = [0 for i in range(10)]

# create bandit
banditinit = numpy.random.randn(10, 2)+2
bandit = numpy.prod(banditinit, axis=1)

print(f"arms {arms}")
print(f"Q {Q}")
print(f"N {N}")

mse = []

# run for 10000 iterations
for i in range(10000):

    # getting picking the highest prob action
    id = numpy.argmax(Q)

    # calculating the probs
    probs = numpy.ones_like(Q) * e
    probs[id] = 1 - e
    probs = probs/probs.sum()

    # selecting action
    action = numpy.random.choice(arms, p=probs)

    # sampling reward from the bandit
    reward = numpy.random.normal(bandit[action])
    
    N[action] += 1
    
    # update Q table
    Q[action] += 1/N[action] * (reward-Q[action])
    
    # calculate mse
    mse.append(0.1 * ((bandit - Q)**2).sum())

plt.plot(mse)
plt.show()
