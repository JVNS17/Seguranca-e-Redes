from zxcvbn import zxcvbn
from api import hash_sha1
from traducao import ctd_br, ctd_br2, fbs_br, fbw_br
from re import search
from getpass import getpass
def verificador():
    
    while True:
        try:
            print('\nVerificador de senhas 1.1 by JVNS17')
            print('\n Qual tipo de verificação você deseja?')
            print('1.Simples (Força da senha + Checar se ela foi exposta em algum Data Breach)', '\n2.Normal (Simples + Tentativas para quebrar senha +  Tempo necessário em diferentes cenários)', '\n3.Detalhada (Normal + Complexidade da senha + Avisos e Sugestões para a senha)')
            num = int(input())
            if num in [1,2,3]:
                senha = getpass('\nDigite a sua senha:')
                if senha.strip():
                    verifica = zxcvbn(senha)
                    tipo = {1: simples, 2: normal, 3: detalhada}
                    return tipo[num](verifica)   
                       
                        
                else:
                    print('\nNenhum caractere digitado.')                
                    break
            else:
                print('\nNúmero inválido.')
                break   
                             
                        
    
        except ValueError:
           print('\nCaractere inválido.\n')    
            
def simples(verifica):
    print('-' * 80)
    forca = {0 : 'Muito Fraca', 1 : 'Fraca', 2 : 'Moderada', 3 : 'Forte', 4 : 'Muito forte'}
    print('\nForça da senha:', forca[verifica['score']])
    print(hash_sha1(verifica['password']))
    



def normal(verifica):
    simples(verifica)
    print('-' * 80)
    vazado = hash_sha1(verifica['password'])
    print(f'\n{verifica['guesses']} tentativas para quebrar a senha.\n')
    
    for num, a in enumerate(ctd_br(verifica)):
        if num >= 2 and vazado == 'A senha não foi encontrada em vazamentos.':
            break
        else:
            print(a, ctd_br2(verifica)[num])
            
        




def detalhada(verifica):
    normal(verifica)
    print('-' * 80)
    
    numeros = ['', '','','']
    soma = 0
    
    if search(r'[A-Z]', verifica['password']):
        numeros[0] = 'x'
        soma += 1
    
    if search(r'[a-z]', verifica['password']):
        numeros[1] = 'x'
        soma += 1
    
    if search(r'[0-9]', verifica['password']):
        numeros[2] = 'x'
        soma += 1
    
    if search(r'[^A-Za-z0-9]', verifica['password']):
        numeros[3] = 'x'
        soma += 1
     
    print(f'Tipos de caracteres diferentes: ({soma}/4)')
    print(f'(Letra maiúscula[{numeros[0]}] | Letra minúscula[{numeros[1]}] | Número[{numeros[2]}] | Caractere especial[{numeros[3]}])')
    
    
    print(f'\nAviso: {fbw_br(verifica)}')
    print(f'Sugestões: {fbs_br(verifica)}')


verificador()

