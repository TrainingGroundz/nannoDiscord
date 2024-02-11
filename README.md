<div style="float: right;">

[![GitHub stars](https://img.shields.io/github/stars/MatheusCoding/nannoDiscord.svg?style=flat-square&logo=github&colorB=white&label=likes&logoWidth=25&logoColor=white)](https://github.com/MatheusCoding/nannoDiscord/stargazers)
</div>

# Bot Discord NSFW

Bem-vindo ao **Bot NSFW para Discord!** Este bot foi desenvolvido para adicionar uma variedade de funcionalidades e entretenimento para servidores NSFW no Discord. Abaixo, você encontrará informações detalhadas sobre suas principais características e comandos.

## Funcionalidades Principais

### Sistema de Economia - "Pikas e VIPs"
- O bot possui um sistema de economia integrado no MongoDB, ranks com diversas funcionalidades.

### VIPs
- Verifique o saldo de VIPs usando o comando `!vips`.

### Sistema de Moderação
- O bot inclui comandos de moderação para manter a ordem no servidor.
- O sistema de avisos e mutes registra o comportamento do usuário, e o mute/banimento é aplicado após atingir um número específico de avisos.

### Jogo de Adivinhação
- Participe do jogo de adivinhação, onde os membros tentam decifrar uma sequência numérica contendo um número secreto.
- Receba dicas durante o jogo e tenha 7 chances para acertar.

### Sistema de Atendimento
- Abra tickets de atendimento privados com membros e moderadores, ao final do atendimento o membro pode avaliar como foi atendido e os moderadores serão notificados.
- Opções de atendimento disponíveis:
  - **Dúvidas**
  - **Denunciar membro**
  - **Apelar punição**
  - **Verificações**
  - **Comprar Vip**
  - **Reinvindicar prêmios**
  - **Parcerias**
  - **Participar da Staff**
  - **Reportar Bug**
  - **Outras**


## Comandos Principais

1. **Economia**
   - `-daily` - Coleta suas "pikas" diárias, recompensa dobrada para cargo especifico.
   - `-pikas @membro` - Verifica o saldo de "pikas" de um membro especifico ou do proprio autor do comando.
   - `-vips @membro` - Consulta o saldo de "VIPs" de um membro especifico ou do proprio autor do comando.
   - `toppikas pagina Ex.: 1, 2, 3` - Exibe o rank com os usuários mais ricos do servidor.
   - `topvip pagina Ex.: 1, 2, 3` - Exibe o rank com os usuários que possuem o maior número de **VIPS** (*Vips* podem ser coletados no jogo de advinhação)
   - `-pagar @membro quantidade_pikas` - Transfere saldo de **pikas** entre os membros.


2. **Moderação**
   - `-mod mute @usuário tempo_em_minutos` - Abre um menu com os motivos já prontos para os moderadores selecionarem, o aviso de mute será enviado para um canal de moderação especifico e também irá notificar o membro na DM. Caso não seja passado o tempo, será adicionado o mute máximo de 28 dias ao membro.
   - `-mod aviso @usuário` - Funciona da mesma forma que o comando mute, porém como o nome já diz são avisos, caso o membro insistir em infringir as regras irá receber uma punição mais severe no aviso 3, 6, 9 será apenas mute no aviso 12 ele irá receber um banimento. Assim como o comando de mute irá notificar o membro e os moderadores sobre as punições conforme necessário. Todos os 12 avisos serão removidos do usuario antes do banimento.
   - `-mod ban @usuário` - Bane o usuário, notifica DM do membro e os moderadores.
   - `-unmute @usuário` - Remove o mute do usuário, notifica os moderadores e a DM do membro.
   - `-unban @usuário` - Remove o ban do usuário, nofica moderadores e DM do membro.
   - `-removeravisos @usuário quantidade` - Remove avisos do usuário, verifica saldo e remove se a quantidade for menor que ou igual o saldo atual do membro.
   - `-removermutes @usuário quantidade` - Remove mutes do usuário, verifica saldo e remove se a quantidade for menor que ou igual o saldo atual do membro.
   - `-setup` - Envia o Menu de Atendimento para o canal
   - `removeedp | removevip | addvip | addedp` - Comandos para adicionar e remover cargos.


3. **Jogos e Interacão**
   - `-n` - Inicia o jogo de adivinhação. Você terá 7 chances para acertar um número secreto em um intervalo gerado aleatoriamente, dicas serão exibidas conforme você se aproxima ou se afasta do número secreto, todos podem participar do mesmo jogo, porém o ganhador das recompensas será apenas o membro que iniciou o jogo!
   - `-s` - Sequestra um membro, caso o autor do comando satisfaça os requisitos do sequestro (será cobrada uma taxa de `vip` e `pikas`. O membro sequestrado é liberado automaticamente após *5* minutos.
   - `-r mensagem_pra_repetir` - Comando simples para repetir a mensagem do membro, onde a mensagem do bot é apagada logo em seguida, simulando uma conversa.
   - `-av @membro` - Envia uma mensagem exibindo o avatar do membro, caso seja passado o `membro`, se não for passado é exibido o avatar do usuário que invocou o comando.

## Requisitos
- Certifique-se de que o bot tenha as permissões necessárias no servidor.
- IDS dos cargos e canais estejam de acordo com sua preferência em seu servidor.
- O arquivo `.env` esteja preenchido corretamente com seus _tokens_ `MONGO` e `DISCORD`.
- As bibliotecas necessárias estejam instaladas.
- Versão Python recomendada `3.11.7`.


## Instalação de Dependências

Para configurar o ambiente de desenvolvimento, siga as etapas abaixo para instalar as dependências necessárias.

### Pré-requisitos

Certifique-se de ter o Python e o GIT instalados no seu sistema. Caso contrário, faça o download e instale a versão mais recente do [Python](https://www.python.org/downloads/) e do [GIT](https://git-scm.com/downloads/).

### Instalação

1. Clone este repositório em seu ambiente local:

    ```bash
    git clone https://github.com/MatheusCoding/nannoDiscord.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd nannoDiscord
    ```

3. Instale as dependências usando o `pip` e o arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

Este comando instalará automaticamente todas as dependências necessárias para o seu projeto.

### Configuração do Ambiente Virtual (Opcional, mas Recomendado)

Para isolar as dependências do projeto, você pode configurar um ambiente virtual. Isso é especialmente útil se estiver trabalhando em vários projetos para evitar conflitos de dependências.

1. Instale a biblioteca `virtualenv` (caso ainda não tenha):

    ```bash
    pip install virtualenv
    ```

2. Crie um ambiente virtual no diretório do projeto:

    ```bash
    virtualenv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - No Linux/Mac:

        ```bash
        source venv/bin/activate
        ```


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório do bot.

Se este projeto trouxe algo positivo à sua jornada, uma ⭐️ seria incrível.


**✨Divirta-se com o Bot NSFW para Discord!** 🔞🤖
