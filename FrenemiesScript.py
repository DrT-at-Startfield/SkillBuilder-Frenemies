# FrenemiesScript
ledger = dict()

def Create(name, likesMe=True, likeThem=True):
    frenemy = {'name':name, 'Likes Me':likesMe, 'Like Them':likeThem}
    ledger[frenemy['name']] = frenemy

def Read(name):
    if name in ledger:
        return ledger[name]
    else:
        return {}
    
def Update(name, likesMe, likeThem):
    if name in ledger:
        ledger[name] = {'name':name, 'Likes Me':likesMe, 'Like Them':likeThem}
    else:
        print("{0} not in the ledger".format(name))

def Delete(name):
    if name in ledger:
        ledger.pop(name)
    else:
        print("{0} not in the ledger".format(name))

def PrintLedger():
    for item in ledger:
        print(ledger[item])

def SaveToDisk(filename):
    fp = open(filename, "w")
    fp.write("# name, likesMe, likeThem\n")
    for key in ledger:
        item = ledger[key]
        fp.write("{0},{1},{2}\n".format(item["name"], item["Likes Me"], item["Like Them"]))
    fp.close()

def ReadFromDisk(filename):
    fp = open(filename,"r")
    lines = fp.readlines()
    if len(ledger) > 0:
        ledger.clear()
    for line in lines:
        if line[0] == '#':
            continue
        else:
            split_line = line.split(",")   
            mybool1 = split_line[1].find("True") != -1
            mybool2 = split_line[2].strip().find("True") != -1
            Create(split_line[0], mybool1, mybool2)

def MakeSomeFrenemies():
    Create('Amy C.')
    Create('Jane T.')
    Create('Sam T.')
    Create('Vlad P.', False, False)
    Create('Bobby D.', False, likeThem=True)


if __name__ == "__main__":
    ReadFromDisk("ledger.csv")
    PrintLedger()
    # SaveToDisk("ledger.csv")
