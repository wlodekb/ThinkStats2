import first
import nsfg
import thinkstats2
import thinkplot


def Diffs(t):
    first = t[0]
    rest = t[1:]
    diffs = [first - x for x in rest]
    return diffs

def PairWiseDifference(live):
    live = live[live.prglngth >= 37]
    preg_map = nsfg.MakePregMap(live)
    diffs = []
    for caseid, indicies in preg_map.items():
        lengths = live.loc[indicies].prglngth.values
        if len(lengths) >= 2:
            diffs.extend(Diffs(lengths))
    return diffs


if __name__ == '__main__':
    live, first, other = first.MakeFrames()
    diffs = PairWiseDifference(live)
    mean = thinkstats2.Mean(diffs)
    print('Mean difference between pairs', mean)

    pmf = thinkstats2.Pmf(diffs)
    thinkplot.Hist(pmf, align="center")
    thinkplot.Show(xlabel='Difference in weeks',
                   ylabel='PMF')
