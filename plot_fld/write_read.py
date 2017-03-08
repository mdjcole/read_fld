#script for reading binaryangy_x_y.fld files produced by EUTERPE
import numpy as np
np.set_printoptions(threshold=np.nan)
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

def fthead(name):
    null = np.fromfile(file=name, dtype='>i4', count=1)

#open fortran-generated binary file
f = open('test.dat','rb')

#read header
cfftdata=ftread_double(f)
cfftmat=np.reshape(cfftdata,(100,16))

print(cfftdata)
print(cfftmat)
