import polynomial

p = polynomial.Polynomial( (1, 2, 3) )
q = polynomial.Polynomial( (-3, 4, 0, 0, 0) )
r = polynomial.Polynomial( (1, -2, -3) )
s = polynomial.Polynomial(p)
zero_poly = polynomial.Polynomial(0.0)


print("p ==", p)
print("q ==", q)
print("r ==", r)


print("-p ==", -p)
print("+p ==", p)

print("p + q ==", p + q)
print("q + p ==", q + p)
print("p - q ==", p - q)
print("q - p ==", q - p)

print("p * q ==", p * q)
print("q * p ==", q * p)

print("p + 1.0 ==", p + 1.0)
print("1.0 + p ==", 1.0 + p)
print("p - 2.0 ==", p - 2.0)
print("2.0 - p ==", 2.0 - p)
print("3.0 * p ==", 3.0 * p)
print("p * 3.0 ==", p * 3.0)

print("p + r ==", p + r)
print("p - r ==", p - r)

print("p * 0.0 ==", p * 0.0)
print("0.0 * p ==", 0.0 *p)

if p == q:
    print("p and q are equal")
else:
    print("p and q are not equal")
    
if p == s:
    print("p and s are equal")
else:
    print("p and s are not equal")
    
print("The degree of p is:", p.degree())
print("The degree of zero_poly is:", zero_poly.degree())

t = polynomial.Polynomial( (-1.0, 1.0))

for i in range(11):
    print(f"pow(t, {i}) ==", pow(t, i))


for poly in (p, q, r, s, t, zero_poly):
    print(repr(poly))
    
u = pow(t, 10)

for i in range(u.degree() + 10):
    print(f"The coefficient of x^{i} in u is:", u[i])
    
v = polynomial.Polynomial(())

for i in range(10):
    v += polynomial.monomial(i)

print("v ==", v)


print("p.prime() ==", p.prime())
print("q.prime() ==", q.prime())
print("v.prime() ==", v.prime())

print("p(1) ==", p(1))
print("q(2) ==", q(2))
print("r(3) ==", r(3))
print("u(4) ==", u(4))


if p:
    print("p evaluates as True when used as a bool")
else:
    print("p evaluates as False when used as a bool")
    
if zero_poly:
    print("zero_poly evaluates as True when used as a bool")
else:
    print("zero_poly evaluates as False when used as a bool")