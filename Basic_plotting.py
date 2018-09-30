import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

ts = pd.Series(np.random.randn(1000)) # and with dataframe???
print(ts)


header = '\n'.join(
    # I like to make sure the header lines are at least utf8-encoded.
    ['1001','Daedalus; Stephen','Dublin; Ireland',
        'Keys','MINOS','1;1','1904;06;16;1922;02;02',
        'time_since_8am', # Ends up being the header name for the index.
    ]
)

with open('new.csv', 'w') as ict:
    # Write the header lines, including the index variable for
    # the last one if you're letting Pandas produce that for you.
    # (see above).
    for line in header:
        ict.write(line)

    # Just write the data frame to the file object instead of
    # to a filename. Pandas will do the right thing and realize
    # it's already been opened.
    ts.to_csv(ict)