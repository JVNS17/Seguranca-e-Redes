import socket
import ipaddress as ipadd
import re 

def validar_ip():
    print("Scanner de portas by JVNS17 1.0\n")
    endereco = input("Digite o endereço de domínio/ip para escanear:")
    try:
        if ipadd.ip_address(endereco):
            escolher_porta(endereco)
    except ValueError:    
        try:
            if socket.gethostbyname(endereco):
                
                escolher_porta(endereco)
        
        except socket.gaierror:
            print('Insira um endereço válido.')
    
       
def escolher_porta(endereco):
    print("Escolha o tipo de escaneamento:")
    print('1- Seleção (Ex: "80" ou "21, 443" )', "\n2- Faixa (Ex: 0-1024)") 
    try:
        tipo = int(input())
        while True:
            if tipo in [1,2]:
                escolha = input("Escolha a porta: ")
                numeros = re.findall(r'\d+', escolha) 
                portas = []
                for n in numeros:
                    if int(n) > 65535:
                        print(f"A porta {n} é inválida")
                        break
                    else:
                        portas.append(int(n))

                if tipo == 1:
                     return escanear_porta(endereco, portas, tipo)
                elif tipo == 2:
                    if len(numeros) == 2 and numeros == sorted(numeros):
                        return escanear_porta(endereco, portas, tipo)    
                    else:
                        print("Formatação incorreta")
                        break
                
            
            else:
                print("Escolha somente a opção 1 ou 2.")
                break
   
    except ValueError:
        print("Caractere inválido.")


def escanear_porta(endereco, portas, tipo):
    try:
        if tipo == 1:
            for p in portas:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                resultado = sock.connect_ex((endereco, p))
                
                if resultado == 0:
                    print(f"Porta {p} aberta")
                else:
                    print(f"Porta {p} fechada")
                sock.close()
        else:
            for p in range(portas[0], portas[1]+1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                resultado = sock.connect_ex((endereco, p))
                
                if resultado == 0:
                    print(f"Porta {p} aberta")
                else:
                    print(f"Porta {p} fechada")
                sock.close()
            
        
    except Exception as e:
        print(f"Erro na porta {portas}: {e}")







if __name__ == '__main__':
    validar_ip()        

    