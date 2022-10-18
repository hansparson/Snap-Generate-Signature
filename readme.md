This Coding Test Working As Merchat that Generate Private Key and Public Key


This is the method to generate Signature for
1. Get Token
2. Signature without Token (example: Inquiry)
3. Signature With Token (exaple: TopUp)

to create Private Key run in terminal (ubuntu) - this process will need passcode to lock private.key file :

        openssl genrsa -des3 -out private.key 2048

After that create Public Key from Private Key - use passcode to unlock private.key file

        openssl rsa -in private.key -outform PEM -pubout -out public.key

the private.key and public key will be created

Please Install Requirements

        pip install -r requirements.txt