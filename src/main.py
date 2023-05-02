#!/usr/bin/env python

import argparse
import logging
import os
import sys
from dotenv import load_dotenv
import requests
import yaml

CONFIG_FILE = 'config.yaml'

# Load env
load_dotenv()

# Load config
config = yaml.safe_load(open(CONFIG_FILE, 'r'))

# Load command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

# Load logger
logging_level = logging.DEBUG if args.verbose else logging.INFO
logging.basicConfig(
    encoding='utf-8',
    level=logging_level,
    datefmt='%Y-%m-%dT%H:%M:%S',
    format='%(asctime)s %(levelname)s: %(message)s',
)

logging.debug(os.environ)
logging.debug(config)
logging.debug(args)


def main():
    logging.info('Running...')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
