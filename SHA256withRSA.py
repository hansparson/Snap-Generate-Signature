import rsa
import base64

__pem_begin = '-----BEGIN RSA PRIVATE KEY-----\n'
__pem_end = '\n-----END RSA PRIVATE KEY-----'


def sign(content, private_key, sign_type):
    """signature

    :param content: signature content
    :type content: str

    :param private_key: private key string, PKCS#1
    :type private_key: str

    :param sign_type: signature type, choose one of'RSA' or'RSA2'
    :type sign_type: str

    :return: return signature content
    :rtype: str
    """ 
    if sign_type.upper() == 'RSA':
        return rsa_sign(content, private_key, 'SHA-1')
    elif sign_type.upper() == 'RSA2':
        return rsa_sign(content, private_key, 'SHA-256')
    else:
        raise Exception('sign_type error' )


def rsa_sign(content, private_key, _hash):
    """SHAWithRSA

    :param content: signature content
    :type content: str

    :param private_key: private key
    :type private_key: str

    :param _hash: hash algorithm, such as: SHA-1, SHA-256
    :type _hash: str

    :return: Signature content
    :rtype: str
    """
    private_key = _format_private_key(private_key)
    pri_key = rsa.PrivateKey.load_pkcs1(private_key.encode('utf-8'))
    sign_result = rsa.sign(content, pri_key, _hash)
    return base64.b64encode(sign_result)


def _format_private_key(private_key):
    """Format the private, missing "-----BEGIN RSA PRIVATE KEY-----" and "-----END RSA PRIVATE KEY-----" Need to add

    :param private_key: private key
    :return: pem private key string
    :rtype: str
    """ 
    if not private_key.startswith(__pem_begin):
        private_key = __pem_begin + private_key
    if not private_key.endswith(__pem_end):
        private_key = private_key + __pem_end
    return private_key


#################### INPUT DATA Yang DIBUTUHKAN untuk create signature get token###################################
x_timestamp  = "2020-01-01T00:00:00+07:00"
x_client_key = "62fb5f23228c10c9b2a269a5"
body = {
    "grantType":"client_credentials",
    "additionalInfo":{
    }
}
#################### INPUT DATA Yang DIBUTUHKAN untuk create signature get token###################################

random_text = (bytes("{}|{}".format(x_client_key,x_timestamp), 'utf-8'))


# Runing SHA256WithRSA (rsa library python)
sign = sign(random_text, open('private.key').read(), 'RSA2')
print(sign)
