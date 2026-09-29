# Projeto Web App

Plataforma de Gerenciamento de Campanha de RolePlayingGame e Virtual Table Top, 
Permitindo uma maior facilidade na organização, a possibilidade do grupo jogar remotamente com uma interface que simula a mesa de jogo,gerar documentos (handouts), rolagens de dados e etc, com proposito final de que esse entretenimento chegue aos usuários sem a necessidade do encontro presencial, além de desenvolver todos os benefícios que o RPG consegue trazer, como o trabalho em equipe, socialização, criatividade e a resolução de problemas.

Iremos integrar de começo apenas o sistema de Dungeons & Dragons Quinta edição, de forma a automatizar o sistema com um compêndio de regras

> A prioridade inicial é o gerenciamento de fichas.


## Individuos (Atores)

           -> Perfil de Mestre (GM) -> Acesso a múltiplos dados (Anotações de enredo, Personagens, Mapas)
           Usuário 
           -> Perfil de Jogador -> Operação sobre seu próprio Avatar e recorrer as regras do sistema

## Atividades

### Mestre (GM) ->

Deve conseguir criar, editar, excluir e ver "Campanhas/Aventuras", e convidar os outros usuários jogadores.

Dentro destas "Campanhas", deve conseguir criar, editar, excluir e ver
    - Documentos (Handouts), 
    - Fichas de personagens integradas (automatizando rolagem de dados, regras e modificadores)
    - Mapas
    - Tokens
personalizados, ou com base em templates pré definidos guardados em uma biblioteca de modelos.

Permitir a mesa de jogo com um sistema de áudio e vídeo integrado, com controle total sobre visão de mapa e permissões de jogador


### Jogador ->

Deve conseguir aceitar convites para entrar em "Campanhas/Aventuras" existentes criadas por um Mestre.

Dentro destas "Campanhas", deve conseguir:
    - Criar, editar, consultar e arquivar sua própria Ficha de Personagem (vinculando atributos, perícias, classes e itens).
    - Executar rolagens automáticas de dados diretamente da ficha (testes de atributo, rolagens de ataque, dano e testes de resistência).
    - Rastrear recursos vitais em tempo real (alterar Pontos de Vida atuais e temporários, consumir e recuperar Espaços de Magia/Pontos de Feitiço, munição e consumíveis).
    - Gerenciar o inventário pessoal (adicionar itens do compêndio, equipar/desequipar armas e armaduras com cálculo automático de peso e capacidade de carga).
    - Visualizar e mover seu próprio Token no mapa tático, respeitando a linha de visão (Line of Sight) e as permissões de deslocamento concedidas pelo Mestre.
    - Acessar a biblioteca de Documentos (Handouts) compartilhados publicamente pelo Mestre ou revelados exclusivamente para o seu personagem.
    - Interagir com o chat integrado da sessão (mensagens públicas para a mesa, rolagens abertas e mensagens secretas em sussurro diretamente para o Mestre).


## Ambiente

O ambiente é caracterizado pelas dimensões físicas, técnicas e operacionais sob as quais a plataforma interativa será executada:

### Ambiente Físico e Operacional
   **Contexto Remoto/Distribuído:** Usuários geograficamente dispersos conectados simultaneamente durante sessões narrativas de longa duração (sessões com média de 3 a 5 horas contínuas).
   **Ambiente Doméstico e Ruído Cognitivo:** Usuários operando em seus próprios espaços de estudo/lazer, sujeitos a distrações periféricas e cansaço visual acumulado, exigindo interfaces limpas e com suporte a alto contraste (*Dark Mode* nativo).
   **Uso Concorrente de Periféricos:** Interação simultânea entre teclado, mouse (para movimentação de tokens em grid tático), microfone/fone de ouvido para a comunicação por voz, e consulta secundária de anotações ou livros físicos.

### Ambiente Tecnológico e Plataforma
   **Ecossistema Web (Navegadores Modernos):** Execução multiplataforma sem necessidade de instalação de clientes pesados, suportada em navegadores baseados em Chromium (Google Chrome, Microsoft Edge, Brave) e Mozilla Firefox.
   **Dispositivos Alvo (Hardware e Resolução):**
       *Mestre (Desktop/Notebook):* Resoluções recomendadas a partir de 1366x768 até Ultrawide (1080p, 1440p), aproveitando telas maiores para painéis simultâneos (múltiplos handouts, grid de batalha e fichas abertas).
    *   *Jogador (Desktop/Tablet/Mobile Híbrido):* Interface responsiva adaptável a monitores convencionais e layouts mais densos para tablets e celulares em consultas rápidas de status.
   **Rede e Comunicação em Tempo Real:** Conexão contínua com a internet exigindo baixa latência para o tráfego de WebSockets (sincronização de posições de tokens, dados no chat e atualizações de vida) e protocolos WebRTC para áudio e vídeo peer-to-peer.


## Objetivos

   **Objetivo Geral:** Reduzir a sobrecarga de gerenciamento manual em mesas virtuais de D&D 5e, integrando criação de conteúdo narrativo e mecânica tática automatizada em um ambiente web único.
   **Objetivos Específicos:**
       Minimizar o tempo de consulta a regras externas durante a sessão por meio de um compêndio automatizado de magias, monstros e itens.
       Eliminar erros de cálculo aritmético comum (bônus de proficiência, cálculo de modificadores de habilidade e capacidade de carga) através de formulários reativos.
       Garantir a transição fluida entre narrativa descritiva (leitura de handouts/notas) e combate tático (VTT e iniciativa) sem troca de abas ou aplicações externas.


## Artefatos e Metáforas de Interação

   **A Ficha de Papel:** Transposta para um painel modular digital com divisão em abas (Combate, Magias, Inventário, Biografia) que mantém os hábitos de leitura da ficha clássica de D&D 5e, agregando automação por cliques diretos nos valores.
   **O Escudo do Mestre (GM Screen):** Metáfora reproduzida como um painel lateral/inferior retrátil ou modal contendo tabelas rápidas de regras, tracker de ordem de iniciativa e cards compactos de monitoramento de vida do grupo.
   **O Mapa Quadriculado e Miniaturas Físicas:** Transpostos para a tela do VTT (Virtual Tabletop) com renderização em Canvas/WebGL, suporte a camadas (camada do mapa, camada dos tokens, camada oculta do mestre) e ferramentas de medição de distância em pés/metros (grid de 5 pés).
   **Os Dados Poliédricos (d4, d6, d8, d10, d12, d20, d100):** Transpostos para um motor de rolagem randômica integrado à interface e acionado contextualment ao clicar em perícias, armas e testes da ficha.





Cores Principais
