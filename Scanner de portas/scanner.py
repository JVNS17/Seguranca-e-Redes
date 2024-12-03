import socket
import ipaddress as ipadd
import re 
from threading import Thread

def validar_ip():
    print("Scanner de portas by JVNS17 1.1\n")
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
                        print(f"A porta {n} é inválida.")
                        break
                    else:
                        portas.append(int(n))

                if tipo == 1:
                     return iniciar_threads(endereco, portas)
                elif tipo == 2:
                    if len(portas) == 2 and portas == sorted(portas):
                        portas = list(range(portas[0], portas[1]+1))
                        return iniciar_threads(endereco, portas)    
                    else:
                        print("Formatação incorreta.")
                        break
                
            
            else:
                print("Escolha somente a opção 1 ou 2.")
                break
   
    except ValueError:
        print("Caractere inválido.")


def escanear_porta(endereco, porta):
    try:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((endereco, porta))
        if resultado == 0:
            print(f"Porta {porta} aberta")
        
        else:
            print(f"Porta {porta} fechada")
        sock.close()
            
                    
    except Exception as e:
        print(f"Erro ao escanear porta {porta}: {e}")
            


def iniciar_threads(endereco, portas):
    
    threads = []
    for porta in portas:
        
        thread = Thread(target=escanear_porta, args=(endereco, porta))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
        
    print(f'Escaneamento concluído!')        
    

if __name__ == '__main__':
    validar_ip()        
