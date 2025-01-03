from fileinput import input
import re

'''
Some of the parser code for regex generated by regex101.com
'''
def parse_input(file_name = "") -> list:

    list = []

    if not file_name:
        file_name = './input.txt'

    regex = r"mul\((\d*\,\d*)\)"
    
    for line in input(files=(file_name)):
    
        matches = re.finditer(regex, line, re.MULTILINE | re.IGNORECASE)

        for matchNum, match in enumerate(matches, start=1):
            
            #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

                str_pairs = match.group(groupNum)
                [lft, rgt] = re.split(r",", str_pairs) 
                list.append([int(lft), int(rgt)])
             

    return list

def parse_input_ext(file_name = "") -> list:

    list = []

    if not file_name:
        file_name = './input.txt'

    regex = r"mul\((\d*\,\d*)\)|(don't\(\))|(do\(\))"
    
    for line in input(files=(file_name)):
    
        matches = re.finditer(regex, line, re.MULTILINE | re.IGNORECASE)

        for matchNum, match in enumerate(matches, start=1):
            
            #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

                str_pairs = match.group(groupNum)
                if str_pairs is not None:
                    #print(str_pairs)
                    if (str_pairs == "don't()"):
                        list.append("-")
                    elif str_pairs.endswith("do()"):
                        list.append("+")
                    else:
                        [lft, rgt] = re.split(r",", str_pairs) 
                        list.append([int(lft), int(rgt)])
             

    return list
