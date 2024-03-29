import json
import argparse
import os
import glob


def input_args():
    parser = argparse.ArgumentParser(
        prog='jsonparse.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dir', type=str, help='set directory of json file', default='./json_files')
    # parser.add_argument('--output', type=str, help='set output directory', default='./text_files/text_file')

    return parser.parse_args()

def parseJSON(file, outputfile):
    # read json data into variable
    with open(file) as json_file:
        json_data = json.load(json_file)
    # set concept objects to list
    concept_list = json_data['concepts']
    # new list to contain all atoms
    atoms_list = []
    concept_count = 1
    for concept in concept_list:
        atoms_list.append({'concept': concept_count})
        for atom in concept['atoms']:
            atoms_list.append(atom)
        concept_count += 1

    # check for text key in atom
    # if text key, print out value otherwise continue
    text_list = []
    for atom in atoms_list:
        for key, value in atom.items():
            if key == 'text':
                textcontent = value
                text_list.append(textcontent)
            elif key == 'concept' and value == 1:
                textcontent = 'Concept ' + str(value)
                text_list.append(textcontent)
            elif key == 'concept':
                textcontent = '\nConcept ' + str(value)
                text_list.append(textcontent)
            else:
                continue

    # write text_list to file
    with open(outputfile, 'w') as filehandle:
        for text in text_list:
            filehandle.write('%s\n' % text)

def getFilePaths(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))
    return all_files

def main():
    args = input_args()
    dir = args.dir
    files = getFilePaths(dir)

    for file in files:
        file_name = os.path.basename(file)
        # output below contains filename without .json extension
        output = './text_files/' + os.path.splitext(file_name)[0]
        parseJSON(file, f'{output}.txt')


if __name__ == '__main__':
    main()
