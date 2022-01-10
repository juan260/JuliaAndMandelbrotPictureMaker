from PlotMandelbrot import *
from PlotJulia import *

# This first example creates a list of values for "c" in the Julia equation
# and plots the Julia set for each one of them, storing them with names like
# JuliaSet.png
cs = [complex(0,0.6),complex(0,0.62),complex(0,0.63),complex(0,0.633),\
    complex(0,0.636), complex(0,0.64),complex(0,0.65), complex(0,0.66)]
for c in cs:
    plotJulia(c, name='JuliaSet'+str(c)+'.png')
    print("JuliaSet with C = " + str(c) + " done!")


# This second example plots the mandlebrot set zooming into the point called base
# Every time we zoom in, each axis halves in length.
base=complex(-0.7652,0.0982)
c=1

for i in range(15):
    c=c/2
    
    plotMandelbrot(complex(0,0),name='mandl'+str(c)+'-'+str(base)+'.png', xmin=base.real-c, xmax=base.real+c, \
                   ymin=base.imag-c, ymax=base.imag+c)
    print("Mandelbrot Set with zoom " + str(i) + " out of 15 done!")
    
# In this one we are zooming into a different point, and we zoom more slowly, but it's basically the same process
base=complex(-0.10450092, 0.926302)
c=1*((3/5)**36)
j=0
for i in range(37,45):
    c=c*3/5
    plotMandelbrot(complex(0,0),name='mandln'+str(i)+'c'+str(c)+'-'+str(base)+'.png', xmin=base.real-c, xmax=base.real+c, \
                   ymin=base.imag-c, ymax=base.imag+c)
    print("Mandelbrot Set with zoom " + str(j) + " out of " + str(45-37) + " done!")
    j += 1