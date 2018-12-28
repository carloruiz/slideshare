import json

infile = open('institutions.txt')
outfile = open('institutions.json', 'w')

augmented = []
for line in infile.readlines():
    out_str = [" "]*65
    if len(line) > 60 or len(line.split(',')) > 2:
        continue
    inst,state = line.split(",")
    out_str[:len(inst)] = inst
    out_str[-(len(state)+3):] = '   ' + state[:-1]
    augmented.append({
        "key": inst.lower(), 
        "text": ''.join(out_str), 
        "value": inst.lower()
    })

outfile.write(json.dumps(augmented))
