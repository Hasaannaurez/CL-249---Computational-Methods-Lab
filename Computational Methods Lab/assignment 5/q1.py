import math

t =[0,1,5.5,10,12,14,16,18,20,24] # time in hours
c =[1,1.5,2.3,2.1,4,5,5.5,5,3,1.2] # concentration in mg/L

# The flowrate in m^3/s can be computed using
# Q = 10 +10 *Sin((2*pi*(t-10))/24)

Q = [10 + 10 * math.sin(2 * math.pi * (ti - 10)/24) for ti in t]
# print("Q values",Q)

QC = [ci * Qi for ci, Qi in zip(c, Q)]

#To use a numerical integration method to determine the flow weighted average concentration leaving the reactor

# c* = ∫(c(t) * Q(t)) dt / ∫Q(t) dt , where t ∈ [0,24]

#using simpsons 1/3rd composition rule

def simpsons_rule(x, y):
    n = len(x)
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires an even number of intervals")
    h = (x[-1] - x[0]) / (n - 1)
    integral = y[0] + y[-1]
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * y[i]
        else:
            integral += 4 * y[i]
    return integral * h / 3

denominator = simpsons_rule(t, Q)
numerator = simpsons_rule(t, QC)

c_star = numerator / denominator
print("Flow weighted average concentration (c*):", c_star)