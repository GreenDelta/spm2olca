import sys
import spm2olca.pack as pack
import spm2olca.parser as parser


def main():
    args = sys.argv
    if len(args) < 2:
        print('No CSV file given')
        return
    file_path = args[1]
    p = parser.Parser()
    p.parse(file_path)
    for m in p.methods:
        print('  ' + m.name)
        for c in m.impact_categories:
            print('    ' + c.name + ' ' + str(len(c.factors)))

    zip_file = file_path + '.zip'
    pack.Pack(p.methods).to(zip_file)