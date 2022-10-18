
import json
import hmac
import hashlib


############### GENERATE SIGNATURE HMAC_SHA512 ###############

merchant_secret = bytes(("9b79eedb5c564136a73d0c1cb2084e31"), 'utf-8')
x_timestamp = "2020-01-01T00:00:00+07:00"
http_method = "POST"
http_url_endpoint = "/openapi/v1.0/emoney/account-inquiry"
request_body = {
            "customerNumber":"6285773483917",
            "partnerReferenceNo":"987654321",
            "amount":{
                "value":"10000.00",
                "currency":"IDR"
            },
            "additionalInfo":{
            }
        }

minify_body = json.dumps(request_body, separators=(',', ':'))
SHA256_hashing = hashlib.sha256(minify_body.encode()).hexdigest()
body = SHA256_hashing.lower()

## String To Signin Ready
StringToSign = ("{}:{}:{}:{}").format(http_method, http_url_endpoint, body, x_timestamp)
print(StringToSign)
StringToSign = StringToSign.encode()

## Convert all Data To Signature
signature = hmac.new(merchant_secret, StringToSign, hashlib.sha512).hexdigest()
print("Inquiry Signature : ", signature)
