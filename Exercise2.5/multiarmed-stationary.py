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

banditinit = numpy.random.randn(10, 2)+2
bandit = numpy.prod(banditinit, axis=1)
print(bandit)

print(f"arms {arms}")
print(f"Q {Q}")
print(f"N {N}")

mse = []

# while(True):
for i in range(10000):
    id = numpy.argmax(Q)

    # calculating the probs
    probs = numpy.ones_like(Q) * e
    probs[id] = 1 - e
    probs = probs/probs.sum()
    action = numpy.random.choice(arms, p=probs)

    reward = numpy.random.normal(bandit[action])
    N[action] += 1
    Q[action] += 1/N[action] * (reward-Q[action])
    mse.append(0.1 * ((bandit - Q)**2).sum())
    # placeholder_bandit

plt.plot(mse)
plt.show()
