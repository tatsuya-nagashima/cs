# _*_coding: utf-8-*-
import math

def encrypt(plain_text, public_key):
    E,N = public_key

    #暗号文=平文**E mod N
    plain_integers = [ord(char) for char in plain_text]
    cipher_integers = [i ** E % N for i in plain_integers]
    cipher_text = ''.join(unichr(i) for i in cipher_integers)

    return cipher_text

def decrypt(cipher_text, private_key):
    D,N = private_key

    #平文=暗号文**D mod N
    cipher_integers = [ord(char) for char in cipher_text]
    plain_intergers = [i ** D % N for i in cipher_integers]
    plain_text = ''.join(chr(i) for i in plain_intergers)

    return plain_text

def generate_keys(p, q):
    N = p * q
    L = lcm(p-1, q-1)

    for i in range(2, L):
        if gcd(i, L) == 1:
            E = i
            break

    for i in range(2, L):
        if (E*i) % L == 1:
            D = i
            break

    public_key  = (E, N)
    private_key = (D, N)

    return public_key, private_key

#最小公倍数
def lcm(p, q):
    return p * q // gcd(p, q)

#最大公約数　ユークリッドの互除法
def gcd(p, q):
	while q:
		p, q = q, p % q
	return p

def attack(cipher_text, public_key):
    e = public_key[0]
    n = public_key[1]

    #鍵の生成に用いられている素数をエラトステネスの篩で見つけ出し、平文を解読
    a = range(n)
    a[1] = 0
    for i in a:
        if not i:
            continue
        elif i > math.sqrt(n):
            break
        else:
            for j in xrange(i+i, n, i):
                a[j] = 0

    a = [x for x in a if x]
    for i in range(len(a)):
        if n % a[i]==0:
            p=a[i]
            q=n/p
            break

    public_key, private_key = generate_keys(p, q)
    plain_text = decrypt(cipher_text, private_key)
    print plain_text

if __name__ == '__main__':
  print ("Please input plaintext :"),
  plain_text = raw_input()

  public_key, private_key = generate_keys(19, 23)
  cipher_text = encrypt(plain_text, public_key)
  plain_text = decrypt(cipher_text, private_key)

  print ("Encrypt : " + cipher_text)
  print ("Decrypt : " + plain_text)

  print ("\nAttack!")
  attack(cipher_text, public_key)
