#script for reading binaryangy_x_y.fld files produced by EUTERPE
import numpy as np
import struct

#functions for reading fortran records - before and after each record is a 4 byte int
#stating the length of that record in bytes, which must be omitted
def ftread_string(name):
    null = np.fromfile(file=name, dtype='>i4', count=1)
    out = np.fromfile(file=name, dtype='i1', count=null[0])
    null = np.fromfile(file=name, dtype='>i4', count=1)
    return out

def ftread_double(name):
    null = np.fromfile(file=name, dtype='>i4', count=1)
    out = np.fromfile(file=name, dtype='>f8', count=null[0]//8)
    null = np.fromfile(file=name, dtype='>i4', count=1)
    return out

def ftread_int(name):
    null = np.fromfile(file=name, dtype='>i4', count=1)
    out = np.fromfile(file=name, dtype='>i4', count=null[0]//4)
    null = np.fromfile(file=name, dtype='>i4', count=1)
    return out

def ftread_longint(name):
    null = np.fromfile(file=name, dtype='>i4', count=1)
    out = np.fromfile(file=name, dtype='>i8', count=null[0]//8)
    null = np.fromfile(file=name, dtype='>i4', count=1)
    return out

#open fortran-generated binary file
f = open('prod_msdmp_angy_phi_pol.fld','rb')

#read header
codename=ftread_string(f)
VERNUM=ftread_double(f)
zverformat=ftread_double(f)
NUM_INT_HEADER=ftread_int(f)
int_header=ftread_longint(f)
NUM_REAL_HEADER=ftread_int(f)
zreal_header=ftread_double(f)

print(codename)
print(VERNUM)
print(zverformat)
print(NUM_INT_HEADER)
print(int_header)
print(NUM_REAL_HEADER)
print(zreal_header)

#read cyclic data


