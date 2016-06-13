"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=R&subSec=7869&srtLabel=606835
    """
    dct = thinkstats2.ReadStataDct("2002FemResp.dct")
    df = dct.ReadFixedWidth("2002FemResp.dat.gz", compression='gzip')
    pregnum = df.pregnum.value_counts().sort_index()
    preg_map = nsfg.MakePregMap(df)
    print(preg_map)
    print(pregnum)


if __name__ == '__main__':
    main(*sys.argv)
