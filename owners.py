class FileOwners:

    @staticmethod

    def group_by_owners(files):
        owners=set()
        ownerDict={}

        for k, v in files.items():
            #fill set w/ names of owners
            owners.add(v)
        for o in owners:
            ownerDict[o]=[]
            for k, v in files.items():
                #fill out new dictionary w/ list of file names
                if v==o:
                    ownerDict[o].append(k)
        return ownerDict;
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))


