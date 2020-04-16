#!/usr/bin/env python

# 1. finde alle jpgs im ordner aus 1 und speichere ihre pfade in einer zwischenvariablen ausgangsdaten (datentyp list)
# 2. für jedes element in der variablen ausgangsdaten, do:
# 2.1 transformiere nach  png
# 2.2 speichere als [dateiname] -.jpg +.png
# 3 gib aus, wie viele dateien transformiert wurden

import os  # os=operation system, importiert die befehle des Betriebssystems
from src import transform
import glob
import argparse


def main(ordner, ausgangstyp, ergebnistyp):

    pattern = ordner + "/*." + ausgangstyp
    ausgangsdaten = glob.glob(pattern)

    for element in ausgangsdaten:
        transform.transform_to(element, ergebnistyp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ordner", type=str)
    parser.add_argument("ausgangstyp", type=str)
    parser.add_argument("ergebnistyp", type=str)

    args = parser.parse_args()

    main(args.ordner, args.ausgangstyp, args.ergebnistyp)
