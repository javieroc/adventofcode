import re

passports = []
num_valid_passports = 0

def isValid(passport):
    if len(passport.keys()) != 7:
        return False
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False
    if int(passport['eyr']) < 2020 or  int(passport['eyr']) > 2030:
        return False
    if 'cm' not in passport['hgt'] and 'in' not in passport['hgt']:
        return False
    if 'cm' in passport['hgt'] and (passport['hgt'] < '150cm' or passport['hgt'] > '193cm'):
        return False
    if 'in' in passport['hgt'] and (passport['hgt'] < '59in' or passport['hgt'] > '76in'):
        return False
    if not re.search(r"^#([a-f0-9]{6})$", passport['hcl']):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.search(r"^\d{9}$", passport['pid']):
        return False
    return True

with open("input.txt", "r") as file:
    passport = {}
    for line in file:
        if line == '\n':
            passports.append(passport)
            passport = {}
            continue
        fields = line.replace('\n', '').split(' ')
        for field in fields:
            key,value = field.split(':')
            if key != 'cid':
                passport[key] = value
    passports.append(passport)

for passport in passports:
    if isValid(passport):
        print(passport['hgt'])
        num_valid_passports = num_valid_passports + 1

print(f"Num of valid passports: {num_valid_passports}")
