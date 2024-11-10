
import hashlib
import requests

def hash_sha1(password):
    
    senha_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefixo = senha_sha1[:5]
    sufixo = senha_sha1[5:]
    return check_pwned_api(prefixo, sufixo)
    
def check_pwned_api(prefixo, sufixo):
    url = f"https://api.pwnedpasswords.com/range/{prefixo}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            hashes = (line.split(':') for line in response.text.splitlines())
            for h, count in hashes:
                if h == sufixo:
                    return f"A senha foi comprometida {count} vezes em vazamentos."
            return "A senha não foi encontrada em vazamentos."
        else:
            return "Erro ao acessar a API."
    except requests.exceptions.Timeout:
        return "A solicitação para a API expirou. Verifique sua conexão e tente novamente."
    
    except requests.exceptions.ConnectionError:
        return "Não foi possível se conectar à API. Verifique sua conexão com a internet."
    
    except requests.exceptions.RequestException as e:
        return f"Erro de solicitação: {e}. Tente novamente mais tarde."
