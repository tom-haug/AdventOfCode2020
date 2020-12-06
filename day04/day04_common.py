import functools
import re


def basic_password_rules():
    regex_birth_year = re.compile("byr:([^\\s]+)")
    regex_issue_year = re.compile("iyr:([^\\s]+)")
    regex_expiration_year = re.compile("eyr:([^\\s]+)")
    regex_height = re.compile("hgt:([^\\s]+)")
    regex_hair_color = re.compile("hcl:([^\\s]+)")
    regex_eye_color = re.compile("ecl:([^\\s]+)")
    regex_passport_id = re.compile("pid:([^\\s]+)")
    return [regex_birth_year, regex_issue_year, regex_expiration_year, regex_height, regex_hair_color,
            regex_eye_color, regex_passport_id]


def strict_password_rules():
    regex_birth_year = re.compile("byr:((19[2-9][0-9])|(200[0-2]))\\b")
    regex_issue_year = re.compile("iyr:((201[0-9])|(2020))\\b")
    regex_expiration_year = re.compile("eyr:((202[0-9])|(2030))\\b")
    regex_height = re.compile("hgt:((1[5-8][0-9]cm)|(19[0-3]cm)|(59in)|(6[0-9]in)|(7[0-6]in))\\b")
    regex_hair_color = re.compile("hcl:#([0-9a-f]{6})\\b")
    regex_eye_color = re.compile("ecl:((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))\\b")
    regex_passport_id = re.compile("pid:\\d{9}\\b")
    return [regex_birth_year, regex_issue_year, regex_expiration_year, regex_height, regex_hair_color,
            regex_eye_color, regex_passport_id]


def build_passport_list(input: str, regex_rules):
    lines = input.split("\n\n")

    valid_passports = []

    for line in lines:
        line = line.replace("\n", " ")
        total_matches = functools.reduce(lambda prev, cur: prev + (1 if cur.search(line) is not None else 0),
                                         regex_rules, 0)

        if total_matches == 7:
            valid_passports.append(line)
        else:
            print(line.replace("\n", " "))

    return valid_passports


def get_valid_passport_count(file_path, regex_rules):
    f = open(file_path, "r")
    input_str = f.read()

    valid_passwords = build_passport_list(input_str, regex_rules)

    return len(valid_passwords)
