from fileinput import input



class Disk:
    _data = None
    _max_pos = 0
        
    def __init__(self):
        self._data = {}
        pass


    def fill(self):
        max_pos = self._max_pos
        data = self._data
        right = max_pos
        left = 0
        while (left <= max_pos):
            chunk = data[left]
            rchunk = data[right]

            if (left == right):
                break
           
            rev = [rchunk['id']] * rchunk['val']
        
            if chunk['free'] > 0:
                strlen = min(chunk['free'], rchunk['val'])
                fill = rev[0:strlen]
                
                chunk['data'] += fill
                rchunk['val'] -=  strlen
                chunk['free'] -= len(fill)

            if chunk['free'] == 0:
                left+=1
                if rchunk['val'] == 0:
                    right-=1
            elif rchunk['val'] == 0 and chunk['free'] > 0:
                right-=1
                
        return self.sum_chunks(data)


    def fill_fit(self):
        max_pos = self._max_pos
        data = self._data
        right = max_pos
        left = 0
        skip = []
        skipped = 0
        while (right >= 0):
            rchunk = data[right]
            avail = rchunk['val']
            
            while (avail not in skip and left <= max_pos and left != right):
                chunk = data[left]
                if chunk['free'] >= avail:
                    chunk['data'] += [rchunk['id']] * rchunk['val']
                    chunk['free'] -= rchunk['val']
                    data[right - 1]['free'] += rchunk['val'] 
                    rchunk['val'] = 0
                    break

                left += 1

            '''
            # check if we should skip the avail-value
            # works good on test case, prod data yields
            # no measurable improvements
            can_skip = True    
            tleft = left + 1
            while (tleft <= max_pos):
                if data[tleft]['free'] >= avail:
                    can_skip = False
                    break
                tleft += 1
            if can_skip:
                print(f"CAN SKIP: {avail}")
                skip.append(avail)            
            '''
            right -= 1
            left = 0

        return self.sum_chunks(data)


    def sum_chunks(self, data) -> int:
        res = 0 
        idx = 0   
        for i in data:
            chunk = data[i]
            
            for i in range(0, chunk['val']):
                res += idx * chunk['id']
                idx += 1        

            for i in range(0, len(chunk['data'])):
                res += idx * int(chunk['data'][i])
                idx += 1        

            idx += chunk['free']  
        return res


def parse_input(file_name = "") -> Disk:

    disk = Disk()

    if not file_name:
        file_name = './input.txt'

    lines = []
    for l in input(files=(file_name)):
        lines.append(l)

    if len(lines) > 1:
        raise Exception("whoops.")    



    line = lines[0].strip()
    
    chunk = 0
    pos = 0
    for j in range(0, len(line)):
        c = line[j]
        match (chunk):
            case 0:
                disk._max_pos = pos
                disk._data[pos] = {
                    'val' : int(c),
                    'data' : [],
                    'id' : pos,
                    'free' : 0
                }
            case 1:
                disk._data[pos]['free'] = int(c)
                pos += 1

        chunk = (chunk + 1) % 2
            

    return disk


'''
PART 1
'''
def part1_process(disk: Disk) -> int:
        
    return disk.fill()
    pass

'''
PART 2
'''
def part2_process(disk: Disk) -> int:
    
    return disk.fill_fit()
    pass
    
'''
HELPER
'''
