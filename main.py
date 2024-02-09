from setting import Bandits
from agent import Agent
import matplotlib.pyplot as plt

TESTING_SIZE = 2000

def test_performance(agent):
    sum = 0
    cnt = 0
    for i in range(TESTING_SIZE):
        action = agent.make_action()
        reward = game.reward(action)

        sum += reward
        cnt += 1

    return sum / cnt

K = 100
M = 3000

game = Bandits(k=K)

agent_1 = Agent(epsilon=0.05, k=K)
agent_2 = Agent(epsilon=0.01, k=K)
agent_3 = Agent(epsilon=0.1, k=K)

game.info()

plt.ion()  # Enable interactive mode

datax = []
datay_1 = []
datay_2 = []
datay_3 = []

fig, ax = plt.subplots()  # Create figure and axis objects

for i in range(M):
    if i % 100 == 0:
        print(f"STEP = {i}")

    action = agent_1.make_action()
    reward = game.reward(action)

    agent_1.set_new_reward(action, reward)

    action = agent_2.make_action()
    reward = game.reward(action)

    agent_2.set_new_reward(action, reward)

    action = agent_3.make_action()
    reward = game.reward(action)

    agent_3.set_new_reward(action, reward)

    datax.append(i)

    datay_1.append(test_performance(agent_1))
    datay_2.append(test_performance(agent_2))
    datay_3.append(test_performance(agent_3))

    ax.clear()  # Clear the previous plot
    ax.plot(datax, datay_1, color='b')  # Plot the new data
    ax.plot(datax, datay_2, color='r')
    ax.plot(datax, datay_3, color='g')

    ax.set_xlabel('Steps')
    ax.set_ylabel('Average Reward')
    ax.set_title('Performance over time')

    plt.pause(0.001)  # Pause for a short interval to update the plot

agent_1.info()
agent_2.info()

plt.ioff()  # Turn off interactive mode
plt.show()
