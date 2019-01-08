import json

infile = open('institutions.txt')
outfile = open('institutions.json', 'w')

augmented = {}
for line in infile.readlines():
    out_str = [" "]*65
    if len(line) > 60 or len(line.split(',')) > 2:
        continue
    inst,state = line.split(",")
    #out_str[:len(inst)] = inst
    #out_str[-(len(state)+3):] = '   ' + state[:-1]
    augmented[inst+', \t'+state] = inst.lower()

outfile.write(json.dumps(augmented))
