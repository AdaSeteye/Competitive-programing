def theatre_square(n, m, a):
    if n//a == n/a and m//a == m/a:
        s1 = n/a
        s2 = m/a
    elif n//a == n/a and m//a != m/a:
        s1 = s1/n
        s2 = m//a + 1
    elif n//a != n/a and m//a == m/a:
        s1 = n//a + 1
        s2 = m/a
    else:
        s1 = n//a + 1
        s2 = m//a + 1
    return s1 * s2
