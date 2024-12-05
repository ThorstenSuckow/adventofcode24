from fileinput import input
import bisect
import math
import re



def parse_input(file_name = "") -> list:

    list = []

    if not file_name:
        file_name = './input.txt'

    sets = []
    pages = []
    target = 'sets'
    for line in input(files=(file_name)):
        
        row = line.strip()
        if row == '':
            target = 'pages'
        else:
            match target:
                case 'sets':
                    sets.append(re.split(r"\|", row))
                    sets[-1] = [int(x) for x in sets[-1]]        
                case 'pages':
                    pages.append(re.split(r",", row))
                    pages[-1] = [int(x) for x in pages[-1]]        

    zset = {}
    for i in range(len(sets)):
        if zset.get(sets[i][0]):
            bisect.insort(zset[sets[i][0]], sets[i][1])
        else : 
            zset[sets[i][0]] = [sets[i][1]]    




    return [zset, pages]

'''
PART 1
'''
def part1_process(data: list) -> int:

    [sets, pages] = data
    [valids, _] = get_lists(data)

    sum = 0
    for i in range(0, len(valids)):
        page_set = valids[i] 
        sum += pages[page_set][int(len(pages[page_set])/2)]

    return sum        



'''
PART 2
'''
def part2_process(data: list) -> int:


    [sets, pages] = data
    [_, invalids] = get_lists(data)

    sum = 0

    sanitized = []
    for i in range(0, len(invalids)):
        
        sanitized.append(pages[invalids[i]])

        page = sanitized[i]

        j = 0
        pagelen = len(page)
        
        while j < pagelen:

            curr = page[j]
            sub = sets.get(curr)

            if sub:
                for u in range(0, pagelen):
                    if (page[u] == curr):
                        continue
                    if (page[u] in sub):
                        el = page[u]
                        page.remove(el)
                        page.insert(j, el)
                        j-=1
                        break
                    
            j +=1

        


    sum = 0 
    for i in range(0, len(sanitized)):
        #print(int(len(sanitized[i])/2), sanitized[i][int(len(sanitized[i])/2)])
        sum += sanitized[i][int(len(sanitized[i])/2)]
    return sum

    pass


'''
HELPER
'''

def get_lists(data: list) -> list:

    [sets, pages] = data

    valids = []
    invalids = []

    

    for j in range(0, len(pages)): # pages: [[75,47,61,13,29], ... ]
        pg = pages[j]              #         [(75,47,61,13),29] -> 29|13 ? , 29|61 
        valid = True
        for y in range(1, len(pg)-1):
            last = pg[-1 - y]
            if preceeding(last, pg[:-1 -y], data) is True:
                valid = False
                break
           
        if (valid is True):
            valids.append(j)
        else: 
            invalids.append(j)

    return (valids, invalids)             


def preceeding(x, sub, data) -> bool:
    [sets, pages] = data
    keyset = sets.get(x)
    if keyset is None or sub == []:
        return True
    if (set(sub).intersection(set(keyset))):
        return True
    
    return False
