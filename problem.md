Como capanga da estação espacial do Comandante Lambda, espera-se que você seja engenhoso, inteligente e tenha raciocínio rápido. Afinal, não é fácil construir um dispositivo do Juízo Final e dar ordens aos coelhinhos ao mesmo tempo! Para garantir que todos sejam suficientemente perspicazes, o Comandante Lambda instalou um novo piso fora dos dormitórios dos capangas. Parece um tabuleiro de xadrez, e todas as manhãs e noites você tem que resolver um novo quebra-cabeça de movimento para cruzar o chão. Tudo bem se você fosse a torre ou a rainha, mas em vez disso, você tem que ser o cavalo. Pior ainda, se você demorar muito para resolver o quebra-cabeça, você será "oferecido" como cobaia para o dispositivo do Juízo Final LAMBCHOP!

Para se ajudar a ir e voltar do seu beliche todos os dias, escreva uma função chamada solução(src, dest) que recebe dois parâmetros: o quadrado de origem, no qual você começa, e o quadrado de destino, que é onde você precisa pousar. resolva o quebra-cabeça. A função deve retornar um número inteiro representando o menor número de movimentos necessários para você viajar da casa de origem até a casa de destino usando os movimentos de um cavalo de xadrez (ou seja, duas casas em qualquer direção imediatamente seguidas por uma casa perpendicular a essa direção , ou vice-versa, em formato de "L"). Os quadrados de origem e de destino serão um número inteiro entre 0 e 63, inclusive, e são numerados como o exemplo do tabuleiro de xadrez abaixo:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

19 -> 36

19 -> 2  = 17
   -> 4  = 15
   -> 9  = 10
   -> 13 = 6
   -> 25 = 6
   -> 30 = 11
   -> 34 = 15
   -> 36 = 17

0 -> 1

0 -> 10
  -> 17 -> 11 -> 1
        -> 02

movimentos do cavalo:
Sobe
x - 7 * 2 + 1 = sobe duas linhas + uma para direita
x - 7 * 2 - 1 = sobe duas linhas + uma para esquerda
x - 7 * 1 + 2 = sobe uma linha + duas casas a direita
x - 7 * 1 - 2 = sobe uma linha + duas casas a esquerda

Desce
x + 7 * 2 + 1 = sobe duas linhas + uma para direita
x + 7 * 2 - 1 = sobe duas linhas + uma para esquerda
x + 7 * 1 + 2 = sobe uma linha + duas casas a direita
x + 7 * 1 - 2 = sobe uma linha + duas casas a esquerda
