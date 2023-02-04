import argparse

from expresso.append_to_chain import append_to_chain
from expresso.cli import process_command_line_args

def main():
    parser = argparse.ArgumentParser(description='Expresso Prototype')
    parser.add_argument('--append', dest='append', action='store_true',
                        help='Append a new block to the blockchain')
    parser.add_argument('--chain', dest='chain', action='store_true',
                        help='Display the current blockchain')
    args = parser.parse_args()

    if args.append:
        append_to_chain()
    elif args.chain:
        process_command_line_args()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()