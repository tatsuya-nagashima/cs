# _*_coding: utf-8-*-

def encrypt(plaintext, key):
    ciphertext = ""

    for i in range(len(plaintext)):
        #文字をkey文字ずらす
        rot_ch = chr(ord(plaintext[i])+key)
        if rot_ch <= 'z':
            ciphertext += rot_ch
        #文字をずらすとzを超える場合
        else :
            rot_ch = chr((ord(plaintext[i])-26+key))
            ciphertext += rot_ch

    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""

    for i in range(len(ciphertext)):
        rot_ch = chr(ord(ciphertext[i])-key)
        if rot_ch >= 'a':
            plaintext += rot_ch
        #文字をずらすとaを超える場合
        else :
            rot_ch = chr((ord(ciphertext[i])+26-key))
            plaintext += rot_ch

    return plaintext

#ブルートフォース攻撃
def attack(ciphertext):
    for i in range(0,26):
        plaintext = ""
        for j in range(len(ciphertext)):
            rot_ch = chr(ord(ciphertext[j])-i)
            if rot_ch >= 'a':
                plaintext += rot_ch
                #文字をずらすとaを超える場合
            else :
                rot_ch = chr((ord(ciphertext[j])+26-i))
                plaintext += rot_ch
        print "rot %d:" % i, plaintext

if __name__ == '__main__':
    print "PLEASE INPUT PLAINTEXT : ",
    plaintext = raw_input()

    print "PLEASE INPUT KEY : ",
    key = raw_input()

    ciphertext = encrypt(plaintext, int(key))
    print("CIPHERTEXT : " + ciphertext)

    plaintext = decrypt(ciphertext, int(key))
    print("PLAINTEXT : " + plaintext)
    
    print ""
    print("ATTACK!")
    attack(ciphertext)
