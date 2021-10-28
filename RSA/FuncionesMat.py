#Mario Rodriguez
#Lab Seguridad Informatica 

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m

def mcd(a, b):
 resto = 0
 while(b > 0):
  resto = b
  b = a % b
  a = resto
 return a

