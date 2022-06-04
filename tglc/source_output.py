import os
from tglc.ffi import *
import multiprocessing
from multiprocessing import Pool
from functools import partial


def ffi_to_source(sector=1, local_directory=''):
    '''
    Cut calibrated FFI to source.pkl
    :param sector: int, required
    TESS sector number
    :param local_directory: string, required
    output directory
    '''
    # local_directory = f'/mnt/d/TESS_Sector_17/'
    os.makedirs(local_directory + f'lc/', exist_ok=True)
    os.makedirs(local_directory + f'epsf/', exist_ok=True)
    os.makedirs(local_directory + f'ffi/', exist_ok=True)
    os.makedirs(local_directory + f'source/', exist_ok=True)

#     with Pool() as p:
#         p.map(partial(cut_ffi, camera, sector, 150, local_directory), [1, 2, 3, 4])
    for i in range(16):
        cut_ffi(camera=1 + i // 4, ccd=1 + i % 4, sector=sector, size=150, path=local_directory)


if __name__ == '__main__':
    sector = 1
    ffi_to_source(sector=sector, local_directory=f'/home/tehan/data/sector{sector:04d}/')