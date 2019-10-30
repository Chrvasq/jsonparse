import json
import argparse

def input_args():
    parser = argparse.ArgumentParser(
        prog='jsonparse.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dir', type=str, help='set directory of json file')
    parser.add_argument('--output', type=str, help='set output directory')

    return parser.parse_args()

def parseJSON(file, outputfile):
    # read json data into variable
    with open(file) as json_file:
        json_data = json.load(json_file)
    # set concept objects to list
    concept_list = json_data['concepts']
    # new list to contain all atoms
    atoms_list = []
    for concept in concept_list:
        for atom in concept['atoms']:
            atoms_list.append(atom)

    # check for text key in atom
    # if text key, print out value otherwise continue
    text_list = []
    for atom in atoms_list:
        for key, value in atom.items():
            if key == 'text':
                textcontent = value
                text_list.append(textcontent)
            else:
                continue

    # write text_list to file
    with open(outputfile, 'w') as filehandle:
        for text in text_list:
            filehandle.write('%s\n' % text)

def main():
    args = input_args()
    dir = args.dir
    output = args.output

    parseJSON(dir, output)


if __name__ == '__main__':
    main()
