import sys
import spm2olca.pack as pack
import spm2olca.parser as parser
import logging as log


def main():
    log.basicConfig(level=log.WARN, format='  %(levelname)s %(message)s')

    args = sys.argv
    if len(args) < 2:
        log.error('No CSV file given')
        return

    arg = args[1]
    if arg in ('-h', 'help'):
        print_help()
        return

    file_path = args[1]
    p = parser.Parser()
    p.parse(file_path)

    zip_file = file_path + '.zip'
    pack.Pack(p.methods).to(zip_file)


def print_help():
    text = '''
    Usage of spm2olca
    -----------------

    spm2olca <SimaPro CSV file with LCIA methods>
    '''
    print(text)