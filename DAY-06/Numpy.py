#numpy
import numpy as np
arr = np.array([19,33,66,32,76,np.nan,44,np.nan])

print(np.nanmean(arr))
print(np.nanmedian(arr))
print(np.nanstd(arr))
