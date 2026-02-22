# Matrix Inversion Using Adjugate Method (From Scratch)

## 📌 Overview
This project implements matrix inversion for a 3×3 matrix using the classical Adjugate (Adjoint) Method.

The goal of this implementation is educational:  
to better understand how matrix inversion works internally without relying on high-level libraries such as NumPy's built-in inverse function.

This project was developed as a personal practice exercise.

---

## 🧠 What This Project Includes

- Determinant calculation
- Cofactor matrix computation
- Adjugate (Adjoint) matrix calculation
- Matrix inversion using:

\[
A^{-1} = \frac{1}{det(A)} \times adj(A)
\]

- A test function that verifies the algorithm by checking:

\[
A \times A^{-1} = I
\]

(where I is the identity matrix)

---

## ⚙️ How the Algorithm Works

1. Compute the determinant of the main matrix.
2. If determinant ≠ 0:
   - Compute the cofactor matrix.
   - Compute the adjugate matrix.
   - Multiply by 1/det(A) to obtain the inverse.
3. Verify correctness by multiplying the original matrix by its inverse.
4. The result should be the Identity Matrix.

---

## 🛠️ Technologies Used

- Python
- NumPy (for array handling only)
- Manual matrix multiplication (no built-in inverse functions used)

---

## ▶️ How to Run

Make sure you have Python and NumPy installed:

`bash
pip install numpy
