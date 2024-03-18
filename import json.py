import json


#per leggere un file json
filejson= open("all-world-cup-players.json","r")
worldcup= json.load(filejson)
filejson.close

print(len(worldcup))
print(worldcup[8000])
print(worldcup[8000]['DateOfBirth'])

quanticalciatori=dict()
for v in worldcup:
    if v["ITA"] in quanticalciatori.values():
        quanticalciatori[v["ITA"]]=quanticalciatori[v["ITA"]]+1
    else:
        quanticalciatori[v["ITA"]]=1

print("Italians:",quanticalciatori)


for v in worldcup:
    if v["Brazil"] in quanticalciatori.values():
        quanticalciatori[v["Brazil"]]=quanticalciatori[v["Brazil"]]+1
    else:
        quanticalciatori[v["Brazil"]]=1
print("Brazilians: ",quanticalciatori)