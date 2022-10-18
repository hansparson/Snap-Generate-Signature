import json
import hmac
import hashlib


#### GENERATE SIGNATURE HMAC_SHA512
merchant_secret = bytes(("9b79eedb5c564136a73d0c1cb2084e31"), 'utf-8')
x_timestamp = "2020-01-01T00:00:00+07:00"
http_method = "POST"
http_url_endpoint = "/openapi/v1.0/emoney/account-inquiry"
token = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ4X3RpbWVzdGFtcCI6ICIyMDIyLTEwLTE4VDExOjEwOjI1KzA3OjAwIiwgInhfY2xpZW50X2tleSI6ICI2MmZiNWYyMzIyOGMxMGM5YjJhMjY5YTUiLCAieF9zaWduYXR1cmUiOiAiYXBwbGljYXRpb24vanNvbiJ9.MWY3YjM3YWE5Mjg5YzEwOWYyMTRlY2Q0NjJlMDA2N2Y1ZDU3NThlOGFjMTI1YTUyZmVjMjEzOTA3M2NhNjdhYw"
request_body = {
            "customerNumber":"6285773483917",
            "partnerReferenceNo":"987654321",
            "notes":"Deskripsi Top Up",
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
StringToSign = ("{}:{}:{}:{}:{}").format(http_method, http_url_endpoint, token, body, x_timestamp)
StringToSign = StringToSign.encode()

## Convert all Data To Signature
signature = hmac.new(merchant_secret, StringToSign, hashlib.sha512).hexdigest()
print("TopUp Signature : ", signature)
