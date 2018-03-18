# _*_coding: utf-8-*-
from rsa import *
import hashlib

if __name__ == '__main__':
  public_key, private_key = generate_keys(19, 23)

  #デジタル署名(送信者想定)
  print ("Please input sign :"),
  sign = raw_input()
  digest = hashlib.sha256(sign).hexdigest()
  signature = encrypt(digest, private_key)

  #デジタル署名を復号し、ハッシュ値を比較することで検証(受信者想定)
  data= decrypt(signature, public_key)
  if data == digest:
      print ("Verify : OK")
  else:
      print ("Verify : NG")
