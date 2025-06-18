import requests

def test_playfair_encrypt():
    url = "http://127.0.0.1:5000/api/playfair/encrypt"
    payload = {
        "plain_text": "HELLO",
        "key": "KEYWORD"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Encrypt Response:", response.json())
    else:
        print("Error during encryption")

def test_playfair_decrypt():
    url = "http://127.0.0.1:5000/api/playfair/decrypt"
    payload = {
        "cipher_text": "ENCRYPTEDTEXT",
        "key": "KEYWORD"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Decrypt Response:", response.json())
    else:
        print("Error during decryption")

if __name__ == "__main__":
    test_playfair_encrypt()
    test_playfair_decrypt()
