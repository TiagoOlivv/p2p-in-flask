# Sistemas Distribuídos
Segundo Tanenbaum, um sistema distribuído é um conjunto de computadores independentes entre si, e até diferentes, ligados através de uma rede de dados, que se apresentam aos utilizadores como um sistema único e coerente.
## Exemplos:
- Sistemas de pesquisas (motores de busca)
- Sistemas financeiros
- Jogos Online
- Redes Sociais e plataformas idênticas



# Rede (P2P)
### O que é P2P?
P2P significa Peer to Peer e o 2 da sigla é um trocadilho com a palavra to ("para" em inglês), já em português, significa "par a par".
O nome se refere ao formato à disposição dos computadores interligados à rede, onde cada computador conectado realiza as funções de cliente e servidor ao mesmo tempo, dessa forma, tudo é descentralizado, sem um único servidor centralizado que detenha o arquivo e precisa se encarregar de enviar todos os milhares de pedidos ao mesmo tempo.

Cada computador que faz parte do cluster recebe o nome de nó (ou node). Teoricamente, não há limite máximo de nós, mas independentemente da quantidade de máquinas que o compõe, o cluster deve ser "transparente", ou seja, ser visto pelo usuário ou por outro sistema que necessita deste processamento como um único computador.

Os nós do cluster devem ser interconectados, preferencialmente, por uma tecnologia de rede conhecida, para fins de manutenção e controle de custos, como a Ethernet. É extremamente importante que o padrão adotado permita a inclusão ou a retirada de nós com o cluster em funcionamento, do contrário, o trabalho de remoção e substituição de um computador que apresenta problemas, por exemplo, faria a aplicação como um todo parar.

[Infowester](https://www.infowester.com/cluster.php)

# Rede (P2P) para compartilhamento de arquivos com o conceito de Torrent 
Acontece como cliente e servidor, no caso o Cliente é o nome dado ao pc que pede algo à rede, e servidor aquele que envia o pedido. Como não existe um servidor dedicado, veja que nenhum servidor de torrent armazena sequer um arquivinho, os arquivos estão na sua máquina, na minha, na do seu vizinho, enfim, em qualquer local do mundo. Aqui está a genialidade deste tipo de conexão: Não há uma única fonte para o seu download (como acontece quando você baixa algo de um site), há milhões de fontes só esperando sua conexão.

O serviço P2P cria uma rede virtual entre as máquinas conectadas no momento e vasculha o HD do usuário atrás da música, vídeo ou qualquer outro documento que a pessoa esteja baixando.
 o que torna a rede P2P tão eficiente é que você pode começar a baixar de uma fonte, e no momento em que esta fonte desligar sua máquina e interromper a conexão, o download recomeçará de onde parou, a partir dos dados cedidos por um outro usuário, se este novo usuário também desconectar, o processo se repetirá, ad eternum, até você completar o download
![academico](img/p2p.jpg)
Mas e como funciona essa coisa de baixar um pouco de um, um pouco de outro, etc. não dá erro? Não, pois neste tipo de conexão, os arquivos a serem transferidos são divididos em pequenos pedaços e então compartilhados. Os pedaços são sempre os mesmos para a música X, ou jogo Y. Funciona assim: Você baixa um desses pedaços de arquivo e, logo após, você imediatamente passa a distribuí-lo aos outros usuários que estão fazendo o download do mesmo arquivo. Assim, evitam-se gargalos na transmissão dos dados e permite que mesmo aquela pessoa com uma conexão lenta de transferência consiga repassar o arquivo para milhares de pessoas. 
[Infowester](https://www.infowester.com/cluster.php)

## REDE (P2P) para compartilhamento de arquivos com o conceito de Torrent  de forma simplificada
O propósito deste presente trabalho abordando conceito de redes P2P e Torrent Arquitetura e estruturação do sistema - Cluster de processamento de texto em grandes volumes (BigData), modelo mapReduce - WordCount example.
#### Modelo padrão mapreduce
![academico](img/figuraprojeto.jpg)
#### Arquitetura mapreduce aplicado neste trabalho
![academico](img/mapreduce.png)
## Segurança

A segurança em uma rede peer-to-peer não é uma caracteristica predominante. Assim se sua organização tiver preocupações em matéria de segurança a decisão deve ser para algo que sua organização pode controlar (como um servidor). Uma vez que os usuários vão  necessitar fazer o compartilhamento do acesso a pastas, eles podem optar por não exigir senhas. Esta falta de hierarquia tem um impacto enorme sobre a segurança da rede e sua organização precisará de uma formação adequada para seus usuários para evitar problemas.

#### Representação do sistema de criptografia utilizado no Cluster e modelo base.
![academico](img/cript.png)

## Arquitetura geral do Sistema Cluster
![academico](img/main.png)

## Contador de palavras
Como foi requisitado no trabalho, foi feita a implementação de algoritmo contador de palavras tendo como parametros de entrada, três palavras que serão buscadas a partir de um arquivo de texto.

Um contador de palavras pode ser útil para quem precisa escrever um texto que terá um limite de caracteres, ou quando se escreve um texto com um número de palavras ou caracteres específicos. Ele tem como alvo uma ampla gama de usuários: de estudante para profissional de SEO, jornalista ou escritor, o gerente da comunidade, o pesquisador ... Esses perfis podem precisar de uma calculadora para contar o número de parágrafos, frases, palavras ou letras em seus escritos, teses, mensagem, artigo ou texto.

Porém o enfoque desse trabalho é fazer a contagem unicamente das palavras, levando em consideração as três palavras dadas como entrada para que sejam buscadas, retornando o seu respectivo número de aparições no texto.


#### Tempos de Execução * Teste Simples.
- 1 - Node: 4.00460786199983 sec
- 2 - Node: 2.0028634170012083 sec

## Telas:
##### Tela Master - Sem cadastro.
![academico](gui/1.png)
##### Tela Master > Cadastrar Nodes/Slaves.
![academico](gui/2.png)
##### Tela Master > Remover Nodes/Slaves.
![academico](gui/3.png)
##### Tela Master - Com cadastro.
![academico](gui/4.png)
##### Tela Cliente > Efetuando Query.
![academico](gui/5.png)
##### Tela Cliente/Resultados > Retorno das ocorrências
![academico](gui/6.png)

## Acknowledgements:
![academico](img/mestres.png)

```LateX
@misc{sdtorrent,
 title   ={A prototype network p2p},
 url     ={https://github.com/TiagoOlivv/prototype-network-p2p/},
 organization={AbnTeX},
 urlaccessdate={4 jun. 2019}
}
```
```LateX
Use \cite{sdtorrent}
```
