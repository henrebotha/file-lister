import os
import argparse

parser = argparse.ArgumentParser(description="Enumerate files.")
parser.add_argument("-p", "--path", help="Path to enumerate", required=True)
parser.add_argument("-o", "--output", help="Output filename", default="")
args = parser.parse_args()

path = args.path

filenames = []

for filename in os.listdir(path):
    filenames.append(filename)

if args.output == "":
    output_file = "".join([c for c in path if c != "\\" and c != ":"]) + ".txt"
else:
    output_file = args.output

with open(output_file, "w") as f:
    for i in filenames:
        f.write(i)
        f.write("\n")
