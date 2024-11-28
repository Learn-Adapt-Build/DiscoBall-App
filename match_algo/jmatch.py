import random
import os
import pandas as pd
df = pd.read_csv('dummy data - Sheet1 - Copy.csv')
groups = [[], [], [], [], []]
participantNum = []
participants = {}
for i in range(25):
    participants[i] = []
answers = df["Are you more of an introvert or an extrovert?"]
q1 = answers.to_dict()
answers2 = df["Do you like to have a more public-facing or BTS role in a team?"]
q2 = answers2.to_dict()
for i in range(len(q1.keys())):
    participants[i].append(q1[i])
for i in range(len(q2.keys())):
    participants[i].append(q2[i])

#sorting alg
sorted_participants = dict(sorted(participants.items(), key=lambda x: x[1]))

#pain made manifest


#assign leaders
for i in groups:
    failsafe = 0
    for j in sorted_participants:
        if sorted_participants.get(j)[0] >= 3 or sorted_participants.get(j)[1] == 3:
            i.append(j)
            failsafe = j
            break
    if failsafe != 0:
        del sorted_participants[failsafe]

#add randos
for i in range(4):
    for j in groups:
        failsafe = 0
        for y in sorted_participants:
            j.append(y)
            failsafe = y
            break
        del sorted_participants[failsafe]

print(groups)