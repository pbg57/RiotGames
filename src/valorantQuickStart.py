import valorant

KEY =  ""

print("Key: " + KEY)
client = valorant.Client(KEY)

agents = client.get_characters()

for agent in agents:
    print(agent.name)
    print(agent)

acts = client.get_acts()

for act in acts:
    print(act.name)
    print(act)
