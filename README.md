### The Quero-Quero Webmail and Web Filter

Ferramente de _front-end_ para interface do The Harvester.


__Requisitos funcionais:__

Uma interface de linha de comando customizado, para o The Harvester.
Ao executar a ferramenta já irá aparecer uma serie de perguntas, bastando entrar com as informações pertinentes ao alvo que deseja pesquisar.
Sendo algumas dessas funções:
- [x] Domínio do alvo
- [x] A quantidade limite de buscas das informações, não há limite, mas quanto maior for, mais abrangente e demorado será.
- [x] O data source, que é a fonte de dados, que pode ser o Google, entre outras opções.
- [x] Pode as informações serem impressos na tela, ao final da varredura, ou enviados para um arquivo do tipo XML/HTML.


__Requisitos não funcionais:__

- [x] Sistema operacional Linux, preferência para o Kali ou qualquer outro que suporte o The Harvester.
- [x] Interpretador Python 2.7 instalado, atualmente na versão 2.7.17.
- [x] The Harvester instalado.
- [x] Mozilla Firefox, para abertura dos arquivos XML/HTML.


__Execução:__
```
python theQueroQuero.py
python2 theQueroQuero.py
```
Ao executar o arquivo, o mesmo irá pedir uma série de informações como:   
> Domínio a ser pesquisado, ex: google.com;   
> Quantidade de Resultados da Pesquisa, ex: 1000;      
> Fonte de Pesquisa, ex: Google;   

Esse projeto faz parte dos meus estudos de "_Python para pentesting_":
Foi desenvolvido para fins de aprendizagem acadêmica, com isso, está em constante evolução, 
até futuramente, se tornar parte do The Harvester, ou uma ferramenta independente.

Está sob licença GPL, mais informações no arquivo LICENSE.
Então fique a vontade para:
- [x] Copiar
- [x] modificar
- [x] Distribuir
Como quiser, apenas mantenha os meus créditos.

Para dúvidas, sugestões e/ou melhorias, basta me escrever um e-mail:
_joaobcfracassi@gmail.com_

