__author__ = 'Lindsay Ward'

INPUT_FILE = "text.txt"
OUTPUT_FILE = "out.txt"

in_file = open(INPUT_FILE, "r")

# print(repr(in_file.read()))

# print(in_file.readlines())

# for line in in_file.readlines():
#     print("! ", line.strip())

# discard first line
in_file.readline()

for line in in_file:
    print("! ", line.strip())

in_file.close()


out_file = open(OUTPUT_FILE, "a")
print("Bob", file=out_file)
out_file.close()