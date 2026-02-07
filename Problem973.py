'''
A game is played with cards.
At the start the cards are dealt out onto a table to get piles of size one.

Each round proceeds as follows:
    1. Select a pile at random and pick it up.
    2. Randomly choose a pile from the table and add the top card of the picked-up pile to it.
    3. Redistribute any remaining cards from the picked-up pile by dealing them into new single-card piles.

The game ends when all cards are in a single pile.

At the end of each round a score is obtained by bitwise-XORing the size of each pile. The score is summed across the rounds.
Let X(n) be the expected total score at the end of the game.

You are given X(2)=2, X(4)=14 and X(10)=1418.
'''
import numpy as np
'''

# States: 0=Active, 1=Idle, 2=Churned
states = ["1,1,1,1", "1,1,2", "2,2","1,3","4"]

# Rows must sum to 1
# Note the last row [0, 0, 1] makes state 2 absorbing
P = np.array([
    [0, 1,   0,   0,   0  ],
    [0, 1/3, 1/3, 1/3, 0  ],
    [0, 0,   0,   1,   0  ],
    [0, 1/2, 0,   0,   1/2],
    [0, 0,   0,   0,   1  ]
])

# Extract Q (transient states: Active and Idle)
Q = P[:4, :4]

# Extract R (transitions to Churned)
R = P[:4, 4:]

# Calculate Fundamental Matrix N = (I - Q)^-1
I = np.eye(4)
N = np.linalg.inv(I - Q)

# 2. Define scores for the transient states
# score_vector[0] is for Active, score_vector[1] is for Idle
scores = np.array([0,2,0,2])

# 4. Calculate Expected Total Score
expected_total_scores = N.dot(scores)

print(f"Expected lifetime score: {4+expected_total_scores[0]:.2f}")

# States: 0=Active, 1=Idle, 2=Churned
states = ["1,1", "2"]

# Rows must sum to 1
# Note the last row [0, 0, 1] makes state 2 absorbing
P = np.array([
    [0, 1],
    [0,1]
])

# Extract Q (transient states: Active and Idle)
Q = P[:1, :1]

# Extract R (transitions to Churned)
R = P[:1, 1:]

# Calculate Fundamental Matrix N = (I - Q)^-1
I = np.eye(1)
N = np.linalg.inv(I - Q)

# 2. Define scores for the transient states
# score_vector[0] is for Active, score_vector[1] is for Idle
scores = np.array([0])

# 4. Calculate Expected Total Score
expected_total_scores = N.dot(scores)

print(f"Expected lifetime score: {2+expected_total_scores[0]:.2f}")



'''







'''
GET P MATRIX
'''

def X(cards):

    # state is an array of tuples representing pilesize,count

    # State A: is all single piles

    #states = [{1:2,2:1}] #there are (cards) piles of size 1
    #p = [0]

    end_state = {cards:1}

    states = [{1:cards}]

    def next_p(state):
        p=[0]*len(states)

        def put(state, handsize, prob_pick):
            piles_in_state = sum(state.values())
            for putsize in state:
                temp_state = state.copy()
                prob_put = state[putsize]/piles_in_state

                # remove one pile of size putsize
                temp_state[putsize] -= 1
                if temp_state[putsize]==0: del temp_state[putsize]

                # add one pile of size putsize+1
                temp_state[putsize+1] = temp_state.get(putsize+1,0)+1

                # this is removed from hand
                remainder = handsize - 1

                # any remaning cards are singelton piles
                if remainder>0: temp_state[1] = temp_state.get(1,0)+remainder

                #output
                #print("FINAL",temp_state, prob_pick*prob_put)

                if temp_state not in states:
                    states.append(temp_state)
                    p.append(0)    
                p[states.index(temp_state)] += prob_pick*prob_put
                



        def pick(state):
            # absorbing state
            if state == end_state:
                p[states.index(state)] = 1.0
                return

            piles_in_state = sum(state.values())
            for handsize in state:
                temp_state = state.copy()
                prob = state[handsize]/piles_in_state
                temp_state[handsize] -= 1
                if temp_state[handsize] == 0: del temp_state[handsize]
                put(temp_state,handsize,prob)

        pick(state)
        #print(states)
        #print(p)
        return p


    P = []
    i = 0
    while i<len(states):
        P.append(next_p(states[i]))
        i+=1
    #print(P)

    


    # Pad rows of P: row + [0] * (difference)
    P = [row + [0] * (len(states) - len(row)) for row in P]
    #P = np.array(P)
    #print(P)

    # move absorbing state to bottom left
    absorb_index = states.index(end_state)
    states[absorb_index], states[-1] = states[-1], states[absorb_index]
    P[absorb_index], P[-1] = P[-1], P[absorb_index]
    for row in P:
        row[absorb_index], row[-1] = row[-1], row[absorb_index]
    #P[:,[-1,absorb_index]] = P[:,[-absorb_index,-1]]
    #P[[-1,absorb_index],:] = P[[-absorb_index,-1],:]
    
    P = np.array(P)
    '''
    # --- VERIFICATION CHECK ---
    print(f"Total States: {len(states)}")
    row_sums = P.sum(axis=1)
    if not np.allclose(row_sums, 1.0):
        print("WARNING: Matrix is not stochastic! Rows do not sum to 1.")
        # Print the first bad row for debugging
        for idx, s in enumerate(row_sums):
            if not np.isclose(s, 1.0):
                print(f"Row {idx} sums to {s}")
                break
    else:
        print("Check Passed: Matrix is stochastic (rows sum to 1.0).")
    '''
    '''
    TO SOLVE

    P = [ Q  R ]
        [ 0  I ]

    Q transitions between transient states
    R transitions to absorbing states
    I identity of absorbing states

    N = (I-Q)^(-1)
    '''

    n = len(states)-1
    Q = P[:n, :n]
    R = P[:n, n:]
    I = np.eye(n)
    N = np.linalg.inv(I - Q)



    scores = []

    for state in states[:-1]:
        score = 0
        for pilesize in state:
            count = state[pilesize]
            # if even count then XOR of these piles is 0. Otherwise only count once.
            if count % 2 == 1: score ^= pilesize
        scores += [score]

    scores = np.array(scores)

    expected_total_scores = N.dot(scores)

    score_from_start = round(expected_total_scores[0] + cards)
    #print(round(expected_total_scores[0] + cards))
    return score_from_start

print(X(2))
print(X(4))
print(X(10))
#print(X(100))
#print(X(1000))



'''
temp_state = state.copy()
# DISCOVER probability of picking pile of size=pilesize
prob_pilesize_pick = temp_state[pilesize_pick]/piles_in_state
print("PICK:",pilesize_pick,prob_pilesize_pick)

# REMOVE pile of size=pilesize to hand
temp_state[pilesize_pick] -= 1
piles_in_state -= 1



for pilesize_put in temp_state:
    final_state = temp_state.copy()
    
    # DISCOVER probability of putting onto pile of size=pilesize
    
    
    prob_pilesize_put = final_state[pilesize_pick]/piles_in_state
    print("PUT: ",pilesize_put,prob_pilesize_put)

    final_state[pilesize_put+1] = final_state.get(pilesize_put+1,0)+1
    final_state[pilesize_put] -= 1
    if final_state[pilesize_put] == 0: del final_state[pilesize_put]
    print(final_state, prob_pilesize_pick*prob_pilesize_put)
    

'''







