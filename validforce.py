import argparse
import xlrd
import os
import logging
import coloredlogs

def parse():
    parser = argparse.ArgumentParser(description='Turn scorify-generated data sheets into NDA-compatible ones.')
    subparsers = parser.add_subparsers(dest='subcommand', title='subcommands', description='valid subcommands', required=True)

    single = subparsers.add_parser('manual')
    single.add_argument('mutator_location', help='How to mutate stuff')
    single.add_argument('input_data', help='The data to pull from')

    auto = subparsers.add_parser('auto', help='Do everything we know how to do')

    return parser.parse_args()


def generate_automatic():
    # load file
    workbook = xlrd.open_workbook(args.input_data)
    sheet = workbook.sheet_by_index(0)

    for row in range(1,sheet.nrows):
        something = sheet.cell_value(row,4)
        logging.error('Not implemented!')


if __name__ == "__main__":
    args = parse()

    if args.subcommand == 'auto':
        generate_automatic()
    elif args.subcommand == 'single':
        logging.error('Not implemented!')
