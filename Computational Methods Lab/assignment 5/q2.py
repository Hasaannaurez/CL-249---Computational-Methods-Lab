# Evaluate the following:
    # ∫∫(x^2 -3y^2 +x*y^3)dx dy 
    # x ∈ [0, 4], y ∈ [-2, 2]
# 1. using multi application trapezoidal rule, n=2
# 2. using simpsons 1/3rd rule

#compute the % error for both 1. and 2.
    # for 1. E = ((b-a)^3 * f''(x*))/12n^2, for x* the point where  max|f''(x)|
    # for 2. E = ((b-a)^5 * f''''(x*))/90

def g(y):
    return (64.0/3.0) - 12.0*(y**2) + 8.0*(y**3)

I_exact = 64.0/3.0

# y-grid with n=2 subintervals
a, b = -2.0, 2.0
n = 2
h = (b - a) / n
y0, y1, y2 = a, a + h, b

# 1) Composite trapezoidal rule (n=2)
I_trap = (h/2.0) * (g(y0) + 2.0*g(y1) + g(y2))

# 2) Composite Simpson's 1/3 rule (n=2)
I_simp = (h/3.0) * (g(y0) + 4.0*g(y1) + g(y2))

# Actual % errors vs exact
trap_pct_actual = abs(I_trap - I_exact) / abs(I_exact) * 100.0
simp_pct_actual = abs(I_simp - I_exact) / abs(I_exact) * 100.0

# Trapezoid: E = ((b-a)^3 * max|g''(y)|) / (12 n^2)
# g(y) = 64/3 - 12y^2 + 8y^3
# g'(y) = -24y + 24y^2
# g''(y) = -24 + 48y  -> max |g''| on [-2,2] occurs at endpoints
max_abs_g2 = max(abs(-24.0 + 48.0*(-2.0)), abs(-24.0 + 48.0*(2.0)))  # = max(120, 72) = 120
E_trap_bound = ((b - a)**3 * max_abs_g2) / (12.0 * (n**2))
trap_pct_bound = (E_trap_bound / abs(I_exact)) * 100.0

# Simpson 1/3: E = ((b-a)^5 * max|g''''(y)|) / 90
# g'''(y) = 48, g''''(y) = 0  -> bound = 0
E_simp_bound = 0.0
simp_pct_bound = 0.0

print("Exact integral:", I_exact)

print("\nComposite Trapezoidal (n=2):", I_trap)
print("Actual % error:       {:.6f}%".format(trap_pct_actual))
print("Bound via formula:    E_T = {:.6f}  (≈ {:.6f}%)".format(E_trap_bound, trap_pct_bound))

print("\nComposite Simpson 1/3 (n=2):", I_simp)
print("Actual % error:       {:.6f}%".format(simp_pct_actual))
print("Bound via formula:    E_S = {:.6f}  (≈ {:.6f}%)".format(E_simp_bound, simp_pct_bound))
