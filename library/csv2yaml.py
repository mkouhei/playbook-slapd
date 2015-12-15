# -*- coding: utf-8 -*-
import sys
import csv
import yaml
import os.path



def basename(filepath):
    return os.path.basename(os.path.splitext(filepath)[0])


def change_ext(filepath):
    return '{0}.yml'.format(basename(filepath))


def vars_dir(filepath):
    return os.path.join(os.path.dirname(os.path.dirname(filepath)), 'vars')


def yaml_path(csvpath):
    return os.path.join(vars_dir(csvpath), change_ext(csvpath))
                        

def convert(csvpath):
    key = basename(csvpath)
    with open(csvpath, 'rb') as fobj:
        reader = csv.DictReader(fobj, delimiter=',', quotechar='"')
        data = {'{0}'.format(key): [i for i in reader]}
    with open(yaml_path(csvpath), 'w') as fobj:
        fobj.write(yaml.safe_dump(data))


if __name__ == '__main__':
    convert(sys.argv[1])
