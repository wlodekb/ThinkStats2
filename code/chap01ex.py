"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys

import nsfg
import thinkstats2


def preg_times(preg_map):
    return {k: len(v) for k, v in preg_map.items()}


def ReadFemResp(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df


def validate(resp):
    assert len(resp.index) == 13593
    assert resp.pregnum.value_counts(1) == 1267

    preg_map = nsfg.MakePregMap(resp)
    preg_times_map = preg_times(preg_map)

    for caseid, indicies in preg_map.items():
        pregnum_resp = resp.loc[indicies, 'pregnum']
        assert len(pregnum_resp) == preg_times_map[caseid]

        caseid_resp = resp.caseid[indicies]
        assert caseid_resp.tolist() == preg_map[caseid]


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(df)
    preg_times_map = preg_times(preg_map)

    for k, v in preg_times_map.items():
        print("subject %s was pregnant %s times" % (k, v))

    resp = ReadFemResp()
    validate(resp)
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
