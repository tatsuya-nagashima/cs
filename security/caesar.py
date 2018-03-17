# _*_coding: utf-8-*-

def encrypt(plain_text, key):
    cipher_text = ""

    for i in range(len(plain_text)):
        #文字をkey文字ずらす
        rot_ch = chr(ord(plain_text[i])+key)
        if rot_ch <= 'z':
            cipher_text += rot_ch
        #文字をずらすとzを超える場合
        else :
            rot_ch = chr((ord(plain_text[i])-26+key))
            cipher_text += rot_ch

    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""

    for i in range(len(cipher_text)):
        rot_ch = chr(ord(cipher_text[i])-key)
        if rot_ch >= 'a':
            plain_text += rot_ch
        #文字をずらすとaを超える場合
        else :
            rot_ch = chr((ord(cipher_text[i])+26-key))
            plain_text += rot_ch

    return plain_text

#ブルートフォース攻撃
def attack(cipher_text):
    for i in range(0,26):
        plain_text = ""
        for j in range(len(cipher_text)):
            rot_ch = chr(ord(cipher_text[j])-i)
            if rot_ch >= 'a':
                plain_text += rot_ch
                #文字をずらすとaを超える場合
            else :
                rot_ch = chr((ord(cipher_text[j])+26-i))
                plain_text += rot_ch
        print "rot %d:" % i, plain_text

if __name__ == '__main__':
    print ("Please input plain_text :"),
    plain_text = raw_input()

    print ("Please input key :"),
    key = raw_input()

    cipher_text = encrypt(plain_text, int(key))
    plain_text = decrypt(cipher_text, int(key))
    print ("Encrypt : " + cipher_text)
    print ("Decrypt : " + plain_text)

    print ("\nAttack!")
    attack(cipher_text)
