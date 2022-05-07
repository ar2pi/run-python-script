#!/usr/bin/env python

import yaml

CONFIG_FILE = "config.yaml"

if __name__ == "__main__":
    config = yaml.safe_load(open(CONFIG_FILE, 'r'))
    print(config)
