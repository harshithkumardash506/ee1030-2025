


import ctypes            
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt


# --- Pure-Python midpoint function ---
def midpoint(x1, y1, x2, y2):
    """Return midpoint ((x1+x2)/2, (y1+y2)/2)."""
    return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)



 lib = ctypes.CDLL('./libmidpoint.so')
 lib.midpoint.argtypes = [
     ctypes.c_double, ctypes.c_double,
     ctypes.c_double, ctypes.c_double,
     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
 ]
 lib.midpoint.restype = None

 def midpoint_c(x1, y1, x2, y2):
     mx = ctypes.c_double()
     my = ctypes.c_double()
     lib.midpoint(x1, y1, x2, y2, ctypes.byref(mx), ctypes.byref(my))
     return (mx.value, my.value)


# --- Given points (Problem 1.2.15) ---
A = (4, 3)
B = (6, 4)
C = (5, -6)
D = (-3, 5)

# --- Midpoints of the diagonals ---
M_AC = midpoint(A[0], A[1], C[0], C[1])
M_BD = midpoint(B[0], B[1], D[0], D[1])

# Format for printing (like your trisection)
M_AC_fmt = (round(M_AC[0], 2), round(M_AC[1], 2))
M_BD_fmt = (round(M_BD[0], 2), round(M_BD[1], 2))

print("Midpoint AC =", M_AC_fmt)
print("Midpoint BD =", M_BD_fmt)


# --- Plotting (similar look/flow to trisection.py) ---
plt.figure(figsize=(8, 8))

# Polygon A-B-C-D-A
plt.plot([A[0], B[0], C[0], D[0], A[0]],
         [A[1], B[1], C[1], D[1], A[1]],
         'ro-', label='ABCD')

# Plot midpoints
plt.plot(*M_AC_fmt, 'bx', label='M_AC', markersize=9)
plt.plot(*M_BD_fmt, 'gx', label='M_BD', markersize=9)

# Labels for vertices
plt.text(A[0]+0.1, A[1],   f'A{A}', fontsize=12, ha='left')
plt.text(B[0]+0.1, B[1],   f'B{B}', fontsize=12, ha='left')
plt.text(C[0]+0.1, C[1],   f'C{C}', fontsize=12, ha='left')
plt.text(D[0]+0.1, D[1],   f'D{D}', fontsize=12, ha='left')

# Labels for midpoints
plt.text(M_AC_fmt[0]+0.1, M_AC_fmt[1],
         f'M_AC{M_AC_fmt}', fontsize=12, ha='left', color='blue')
plt.text(M_BD_fmt[0]+0.1, M_BD_fmt[1],
         f'M_BD{M_BD_fmt}', fontsize=12, ha='left', color='green')

# Match your script’s backend/style bits
mp.use("TkAgg")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Midpoint test for parallelogram (1.2.15)')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Save before show (path relative to codes/ -> figs/)
plt.savefig("../figs/1_2_15.png", dpi=300, bbox_inches='tight')
plt.show()
