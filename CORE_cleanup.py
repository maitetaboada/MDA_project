# ----------------------------------------------------------------
# Clean CORE files.
#
# (C) 2020 Laurens Bosman, Discourse Processing Lab, SFU
# Released under GNU General Public License (GPL)
# email lbosman@sfu.ca
# ----------------------------------------------------------------

import os
import re

def main(corpusFolder):
    os.mkdir('./CORE_clean')
    for folder in os.listdir(corpusFolder):
        os.mkdir('./CORE_clean/' + folder)
        for file in os.listdir(corpusFolder + folder):
            i = 0
            with open(corpusFolder + folder + "/" + file, 'r', encoding="latin-1") as inputFile:
                for line in inputFile:
                    if line == "\n":
                        i += 1
                        break
                    i += 1
            with open(corpusFolder + folder + "/" + file, 'r', encoding="latin-1") as inputFile:
                if (i > 7):
                    i = 6
                lines = inputFile.readlines()[i:]
            with open('./CORE_clean/'+ folder + '/' + file, 'w') as output:
                for line in lines:
                    first = re.sub(r'<.{1,3}> ', '', line)
                    second = re.sub(r'_{4,100} ', '', first)
                    third = re.sub(r'-{4,100}', '', second)
                    fourth = re.sub(r'~{4,100}', '', third)
                    output.write(fourth)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='remove artifacts from data collection process')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus folder')
	args = parser.parse_args()
	main(args.corpusPath) 
