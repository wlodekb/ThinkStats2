"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
import nsfg
import thinkstats2


def ValidatePregnum(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)
    for i, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[i]
        if len(preg_map[caseid]) != pregnum:
            return False
    return True


def CleanFemResp(df):
    pass


def ReadFemResp(dct_file="2002FemResp.dct", dat_file="2002FemResp.dat.gz"):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemResp(df)
    return df


def main(script):
    """Tests the functions in this module.

    script: string script name
    http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=R&subSec=7869&srtLabel=606835
    """
    resp = ReadFemResp()
    assert len(resp) == 7643
    assert (resp.pregnum.value_counts()[1] == 1267)

    assert ValidatePregnum(resp)


if __name__ == '__main__':
    main(*sys.argv)
