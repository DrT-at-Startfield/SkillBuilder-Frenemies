# FrenemiesScript
ledger = dict()

def Create(name, likesMe=True, likeThem=True):
    frenemy = {'name':name, 'Likes Me':likesMe, 'Like Them':likeThem}
    ledger[frenemy['name']] = frenemy

def PrintLedger():
    for item in ledger:
        print(ledger[item])


Create('Amy C.')
Create('Jane T.')
Create('Sam T.')
Create('Vlad P.', False, False)
Create('Bobby D.', False, likeThem=True)


if __name__ == "__main__":
    PrintLedger()