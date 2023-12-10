import string

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day4input.txt")

required = [
    "byr", #(Birth Year)
    "iyr", #(Issue Year)
    "eyr", #(Expiration Year)
    "hgt", #(Height)
    "hcl", #(Hair Color)
    "ecl", #(Eye Color)
    "pid", #(Passport ID)
]

optional = [
    "cid", #(Country ID)
]

# class Passport:
#     def __init__(self):
#         self.byr #(Birth Year)
#         self.iyr #(Issue Year)
#         self.eyr #(Expiration Year)
#         self.hgt #(Height)
#         self.hcl #(Hair Color)
#         self.ecl #(Eye Color)
#         self.pid #(Passport ID)
#         self.cid #(Country ID)
#         self.valid = false

passports = []

passport = dict()
passports.append(passport)

for line in f:
    
    if line == "\n":
        passport = dict()
        passports.append(passport)
        continue
    
    fields = line.split(" ")
    for field in fields:
        key,value = field.split(":")
        passport[key] = value

valids = 0
for passport in passports:

    for k,v in passport.items():
        passport[k] = v.strip()

    if all(item in passport.keys() for item in required):

        #Continue validation here

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        byr = passport['byr']
        if not (len(byr) == 4 and byr.isdigit() and int(byr) >= 1920 and int(byr) <= 2002):
            print('byr',byr)
            continue

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        iyr = passport['iyr']
        if not (len(iyr) == 4 and iyr.isdigit() and int(iyr) >= 2010 and int(iyr) <= 2020):
            print('iyr',iyr)
            continue

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        eyr = passport['eyr']
        if not (len(eyr) == 4 and eyr.isdigit() and int(eyr) >= 2020 and int(eyr) <= 2030):
            print('eyr',eyr)
            continue

        # hgt (Height) - a number followed by either cm or in:
        hgtNumber = passport['hgt'][:-2]
        hgtUnit = passport['hgt'][-2:]
        if not hgtNumber.isdigit():
            print('hgtNumber',hgtNumber)
            continue
        else:
            hgtNumber = int(hgtNumber)

        # If in, the number must be at least 59 and at most 76.
        if hgtUnit == "in":
            if not (hgtNumber >= 59 and hgtNumber <= 76):
                print('hgtNumber',hgtNumber)
                continue
        # If cm, the number must be at least 150 and at most 193.
        elif hgtUnit == "cm":
            if not (hgtNumber >= 150 and hgtNumber <= 193):
                print('hgtNumber',hgtNumber)
                continue
        else:
            print('hgtUnit',hgtUnit)
            continue

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        hcl = passport['hcl']
        allowedChars = ['a','b','c','d','e','f'] + list(string.digits)
        if not (hcl[0] == '#' and len(hcl) == 7 and set(hcl[1:]).issubset(allowedChars) ):
            print('hcl',hcl)
            continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        allowedEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        ecl = passport['ecl']
        if not (ecl in allowedEyeColors):
            print('ecl',ecl)
            continue

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        pid = passport['pid']
        if not (len(pid) == 9 and pid.isdigit()):
            print('pid',pid)
            continue

        valids += 1

print(valids)