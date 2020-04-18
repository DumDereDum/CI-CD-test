import json
import requests
from base64 import b64encode
from nacl import encoding, public


def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(
        public_key.encode("utf-8"),
        encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


# ----------------------------------------
# input your information here

token = '***'  # your token
user_name = '***'  # your user name
password = '***'  # your password
image_name = '***'  # your password
repository_name = '***'  # your repository
# ----------------------------------------

r = requests.get('https://api.github.com/repos/HSE-NN-SE/'
                 + repository_name + '/actions/secrets/public-key',
                 headers={'Authorization': 'token ' + token})
data = r.json()
print(data)

key = data['key']
key_id = data['key_id']

# DOCKER_USERNAME
encripted_value = encrypt(key, user_name)
tmp = {'encrypted_value': encripted_value,
       'key_id': key_id}
print(tmp)
requests.put('https://api.github.com/repos/HSE-NN-SE/'
             + repository_name + '/actions/secrets/DOCKER_USERNAME',
             headers={'Authorization': 'token ' + token,
                      "Content-Type": "application/json"},
             data=json.dumps(tmp))

# DOCKER_PASSWORD
encripted_value = encrypt(key, password)
tmp = {'encrypted_value': encripted_value,
       'key_id': key_id}
requests.put('https://api.github.com/repos/HSE-NN-SE/'
             + repository_name + '/actions/secrets/DOCKER_PASSWORD',
             headers={'Authorization': 'token ' + token,
                      "Content-Type": "application/json"},
             data=json.dumps(tmp))

# IMAGE
encripted_value = encrypt(key, image_name)
tmp = {'encrypted_value': encripted_value,
       'key_id': key_id}
requests.put('https://api.github.com/repos/HSE-NN-SE/'
             + repository_name + '/actions/secrets/IMAGE',
             headers={'Authorization': 'token ' + token,
                      "Content-Type": "application/json"},
             data=json.dumps(tmp))

r = requests.get('https://api.github.com/repos/HSE-NN-SE/'
                 + repository_name + '/actions/secrets',
                 headers={'Authorization': 'token ' + token})
data = r.json()
print(data)
