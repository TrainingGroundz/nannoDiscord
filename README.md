# Bot Discord NSFW

Bem-vindo ao **Bot NSFW para Discord!** Este bot foi desenvolvido para adicionar uma variedade de funcionalidades e entretenimento para servidores NSFW no Discord. Abaixo, você encontrará informações detalhadas sobre suas principais características e comandos.

## Funcionalidades Principais

### Sistema de Economia - "Pikas e VIPs"
- O bot possui um sistema de economia integrado no MongoDB, com uma moeda denominada "pikas" com diversas funcionalidades

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
   - `-pikas` - Verifica o saldo de "pikas".
   - `-vips` - Consulta o saldo de VIPs.
   - `toppikas pagina Ex.: 1, 2, 3` - Exibe o rank com os usuários mais ricos do servidor.
   - `topvip pagina Ex.: 1, 2, 3` - Exibe o rank com os usuários que possuem o maior número de **VIPS** (*Vips* podem ser coletados no jogo de advinhação)

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


## Requisitos
- Certifique-se de que o bot tenha as permissões necessárias no servidor, os IDS dos cargos e canais estejam de acordo com sua preferência em seu servidor, e o arquivo `.env` esteja preenchido corretamente com seus _tokens_ `MONGO` e `DISCORD`.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório do bot.

**Divirta-se com o Bot NSFW para Discord!** 🎉
