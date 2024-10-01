import pickle

data = {}
for i in range(10000):
    try:
        name = 'teamMatches\\' + str(i)
        print(name)
        file = open(name, 'rb')
        data[i] = pickle.load(file)
        file.close()
    except:
        pass
print(len(data))

file = open('allTeamsMatches', 'wb+')
pickle.dump(data, file)
file.close()