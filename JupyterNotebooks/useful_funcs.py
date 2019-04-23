import numpy as np

def PAUSflux_to_ABmag(flux_PAUS):
    return 26 - 2.5 * np.log10(flux_PAUS)