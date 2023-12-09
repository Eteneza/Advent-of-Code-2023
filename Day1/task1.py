import re

with open("data1.txt") as f:
    data = f.read().strip()


def calibration(data):
    ls = data.split("\n")
    ns = [re.findall("\d", x) for x in ls]
    return sum(int(n[0] + n[-1]) for n in ns)


# Part 1
print(calibration(data))

# Part 2
data = (
    data.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)
#One letter used to compose one digit is not "burnt" and so it can be used to compose another digit.
print(calibration(data))


#Another way to replace the numbers

# .replaceAll('one', 'o1e')
# .replaceAll('two', 't2o')
# .replaceAll('three','t3e')
# .replaceAll('four', '4') // no other number starts with f nor ends in r
# .replaceAll('five', 'f5e')
# .replaceAll('six', '6') // no number starts with s nor ends in x
# .replaceAll('seven','7n') // no number starts with s
# .replaceAll('eight','e8t')
# .replaceAll('nine', 'n9e')