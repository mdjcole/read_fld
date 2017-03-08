#script for reading binaryangy_x_y.fld files produced by EUTERPE
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an

#functions for reading fortran records - before and after each record is a 4 byte int
#stating the length of that record in bytes, which must be omitted
def ftread_string():
    null = np.fromfile(file=f, dtype='>i4', count=1)
    out = np.fromfile(file=f, dtype='i1', count=null[0])
    null = np.fromfile(file=f, dtype='>i4', count=1)
    return out

def ftread_double():
    null = np.fromfile(file=f, dtype='>i4', count=1)
    out = np.fromfile(file=f, dtype='>f8', count=null[0]//8)
    null = np.fromfile(file=f, dtype='>i4', count=1)
    return out

def ftread_int():
    null = np.fromfile(file=f, dtype='>i4', count=1)
    out = np.fromfile(file=f, dtype='>i4', count=null[0]//4)
    null = np.fromfile(file=f, dtype='>i4', count=1)
    return out

def ftread_longint():
    null = np.fromfile(file=f, dtype='>i4', count=1)
    out = np.fromfile(file=f, dtype='>i8', count=null[0]//8)
    null = np.fromfile(file=f, dtype='>i4', count=1)
    return out

def fthead():
    null = np.fromfile(file=f, dtype='>i4', count=1)

def cycread(f):
#read cyclic data
#header
    fthead(f)
    simtime=np.fromfile(file=f, dtype='>f8', count=1)
    mmin_filter=np.fromfile(file=f, dtype='>i8', count=1)
    im_number=np.fromfile(file=f, dtype='>i8', count=1)
    fthead(f)
#body
    fthead(f)
    cfftlist=np.fromfile(file=f, dtype='>c16', count=4224)
    fthead(f)
#reshape into array (mode number, radial location)
    cfftdata=np.reshape(cfftlist,(128,33))
    return cfftdata

#switches
s = 1

#open fortran-generated binary file
f = open('prod_msdmp_angy_phi_pol.fld','rb')

#read header
codename=ftread_string()
VERNUM=ftread_double()
zverformat=ftread_double()
NUM_INT_HEADER=ftread_int()
int_header=ftread_longint()
NUM_REAL_HEADER=ftread_int()
zreal_header=ftread_double()

#print(codename)
#print(VERNUM)
#print(zverformat)
#print(NUM_INT_HEADER)
#print(int_header)
#print(NUM_REAL_HEADER)
#print(zreal_header)

nums=int_header[21]
if s:
  sgrid=np.arange(0.,1.,1./nums)
else:
  sgrid=np.arange(0.,1.,1./nums)**0.5
  
def cycdat():
#read cyclic data
#header
    fthead()
    simtime=np.fromfile(file=f, dtype='>f8', count=1)
    mmin_filter=np.fromfile(file=f, dtype='>i8', count=1)
    im_number=np.fromfile(file=f, dtype='>i8', count=1)
    fthead()
#body
    fthead()
    cfftlist=np.fromfile(file=f, dtype='>c16', count=nums*im_number[0])
    fthead()
#reshape into array (mode number, radial location)
    cfftdata=np.reshape(cfftlist,(128,33))  
    return simtime, cfftdata

#plt.plot(sgrid,phigrid)
#plt.title(simtime)
#plt.show()

simtime, cfftdata=cycdat()
phigrid=np.absolute(cfftdata[:,26])
normvar=max(phigrid)
phigrid=phigrid/normvar

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(sgrid, phigrid, 'r-')

while 1:
    line1.set_ydata(phigrid)
    fig.canvas.draw()
    fig.canvas.flush_events()
    simtime, cfftdata=cycdat()
    phigrid=np.absolute(cfftdata[:,26])
    normvar=max(phigrid)
    phigrid=phigrid/normvar
