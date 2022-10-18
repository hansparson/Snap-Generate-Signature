from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Hash import SHA
import base64

#################### INPUT DATA Yang DIBUTUHKAN untuk create signature get token###################################
x_timestamp  = "2020-01-01T00:00:00+07:00"
x_client_key = "62fb5f23228c10c9b2a269a5"
body = {
    "grantType":"client_credentials",
    "additionalInfo":{
    }
}
#################### INPUT DATA Yang DIBUTUHKAN untuk create signature get token###################################

random_text = SHA256.new(bytes("{}|{}".format(x_client_key,x_timestamp), 'utf-8'))

##### private key ######
private_key = RSA.importKey(open('private.key').read(),passphrase="12345")
privkey = PKCS1_v1_5.new(private_key)

#####  public key ######
public_key = RSA.importKey(open('public.key').read())
pubkey = PKCS1_v1_5.new(public_key)

## Generate Signature (Pycryptodome Python)
signature = privkey.sign(random_text)
signature_base64 = base64.b64encode(signature).decode('UTF-8')
signature_decode = base64.b64decode(signature_base64)
print(signature_base64)

### Verify
if pubkey.verify(random_text, signature):
    print ("The signature is authentic.")
else:
    print ("The signature is not authentic.")


