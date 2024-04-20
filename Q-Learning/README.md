# Q-Learning on GridWorld

**A rectangular grid is an intuitive example
of reinforcement learning application. Many real-world scenarios can be abstractly modeled as a rectangular grid.**

• **<u>Environment</u>**: GridWorld is a 2D rectangular grid of size (Ny, Nx). In the
GridWorld an agent starts off at any “grid square” and try to move to another
grid square located elsewhere in its world. The objective is to discover optimal
paths and policies for agents on the grid to get to their desired goal “grid
square” in the least number of moves.

![GridWorld](/resources/GridWorld.png)

In our GridWorld implementation (above), we start the agent at the top-left
grid corner at (0, 0) with the aim of arriving at bottom-right grid corner at (Ny-1, Nx-1) in a minimal number of steps i.e. (Ny + Nx) steps. The agent is only
allowed actions of: UP, DOWN, LEFT, and RIGHT by 1 grid square. [A possible policy is shown by green highlighted squares]


• **<u>Rewards</u>**: An agent can move in all 4 directions in a middle square, 3
directions on the grid edge, and 2 directions at the grid corner. As for
rewarding the agent, we give a reward of R=+100 for arriving at the desired
goal grid square, and a reward of R= - 0.1 to incentivize the agent to reduce the
number excess moves to get to the goal.

• **<u>Q-Learning</u>**: The training cycle involves having the agent interacting with the
environment via taking actions, collecting the corresponding rewards, and
transitioning its state to other states. We initialize a tabular state-action value
function Q(s, a) that will be iteratively updated to assist in the agent’s
exploitation mechanism. Recall that Q(s, a) represents the expected long-term
discounted reward collected from applying action “a” to the state “s”, then
following the optimal policy afterwards for the remainder of the state
transitions.
Use the following update rule for action-value updates.

    Q(s,a) ← [1−α]Q(s,a) + α[r(s,a) + γ maxb Q(s',b)]

where, α is the learning rate.
The Q(s,a) update happens after every episode where we take the total reward
collected from the episode, and update exactly the Q(s,a) values for the (s, a)
state-action pairs that agent experienced during the episode; it is the memory
that stores this information for the brain to process.


My Implementation:

I have implemented Q-Learning for GridWorld.
Defined 3 distinct classes to make code conceptually easier to
understand:

• Environment

• Agent

• Brain (of agent)