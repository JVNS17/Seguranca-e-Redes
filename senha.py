from zxcvbn import zxcvbn
from api import hash_sha1
from traducao import ctd_br, ctd_br2, fbs_br, fbw_br
from re import search
def verificador():
    
    while True:
        try:
            print('\nVerificador de senhas by JVNS17')
            print('\n Qual tipo de verificação você deseja?')
            print('1.Simples (Força da senha + Checar se ela foi exposta em algum Data Breach)', '\n2.Normal (Simples + Tentativas para quebrar senha +  Tempo necessário em diferentes cenários)', '\n3.Detalhada (Normal + Complexidade da senha + Avisos e Sugestões para a senha)')
            tipo = int(input())
           
            if tipo in [1,2,3]:    
                senha = input('\nDigite a sua senha:')
                if senha.strip():
                    verifica = zxcvbn(senha)
                    if tipo == 1:    
                        simples(verifica)
                        break
                        
                    elif tipo == 2:
                        simples(verifica)
                        normal(verifica)
                        break
                        
                    else:
                        simples(verifica)
                        normal(verifica)
                        detalhada(verifica)
                        break
                else:
                    print('\nNenhum caractere digitado.')                
                        
    
            else:
                print('\nNúmero inválido.')
        except ValueError:
           print('\nCaractere inválido.\n')    
            
def simples(verifica):
    print('-' * 80)
    forca = {0 : 'Muito Fraca', 1 : 'Fraca', 2 : 'Moderada', 3 : 'Forte', 4 : 'Muito forte'}
    print('\nForça da senha:', forca[verifica['score']])
    print(hash_sha1(verifica['password']))
    



def normal(verifica):
    print('-' * 80)
    vazado = hash_sha1(verifica['password'])
    print(f'\n{verifica['guesses']} tentativas para quebrar a senha.\n')
    
    for num, a in enumerate(ctd_br(verifica)):
        if num >= 2 and vazado == 'A senha não foi encontrada em vazamentos.':
            break
        else:
            print(a, ctd_br2(verifica)[num])
            
        




def detalhada(verifica):
    print('-' * 80)
    
    tipos = ['', '','','']
    soma = 0
    
    if search(r'[A-Z]', verifica['password']):
        tipos[0] = 'x'
        soma += 1
    
    if search(r'[a-z]', verifica['password']):
        tipos[1] = 'x'
        soma += 1
    
    if search(r'[0-9]', verifica['password']):
        tipos[2] = 'x'
        soma += 1
    
    if search(r'[^A-Za-z0-9]', verifica['password']):
        tipos[3] = 'x'
        soma += 1
     
    print(f'Tipos de caracteres diferentes: ({soma}/4)')
    print(f'(Letra maiúscula[{tipos[0]}] | Letra minúscula[{tipos[1]}] | Número[{tipos[2]}] | Caractere especial[{tipos[3]}])')
    
    
    print(f'\nAviso: {fbw_br(verifica)}')
    print(f'Sugestões: {fbs_br(verifica)}')


verificador()

