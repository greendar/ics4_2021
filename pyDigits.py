import time

q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

while True:
    if 4 * q + r - t < n * t:
        print(n)
        r, n = 10 * (r-n*t), ((10*(3*q+r))//t)-10*n
        q = 10 * q

    else:
        r, n = (2 * q + r) * l, (q * (7 * k) + 2 + (r*l))//(t*l)
        q, t, l, k = k*q, l*t, l+2, k+1

    time.sleep(0.1)

    #print(f"q: {q}   r: {r}   t: {t}   k: {k}   n: {n}   l: {l}")
