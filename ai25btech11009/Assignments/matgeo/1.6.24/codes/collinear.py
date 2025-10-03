import matplotlib.pyplot as plt

# Points
A = (2, 3)
B = (4, 0)   # k = 0
C = (6, -3)

# Line through A and C
x_vals = [A[0], C[0]]
y_vals = [A[1], C[1]]

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, 'b-', label="Line through A, B, C")
plt.scatter(*A, color='r')
plt.text(A[0]+0.1, A[1], "A(2,3)", fontsize=10, color='r')
plt.scatter(*B, color='g')
plt.text(B[0]+0.1, B[1], "B(4,0)", fontsize=10, color='g')
plt.scatter(*C, color='purple')
plt.text(C[0]+0.1, C[1], "C(6,-3)", fontsize=10, color='purple')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Collinear Points for k = 0")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
