import sys
import os
import os.path






def main():
    args = sys.argv
    if len(args) < 2:
        print('No CSV file given')
        return
    file_path = args[1]
    file_name = os.path.basename(args[1])
    print('Convert CSV file "' + file_name + '"')
    parse_file(file_path)
