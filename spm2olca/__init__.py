import sys
import spm2olca.pack as pack
import spm2olca.parser as parser


def main():
    args = sys.argv
    if len(args) < 2:
        print('No CSV file given')
        return

    arg = args[1]
    if arg in ('-h', 'help'):
        print_help()
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


def print_help():
    text = '''
    Usage of spm2olca
    -----------------

    spm2olca <SimaPro CSV file with LCIA methods>
    '''
    print(text)