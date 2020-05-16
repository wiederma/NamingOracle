#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

def process(name):
    print('Name to process is: ' + name)

    #
    # Oracle magic goes here ...
    #


def main():
    parser = argparse.ArgumentParser(
        description='''This applications reads a name string from the
        commandline and oracles about its meaning.''',
    )
    parser.add_argument(
        '--name',
        type=str,
        default='',
        help='put the name you want to process in \' \'',
    )
    parser.add_argument(
        '--demo',
        action='store_true',
        default=False,
        help='show a demo',
    )
    args = parser.parse_args()

    if args.demo == True:
        process('Pippilotta Viktualia Rollgardina Pfefferminza Efraimstochter Langstrumpf')
    else:
        process(args.name)

#===============================================================================
# Main
#
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Shutting down', file=sys.stderr)
    except Exception as e:
        print(e)
