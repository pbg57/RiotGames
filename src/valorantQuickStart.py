import valorant

KEY = "RGAPI-120a1779-37cd-47a1-a8f6-4feb8fef6428"

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
