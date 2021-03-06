#script for reading binary angy_x_y.fld files produced by EUTERPE
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

#read cyclic data containing phi/apar radial perturbations for each fourier mode
def cycdat():
#read cyclic header for given timestep
    fthead()
    simtime=np.fromfile(file=f, dtype='>f8', count=1)
    mmin_filter=np.fromfile(file=f, dtype='>i8', count=1)
    im_number=np.fromfile(file=f, dtype='>i8', count=1)
    fthead()
#read body
    fthead()
    cfftlist=np.fromfile(file=f, dtype='>c16', count=nums*im_number[0])
    fthead()
#reshape into array (mode number, radial location)
    cfftdata=np.reshape(cfftlist,(nums,im_number[0]))  
#return data for all modes at all radial locations
    return simtime, cfftdata

#switches
s = 1

#open fortran-generated binary file
f = open('prod_msdmp_angy_phi_pol.fld','rb')

#read file header
codename=ftread_string()
VERNUM=ftread_double()
zverformat=ftread_double()
NUM_INT_HEADER=ftread_int()
int_header=ftread_longint()
NUM_REAL_HEADER=ftread_int()
zreal_header=ftread_double()

#switch for s or r x-axis
nums=int_header[21]
if s:
  sgrid=np.arange(0.,1.,1./nums)
else:
  sgrid=np.arange(0.,1.,1./nums)**0.5

#get values for first time step and normalise
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

    #get values for next time step
    simtime, cfftdata=cycdat()
    phigrid=np.absolute(cfftdata[:,26])
    normvar=max(phigrid)
    phigrid=phigrid/normvar
