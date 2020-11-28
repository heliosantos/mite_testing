import csv
from mite.datapools import RecyclableIterableDataPool
import pathlib
import os.path


with open(os.path.join(pathlib.Path(__file__).parent.absolute(), 'names.csv')) as f:
    names = [(r['First Name'], ) for r in csv.DictReader(f)]

names_datapool = RecyclableIterableDataPool(names)
