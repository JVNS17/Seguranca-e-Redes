Verificador de Vulnerabilidades de Senhas
Este projeto consiste em um script de verificação de senhas que avalia a força de uma senha, verifica se ela foi comprometida em vazamentos de dados e fornece sugestões de segurança. O código é organizado em três módulos principais para facilitar a manutenção e a expansão: senha.py, api.py e traducao.py.

==Estrutura dos Módulos==
1. senha.py 
Descrição: Este é o módulo principal do script, que coordena o fluxo e a interação com o usuário. Ele permite ao usuário escolher entre três níveis de verificação:

Simples: Analisa a força da senha e verifica se ela foi exposta em vazamentos.

Normal: Inclui a verificação simples, além de estimativas de tentativas e tempos para quebrar a senha em diferentes cenários.

Detalhada: Exibe todas as informações anteriores, além de uma análise detalhada dos tipos de caracteres utilizados e sugestões de melhorias.

==Funcionalidades==
Recebe a senha do usuário.
Chama as funções apropriadas para cada nível de verificação (simples, normal, detalhada).
Exibe o resultado da verificação em português.

2. api.py 
Descrição: Este módulo se conecta à API Have I Been Pwned para verificar se a senha fornecida foi exposta em algum vazamento de dados. A senha é convertida para um hash SHA-1, e apenas parte desse hash é enviada à API para proteção.

==Funcionalidades==
hash_sha1(password): Gera o hash SHA-1 da senha e o divide em prefixo e sufixo.
check_pwned_api(prefixo, sufixo): Realiza a busca do hash parcial na API e retorna o número de vezes que a senha foi comprometida, se aplicável.

3. traducao.py 
Descrição: Este módulo traduz o feedback e as estimativas de tempos de quebra de senha da biblioteca zxcvbn para o português. Ele utiliza dicionários de tradução que mapeiam os avisos e sugestões de segurança comuns de inglês para português.

==Funcionalidades==
ctd_br(senha) e ctd_br2(senha): Traduzem os tempos estimados para quebra de senha em diferentes cenários.
fbw_br(senha) e fbs_br(senha): Traduzem os avisos e sugestões da biblioteca zxcvbn para orientar o usuário em como melhorar a segurança da senha.

==Como Executar==
1. Instale as dependências (como zxcvbn e requests) com o comando:
pip install zxcvbn-python requests

2. Execute o script principal:
python senha.py

==Considerações de Uso==
Níveis de Verificação: O usuário pode escolher a profundidade da análise desejada, permitindo uma verificação rápida ou mais detalhada.
Verificação de Vazamentos: A senha é verificada contra vazamentos online, mas apenas se ela não tiver sido comprometida é que os cenários de ataque offline são omitidos.
Feedback Traduzido: Todo o feedback sobre a força da senha é apresentado em português para fácil compreensão.
