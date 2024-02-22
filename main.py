import asyncio
import random
from datetime import timedelta
from io import BytesIO
import discord
import requests
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from database import *
import datetime

load_dotenv()

id_cargo_atendente = 983142362698092555


class Dropdown(discord.ui.Select):
    def __init__(self):
        self.mensagens = {
            "1": "Para tirar dúvidas sobre o servidor, envie nesse ticket!",
            "2": "Para denunciar um membro é __indispensável__ as seguintes informações:\n\n> 1. Motivo da denúncia\n> 2. Nick do denunciado (de preferência o ID)\n> 3. Provas\n\nNa falta de alguma das informações acima é **inviável** realizar qualquer punição!",
            "3": "Para apelar uma advertência é __obrigatório__  as seguintes informações:\n\n> 1. Motivo do aviso\n> 2. Nick do punido (de preferência o ID)\n> 3. Motivos para retirarmos o aviso\n\nNa falta de alguma das informações acima é **inviável** realizar qualquer apelação!",
            "4": "Existem 3 verificações na Elite, sendo elas, Verificar Pack, Verificar Idade e Verificar Interação!\nEscolha uma delas em https://discord.com/channels/982795400798937128/982811153753341952 e abra o Ticket da verificação desejada.",
            "5": "O EDP+ Elite é uma assinatura mensal e pode ser adquirido por pikas, sonhos ou PIX.\n\n> __Pikas__: 50.000 \n> __Sonhos__: 50.000\n> __Pix__: R$5 \n\n> Para pikas, use o comando `-pagar @staff_atendente 50000` \n> Para sonhos, use o comando `+pagar @staff_atendente 50000` \n> Para PIX, envie o valor na chave:\n```00c72e9d-9db8-41a2-aa2d-7b0ec27e4447``` ou pelo QR [Code](https://media.discordapp.net/attachments/1124725730807394317/1187450957114638356/Screenshot_20231221_144430_Chrome.jpg?ex=6596eee1&is=658479e1&hm=7091c13aefaeaa74c799c71a2c332c2752e401adc98525eaed00b80095683d6a&)\nFavor enviar o comprovante do PIX!!!",
            "6": "Você ganhou um sorteio ou evento? Parabéns!!!\nInforme o nome do sorteio/evento e o prêmio",
            "7": "As parcerias do Elite são feitas através de **sorteios**. Para patrocinar um sorteio, você deve pagar o valor do prêmio, como PIX, Nitro ou Sonhos.\n\nCom isso, terá direito a mencionar o ping de sorteios e enviar o link do seu servidor.",
            "8": "Para fazer parte da __Staff EDP__, responda as perguntas abaixo:\n\n> Qual o seu nick e ID?\n> Qual a sua idade?\n> Qual a sua ocupação atual?\n> Quanto tempo faz parte da EDP?\n> Qual a sua disponibilidade?\n> Tem um bom microfone?\n> Se considera um membro ativo no servidor?\n> Já fez parte de alguma Staff? Se sim, qual?\n> Está ciente de todas as suas funções como staff previstas em https://discord.com/channels/982795400798937128/1056017474623131749 ?\n> Faça um breve resumo das regras da Elite.",
            "9": "Para reportar um **Bug** no servidor, informe:\n\n> 1. Contexto para ter encontrado o bug\n> 2. Explicação do bug\n> 3. Print ou gravação da tela mostrando o bug",
            "10": "A sua opção não está aqui?\nSem problemas, conte todos os detalhes aqui!",
        }
        options = [
            discord.SelectOption(
                value="duvidas",
                label="Tirar Dúvidas",
                emoji="<:anime_pensando:984217711708110948>",
            ),
            discord.SelectOption(
                value="denuncia",
                label="Denunciar Membro",
                emoji="<:frase_ban:1143185480557547581>",
            ),
            discord.SelectOption(
                value="apelo",
                label="Apelar Punição",
                emoji="<:pepe_ban:983158328295305227>",
            ),
            discord.SelectOption(
                value="verificaçao",
                label="Solicitar Verificação",
                emoji="<:colorido_sim:1013521308497215651>",
            ),
            discord.SelectOption(
                value="comprar edp+",
                label="Comprar EDP+",
                emoji="<:diamante_azul:1058813444704448633>",
            ),
            discord.SelectOption(
                value="resgatar prêmio",
                label="Resgatar Prêmio",
                emoji="<:colorido_festa:1013536095717298186>",
            ),
            discord.SelectOption(
                value="parceria",
                label="Fazer Parceria",
                emoji="<:dinheiro:1058813330531291236>",
            ),
            discord.SelectOption(
                value="form staff",
                label="Form Staff",
                emoji="<:emoji_bdsm:1132367626115489852>",
            ),
            discord.SelectOption(
                value="report bug",
                label="Reportar Bug",
                emoji="<:urso_besta:983194182585823263>",
            ),
            discord.SelectOption(
                value="outra",
                label="Outra Opção",
                emoji="<:emoji_caio:1060460880162197546>",
            ),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            options=options,
            custom_id="persistent_view:dropdown_help",
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "duvidas":
            await interaction.response.send_message(
                f'{self.mensagens["1"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["1"]),
            )
        elif self.values[0] == "denuncia":
            await interaction.response.send_message(
                f'{self.mensagens["2"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["2"]),
            )
        elif self.values[0] == "apelo":
            await interaction.response.send_message(
                f'{self.mensagens["3"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["3"]),
            )
        elif self.values[0] == "verificaçao":
            await interaction.response.send_message(
                f'{self.mensagens["4"]}', ephemeral=True, view=Verificacao()
            )
        elif self.values[0] == "comprar edp+":
            await interaction.response.send_message(
                f'{self.mensagens["5"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["5"]),
            )
        elif self.values[0] == "resgatar prêmio":
            await interaction.response.send_message(
                f'{self.mensagens["6"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["6"]),
            )
        elif self.values[0] == "parceria":
            await interaction.response.send_message(
                f'{self.mensagens["7"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["7"]),
            )
        elif self.values[0] == "form staff":
            await interaction.response.send_message(
                f'{self.mensagens["8"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["8"]),
            )
        elif self.values[0] == "report bug":
            await interaction.response.send_message(
                f'{self.mensagens["9"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["9"]),
            )
        elif self.values[0] == "outra":
            await interaction.response.send_message(
                f'{self.mensagens["10"]}',
                ephemeral=True,
                view=CreateTicket(self.mensagens["10"]),
            )


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Dropdown())


class CreateTicket(discord.ui.View):
    def __init__(self, msg):
        super().__init__(timeout=300)
        self.value = None
        self.msg = msg

    @discord.ui.button(
        label="Abrir Ticket", style=discord.ButtonStyle.blurple, emoji="➕"
    )
    async def confirm(
            self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.value = True
        self.stop()
        mod = interaction.guild.get_role(id_cargo_atendente)

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(
                        "Você já tem um atendimento em andamento!",
                        ephemeral=True
                    )
                    return

        async for thread in interaction.channel.archived_threads(private=True):
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(
                        "Você já tem um atendimento em andamento!", view=None
                    )
                    return

        if ticket is not None:
            await ticket.edit(archived=False, locked=False)
            await ticket.edit(
                name=f"{interaction.user.name} ({interaction.user.id})",
                auto_archive_duration=10080,
                invitable=False,
            )
        else:
            ticket = await interaction.channel.create_thread(
                name=f"{interaction.user.name} ({interaction.user.id})",
                auto_archive_duration=10080,
            )
            await ticket.edit(invitable=False)

        await interaction.response.send_message(
            f"Criei um ticket para você! {ticket.mention}", ephemeral=True
        )
        await ticket.send(f"Mencionando staff: {mod.mention}")
        await asyncio.sleep(5)
        await ticket.purge(limit=1)
        await ticket.send(
            f"📩  **|** {interaction.user.mention} ticket criado!"
            f"\n{self.msg}\nApós a sua questão ser sanada, use `-fecharticket` "
            f"para encerrar o atendimento!"
        )


class Verificacao(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value = None
        self.msg = {
            "1": 'Para se verificar como **Vendedor(a) Oficial** e poder anunciar venda de conteúdo +18, você pode escolher uma forma:\n\n- __Plaquinha__: Uma foto NSFW (parte íntima) com uma plaquinha escrito "EDP"!\n\n- __Call__: Uma call (15s) com a câmera aberta mostrando o rosto e acenando!\n\nApós realizar a verificação, você deve pagar pelo cargo, possuindo duas opções:\n\n**R$15/mês** para poder anunciar venda de pack no <#1093456891889336370>, <#1158729581956698114> e/ou privado dos membros.\n\n**R$25/mês** você adquire, além do benefício a cima, um canal exclusivo para postar seus conteúdos, com permissão de mencionar o ping de pack e enviar o link do seu servidor quantas vezes desejar.\n\nRealize o PIX nessa chave:\n```00c72e9d-9db8-41a2-aa2d-7b0ec27e4447``` ou pelo QR [Code](https://media.discordapp.net/attachments/1124725730807394317/1187450957114638356/Screenshot_20231221_144430_Chrome.jpg?ex=6596eee1&is=658479e1&hm=7091c13aefaeaa74c799c71a2c332c2752e401adc98525eaed00b80095683d6a&)\nFavor enviar o comprovante do PIX!!!',
            "2": 'Para se verificar para poder postar nos canais de **nudes**, você pode escolher uma forma:\n\n- __Selfie__: Envie uma foto sua segurando uma plaquinha escrito "EDP" + sua data de nascimento. Com isso, analisaremos se você possui +18 anos para liberar a permissão.\n\n- __RG__: Envie uma foto do seu RG ou outro documento oficial, mostrando seu nome e data de nascimento. Demais informações, se quiser, pode censurar.',
            "3": 'A verificação de interação é para liberar a permissão de postar no <#982805582924886056> e/ou <#982805666420887602>. Veja a instrução de cada canal:\n\n- __Fotinha__: Envie um vídeo de 5 segundos acenando para câmera e falando seu nick no Discord.\n\n- __Instagram__: Envie uma foto sua segurando uma plaquinha escrito "@seu_user_do_instagram" + print do seu perfil no Instagram.',
        }

    @discord.ui.button(
        label="Verificar Pack", style=discord.ButtonStyle.red, emoji="➕", row=1
    )
    async def confirm_pack(
            self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.value = True
        self.stop()
        mod = interaction.guild.get_role(id_cargo_atendente)

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(
                        "Você já tem um atendimento em andamento!",
                        ephemeral=True
                    )
                    return

        async for thread in interaction.channel.archived_threads(private=True):
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(
                        "Você já tem um atendimento em andamento!", view=None
                    )
                    return

        if ticket is not None:
            await ticket.edit(archived=False, locked=False)
            await ticket.edit(
                name=f"{interaction.user.name} ({interaction.user.id})",
                auto_archive_duration=10080,
                invitable=False,
            )
        else:
            ticket = await interaction.channel.create_thread(
                name=f"{interaction.user.name} ({interaction.user.id})",
                auto_archive_duration=10080,
            )
            await ticket.edit(invitable=False)

        await interaction.response.send_message(
            f"Criei um ticket para você! {ticket.mention}",
            ephemeral=True,
        )
        await ticket.send(f"Mencionando staff: {mod.mention}")
        await asyncio.sleep(5)
        await ticket.purge(limit=1)
        await ticket.send(
            f"📩  **|** {interaction.user.mention} ticket criado!"
            f'\n\n\n{self.msg["1"]}\nApós a sua questão ser sanada, você pode '
            f"usar `-fecharticket` para encerrar o atendimento!"
        )

    @discord.ui.button(
        label="Verificar Idade", style=discord.ButtonStyle.green, emoji="➕",
        row=2
    )
    async def confirm_idade(
            self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.value = True
        self.stop()
        mod = interaction.guild.get_role(id_cargo_atendente)

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(
                        "Você já tem um atendimento em andamento!",
                        ephemeral=True
                    )
                    return

        async for thread in interaction.channel.archived_threads(private=True):
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(
                        "Você já tem um atendimento em andamento!", view=None
                    )
                    return

        if ticket is not None:
            await ticket.edit(archived=False, locked=False)
            await ticket.edit(
                name=f"{interaction.user.name} ({interaction.user.id})",
                auto_archive_duration=10080,
                invitable=False,
            )
        else:
            ticket = await interaction.channel.create_thread(
                name=f"{interaction.user.name} ({interaction.user.id})",
                auto_archive_duration=10080,
            )
            await ticket.edit(invitable=False)

        await interaction.response.send_message(
            f"Criei um ticket para você! {ticket.mention}", ephemeral=True
        )
        await ticket.send(f"Mencionando staff: {mod.mention}")
        await asyncio.sleep(5)
        await ticket.purge(limit=1)
        await ticket.send(
            f"📩  **|** {interaction.user.mention} ticket criado!"
            f'\n{self.msg["2"]}\nApós a sua questão ser sanada, você pode usar '
            f"`-fecharticket` para encerrar o atendimento!"
        )

    @discord.ui.button(
        label="Verificar Interação", style=discord.ButtonStyle.gray, emoji="➕",
        row=3
    )
    async def confirm_interacao(
            self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.value = True
        self.stop()
        mod = interaction.guild.get_role(id_cargo_atendente)

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(
                        "Você já tem um atendimento em andamento!",
                        ephemeral=True
                    )
                    return

        async for thread in interaction.channel.archived_threads(private=True):
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(
                        "Você já tem um atendimento em andamento!", view=None
                    )
                    return

        if ticket is not None:
            await ticket.edit(archived=False, locked=False)
            await ticket.edit(
                name=f"{interaction.user.name} ({interaction.user.id})",
                auto_archive_duration=10080,
                invitable=False,
            )
        else:
            ticket = await interaction.channel.create_thread(
                name=f"{interaction.user.name} ({interaction.user.id})",
                auto_archive_duration=10080,
            )
            await ticket.edit(invitable=False)
        await interaction.response.send_message(
            f"Criei um ticket para você! {ticket.mention}", ephemeral=True
        )
        await ticket.send(f"Mencionando staff: {mod.mention}")
        await asyncio.sleep(5)
        await ticket.purge(limit=1)

        await ticket.send(
            f"📩  **|** {interaction.user.mention} ticket criado!"
            f'\n{self.msg["3"]}\nApós a sua questão ser sanada, você pode usar '
            f"`-fecharticket` para encerrar o atendimento!"
        )


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="-", intents=discord.Intents.all())

    async def on_ready(self):
        activity = discord.Game(name="com ELITE DAS PUTARIAS", type=3)
        await self.change_presence(status=discord.Status.online,
                                   activity=activity)
        print(f"Sou o {self.user} e acabei de me conectar")

    async def setup_hook(self):
        self.add_view(DropdownView())


client = Client()


@client.command(name="r", description="Repita algo")
@commands.has_permissions(send_tts_messages=True)
async def r(ctx, *, message: commands.clean_content = None):
    if message is not None:
        await ctx.message.delete()
        async with ctx.typing():
            await asyncio.sleep(2)
            await ctx.send(message)

    await ctx.message.delete()

    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.send(
            f"Ei {ctx.author.mention} amiguinho, é pra repetir uma mensagem "
            "e você não deixou mensagem alguma, cabeça de vento"
        )


@r.error
async def repeat_message_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "Você não tem a tag <@&983012540663599114> para utilizar " "esse comando",
            allowed_mentions=discord.AllowedMentions(roles=False,
                                                     everyone=False),
        )


@client.command(name="addvip", description="Adiciona saldo vip no membro.")
@commands.has_guild_permissions(ban_members=True)
async def addvip(ctx, membro: discord.Member, quantidade: int):
    if not membro or not quantidade:
        await ctx.send(
            f"{ctx.author.mention} O comando deve ser usado da seguinte "
            "forma `-addvip @membro quantidade`"
        )

        return
    else:
        await add_vip(membro, quantidade)
        await ctx.send(
            f"{ctx.author.mention} O valor de **{quantidade} VIPS** "
            f":moneybag: foi enviado com sucesso para **{membro.global_name}**"
        )


@addvip.error
async def addvip_error(ctx, error):
    error_messages = {
        commands.MissingPermissions: lambda
            e: "Você não tem permissão para usar este comando!",
        commands.MissingRequiredArgument: lambda
            e: "Opaaa, algo deu errado. Use o comando corretamente mencionando o membro que deseja adicionar saldo!",
        commands.BadArgument: lambda
            e: "Hmmm, eu não consegui encontrar esse membro. Certifique-se de mencionar um membro válido!",
    }

    for error_type, message_func in error_messages.items():
        if isinstance(error, error_type):
            await ctx.send(message_func(error) + " " + ctx.author.mention)
            break


@client.command(name="addedp", description="Adiciona o edp no membro.")
@commands.has_guild_permissions(ban_members=True)
async def addedp(ctx, membro: discord.Member):
    edp = ctx.guild.get_role(983142637492137985)
    if edp not in membro.roles:
        await membro.add_roles(edp)
        await ctx.send("Cargo setado em " + membro.mention)
    else:
        await ctx.send(f"{membro.mention} já tem esse cargo")


@addedp.error
async def addedp_error(ctx, error):
    error_messages = {
        commands.MissingPermissions: lambda
            e: "Você não tem permissão para usar este comando!",
        commands.MissingRequiredArgument: lambda
            e: "Opaaa, algo deu errado. Use o comando corretamente mencionando "
               "o membro que deseja atribuir o cargo!",
        commands.BadArgument: lambda
            e: "Hmmm, eu não consegui encontrar esse membro. "
               "Certifique-se de mencionar um membro válido!",
    }

    for error_type, message_func in error_messages.items():
        if isinstance(error, error_type):
            await ctx.send(message_func(error) + " " + ctx.author.mention)
            break


@client.command(name="removevip", description="Remove saldo vip do membro.")
@commands.has_guild_permissions(ban_members=True)
async def removevip(ctx, membro: discord.Member, quantidade: int):
    check = await checar_vips(membro)
    if not membro or not quantidade:
        await ctx.send(
            f"{ctx.author.mention} O comando deve ser usado da seguinte forma "
            "`-removevip @membro quantidade`\n\nLembrando que a quantidade deve ser "
            "menor/igual o saldo atual de **{membro.global_name}**\nVocê pode "
            "verificar o saldo com o comando `-vips @membro`"
        )

        return
    else:
        if check >= quantidade:
            await remove_vip(membro, quantidade)
            await ctx.send(
                f"{ctx.author.mention} O valor de **{quantidade} VIPS** "
                f":moneybag: foi removido com sucesso de **{membro.name}**"
            )
        else:
            await ctx.send(
                f"{ctx.author.mention} Você não pode remover **{quantidade} VIPS** "
                f":moneybag: pois **{membro.name}** tem um saldo de **{check} VIP**"
            )


@removevip.error
async def removevip_error(ctx, error):
    error_messages = {
        commands.MissingPermissions: lambda
            e: "Você não tem permissão para usar este comando!",
        commands.MissingRequiredArgument: lambda
            e: "Opaaa, algo deu errado. Use o comando corretamente mencionando "
               "o membro que deseja remover saldo!",
        commands.BadArgument: lambda
            e: "Hmmm, eu não consegui encontrar esse membro. Certifique-se de "
               "mencionar um membro válido!",
    }

    for error_type, message_func in error_messages.items():
        if isinstance(error, error_type):
            await ctx.send(message_func(error) + " " + ctx.author.mention)
            break


@client.command(name="removeedp", description="Remove o edp do membro.")
@commands.has_guild_permissions(ban_members=True)
async def removeedp(ctx, membro: discord.Member):
    edp = ctx.guild.get_role(983142637492137985)
    if edp in membro.roles:
        await membro.remove_roles(edp)
        await ctx.send(f"Cargo removido de {membro.mention}")
    else:
        await ctx.send(
            f"Ei meu chapa {ctx.author.mention}, esse carinha não tem a tag "
            f"edp, favor prestar mais atenção diabo"
        )


@removeedp.error
async def removeedp_error(ctx, error):
    error_messages = {
        commands.MissingPermissions: lambda
            e: "Você não tem permissão para usar este comando!",
        commands.MissingRequiredArgument: lambda
            e: "Opaaa, algo deu errado. Use o comando corretamente mencionando o "
               "membro que deseja remover o cargo!",
        commands.BadArgument: lambda
            e: "Hmmm, eu não consegui encontrar esse membro. Certifique-se de "
               "mencionar um membro válido!",
    }

    for error_type, message_func in error_messages.items():
        if isinstance(error, error_type):
            await ctx.send(message_func(error) + " " + ctx.author.mention)
            break


@client.command(name="s", description="Comando secreto")
async def s(ctx, membro: discord.Member):
    channel_commands = client.get_channel(982805491732320336)
    channel_porao = client.get_channel(1060307386889408564)
    sequestrador = ctx.author.guild.get_role(1060327608530776125)
    sequestrado = ctx.author.guild.get_role(1148067988470239252)

    permanent_roles = [
        1047588622603407501,
        982821606961344543,
        1172200597647269989,
    ]

    saldo = await checar_saldo(ctx.author)
    vips = await checar_vips2(ctx.author)

    if saldo < 7000:
        await channel_commands.send(
            f"O dotado {ctx.author.mention} não conseguiu "
            f"sequestrar a passiva **{membro.global_name}** "
            "por ter pikas insuficientes💰\nPara verificar "
            "suas pikas, use o comando `-pikas`"
        )
        return

    if not vips:
        await channel_commands.send(
            f"O dotado {ctx.author.mention} não conseguiu sequestrar "
            f"a passiva **{membro.global_name}** "
            f"por ter **VIPS** insuficientes💰 "
            f"verifique seu saldo com `-vips` "
        )
        return
    else:
        if not any(role.id in permanent_roles for role in ctx.author.roles):
            custo_pikas = 7000
        else:
            custo_pikas = 3000

        await alterar_saldo(ctx.author, -custo_pikas)
        await ctx.author.add_roles(sequestrador)
        await membro.add_roles(sequestrado)

        await channel_porao.send(
            f"O dotado {ctx.author.mention} pagou **{custo_pikas} "
            f"pikas** + **1 VIP** e sequestrou a passiva "
            f"{membro.mention} <:emoji_caio:1060460880162197546> "
            f"`verifique seu saldo com -vips`"
        )
        await channel_commands.send(
            f"O dotado {ctx.author.mention} pagou **{custo_pikas} "
            f"pikas** + **1 VIP** e sequestrou a passiva "
            f"{membro.mention} <:emoji_caio:1060460880162197546> "
            f"`verifique seu saldo com -vips`"
        )

        await decrementar_vitorias(ctx.author)

        await asyncio.sleep(300)

        await ctx.author.remove_roles(sequestrador)
        await membro.remove_roles(sequestrado)

        await channel_commands.send(
            f"Tempo esgotado! {membro.mention} foi liberado")


@s.error
async def s_error(ctx, error):
    error_messages = {
        commands.MissingRequiredArgument: lambda
            e: "Opaaa, algo deu errado. Use o comando corretamente mencionando o "
               "membro que deseja **sequestrar** !",
        commands.BadArgument: lambda
            e: "Hmmm, eu não consegui encontrar esse membro. "
               "Certifique-se de mencionar um membro válido !",
    }

    for error_type, message_func in error_messages.items():
        if isinstance(error, error_type):
            await ctx.send(
                message_func(error),
                allowed_mentions=discord.AllowedMentions(roles=False),
            )
            break


@client.command(name="n")
@commands.cooldown(1, 60, commands.BucketType.guild)
async def n(ctx):
    inicio = random.randint(50, 3500)
    intervalo = 1500
    fim = inicio + intervalo
    porao_channel = client.get_channel(1187065450459316364)
    vip = ctx.guild.get_role(983012540663599114)

    numero_secreto = random.randint(inicio, fim)
    print("numero secreto", numero_secreto)

    embed = discord.Embed(
        title="Descubra o número secreto e ganhe VIP",
        description=f"<:emoji_caio:1060460880162197546> Seu número secreto "
                    f"está entre **{inicio}** e **{fim}**\n"
                    f"Você tem 7 chances de acertá-lo em **2 minutos**\n\n\n"
                    f"Digite `!stop` para terminar o jogo a qualquer momento",
    )

    await porao_channel.send(embed=embed)

    def dicas(arg):
        if int(arg) < numero_secreto:
            return " ⬅️ é menor que o número secreto!"
        else:
            return " ⬅️ é maior que o número secreto!"

    async def calcular_proximidade(numero_secreto, resposta_user):
        diferenca = abs(numero_secreto - resposta_user)

        if diferenca <= 10:
            return discord.Color.dark_red(), (
                f"**Muito quente** 🔥!!!\n{resposta.author.mention} está muito"
                f" perto do número secreto, "
                f"á uma diferença de apenas **10** números no máximo! 🌞"
            )

        elif 10 < diferenca <= 50:
            return discord.Color.red(), (
                f"**Quente** ☀️!!\n{resposta.author.mention} está se "
                f"aproximando do número secreto! 🔥"
            )

        elif 50 < diferenca <= 500:
            return (
                discord.Color.from_rgb(255, 105, 97),
                (
                    f"**Morno** 😎!\n{resposta.author.mention} ainda "
                    f"falta um pouco, confia! 🌡️"
                ),
            )

        elif 500 < diferenca <= 800:
            return (
                discord.Color.from_rgb(0, 255, 255),
                (
                    f"❄️‍🦰 **Uh, está frio aqui né?** ❄️\n"
                    f"{resposta.author.mention} melhor ir buscar um agasalho"
                    f" pra gente não morrer de frio por aqui! 🧥"
                ),
            )

        elif 800 < diferenca <= 1000:
            return (
                discord.Color.blue(),
                (
                    f"👩‍🦰 **Brrr... está congelando!** ❄️\n"
                    f"{resposta.author.mention} <= Se dependermos dessa "
                    f"pessoa aqui estaremos todos mortos de frio! 🥶"
                ),
            )

        else:
            return (
                discord.Color.dark_blue(),
                (
                    f"🐻‍❄️ **Ops, parece que o {resposta.author.mention} gosta "
                    f"do Polo Norte!** ❄️\nA diferença é tão grande que até os "
                    f"**pinguins** estão surpresos! 🐧"
                ),
            )

    tentativas_restantes = 7
    numero_invalido = 0

    try:
        while tentativas_restantes > 0:
            resposta = await client.wait_for(
                "message",
                check=lambda m: m.channel == porao_channel
                                and m.author != client.user
                                and not m.content.startswith("-n"),
                timeout=120,
            )

            if "!stop" in resposta.content:
                embed_stop = discord.Embed(
                    title="O jogo foi encerrado pelo comando `!stop`",
                    description=f"Agora ninguém vai ganhar as recompensas da"
                                f" {client.user.mention} 😭\n"
                                f"Graças ao {resposta.author.mention} que"
                                f" encerrou o jogo 🥺",
                )

                await porao_channel.send(embed=embed_stop)
                break

            try:
                resposta_user = int(resposta.content)

                if not inicio <= resposta_user <= fim:
                    embed_range = discord.Embed(
                        title=f"❌ {resposta.content} está fora do intervalo!\n"
                              f"O número secreto deve estar entre {inicio} e "
                              f"{fim}! Boa sorte 🫱🏻‍🫲🏾",
                        description=f"{resposta.author.mention} 😭 Não se "
                                    f"preocupe, você ainda tem "
                                    f"**{tentativas_restantes}** tentativas ✔️",
                    )

                    await porao_channel.send(embed=embed_range)
                    continue

            except ValueError:
                numero_invalido += 1
                if numero_invalido == 2:
                    await porao_channel.send(
                        f"{resposta.author.mention} **Você precisa se "
                        f"concentrar mais!** 🙏🏻\n**{resposta.content}** `"
                        f"<= Em que universo isso aqui é um número pra você"
                        f" meu querido ?!🤬`"
                    )

                else:
                    if tentativas_restantes == 0:
                        break
                    await porao_channel.send(
                        f"Por favor, digite um número válido.\n"
                        f"Não se preocupe, você ainda tem "
                        f"**{tentativas_restantes}** tentativas ✔️"
                    )

                continue

            saldo_vip = await checar_vips(ctx.author)
            cor_embed, mensagem = await calcular_proximidade(
                numero_secreto, resposta_user
            )
            if resposta_user != numero_secreto:
                tentativas_restantes -= 1
                if resposta_user != numero_secreto:
                    hints = dicas(resposta_user)
                    if tentativas_restantes:
                        embed_tentativa = discord.Embed(
                            title=f"{resposta_user} {hints}",
                            description=f"{mensagem}\n\n"
                                        f"✔️ {tentativas_restantes} "
                                        f"tentativas restantes",
                            color=cor_embed,
                        )

                        await porao_channel.send(embed=embed_tentativa)

            else:
                com_vip = "já está registrado"
                sem_vip = "foi registrado"
                tem_vip = vip in ctx.author.roles
                mensagem_registro = (
                    (
                        f"🌟 {ctx.author.mention} {com_vip} no "
                        f"<@&983012540663599114> "
                        f"<:anime_popo_face:1013232728545697802>"
                        f"\nForam adicionadas 5000 **pikas** "
                        f":moneybag: no seu saldo"
                    )
                    if tem_vip
                    else (
                        f"{ctx.author.mention} {sem_vip} no <@&983012540663599114>"
                        f" <:anime_popo_face:1013232728545697802>\n Foram "
                        f"adicionadas 5000 **pikas** :moneybag: no seu saldo"
                    )
                )

                embed_acerto = discord.Embed(
                    description=f"# Parabéns 👻!\n O número secreto era "
                                f"**{numero_secreto}**\n{mensagem_registro}"
                                f"\nVocê ganhou **1 VIP** e agora possui "
                                f"{saldo_vip + 1} VIPs\nUse o comando "
                                f"`-topvip` para ver sua posição!",
                    color=discord.Color.light_grey(),
                )

                embed_acerto.set_image(
                    url="https://media1.tenor.com/m/W7g4Ay3jTCAAAAAd/nanno.gif"
                )

                if tem_vip:
                    await alterar_saldo(ctx.author, 5000)
                else:
                    await ctx.author.add_roles(vip)
                    await alterar_saldo(ctx.author, 5000)

                await porao_channel.send(embed=embed_acerto)
                await incrementar_vitorias(ctx.author)
                break

            await asyncio.sleep(0.5)

            if tentativas_restantes % 5 == 0:
                await asyncio.sleep(0.5)

        else:
            embed_game_over = discord.Embed(
                title="Game Over",
                description=f"☠️ É meu puto, pensei que você fosse um "
                            f"verdadeiro **transudo**, mas me enganei!\nO "
                            f"número secreto era **{numero_secreto}**\n"
                            f"Você não tem mais tentativas! 😵",
                color=discord.Color.red(),
            )

            await porao_channel.send(embed=embed_game_over)
    except asyncio.TimeoutError:
        embed_timeout = discord.Embed(
            title="Game Over",
            description=f"☠️ **Tempo esgotado!** ☠️\nO número secreto "
                        f"era **{numero_secreto}**",
            color=discord.Color.red(),
        )

        await porao_channel.send(embed=embed_timeout)


@n.error
async def n_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"**💕{ctx.author.mention} Descanse um pouquinho enquanto recarrego "
            f"minhas energias! ✨\n⏳ Próximo jogo liberado em "
            f"{round(error.retry_after)} segundos**!"
        )


@client.command(name="setup")
@commands.has_permissions(manage_guild=True)
async def setup(ctx):
    embed = discord.Embed(
        title="Central de Atendimento EDP ☎️",
        description="Nesse menu, você pode entrar em contato com a nossa "
                    "equipe de atendimento da Elite!\n\nPara evitar problemas, "
                    "leia as opções com atenção e lembre-se que ao criar um "
                    "Ticket fora do horário abaixo, é provável que demore "
                    "mais para ser atendido.\n\n**Horário de atendimento:**"
                    "\n- Segunda a sexta-feira: 08h às 22h\n- Final de semana"
                    " e feriado: 10h às 20h",
        color=discord.Color.red(),
    )

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/1100253073596764190/1179374529173270589/Screenshot_20231129_075105_Photos.jpg"
    )
    embed.set_image(
        url="https://media.discordapp.net/attachments/1124725730807394318/1187122761118777434/standard_8.gif"
    )

    await ctx.send(embed=embed, view=DropdownView())


@client.command(name="fecharticket")
async def _fecharticket(ctx):
    mod = ctx.guild.get_role(id_cargo_atendente)

    if str(ctx.author.id) in ctx.channel.name or mod in ctx.author.roles:
        await ctx.send(
            f"O ticket foi arquivado por {ctx.author.mention}, "
            f"obrigado por entrar em contato!"
        )

        await ctx.channel.edit(locked=True)
        await asyncio.sleep(1)

        reacoes = ["😡", "😤", "🙂", "😄"]
        msg = await ctx.send(
            "Por favor, avalie seu atendimento\n"
            "😡 Experiência frustrante, atendimento precisa melhorar urgentemente.\n"
            "😤 Não muito satisfeito com o serviço prestado, há espaço para melhorias.\n"
            "🙂 Atendimento razoável, mas poderia ser mais eficiente.\n"
            "😄 Excelente atendimento! Satisfeito com a experiência proporcionada."
        )

        for reacao in reacoes:
            await msg.add_reaction(reacao)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in reacoes

        try:
            reaction, _ = await client.wait_for(
                "reaction_add", timeout=60.0, check=check
            )

            canal_avaliacoes = ctx.guild.get_channel(1195429851943948399)
            await canal_avaliacoes.send(
                f"Avaliação de {ctx.author.mention}: {str(reaction.emoji)}"
            )
        except asyncio.TimeoutError:
            pass
        await ctx.channel.edit(archived=True)

    else:
        await ctx.send("Isso não pode ser feito aqui...")


@client.command(name="pikas")
async def _saldo(ctx, user: discord.User = None):
    if user:
        moedas_user = await checar_saldo(user)
        await ctx.send(f"{user.mention} têm **{moedas_user} pikas**")
        return

    moedas_author = await checar_saldo(ctx.author)
    await ctx.send(
        f"{ctx.author.mention} possui **{moedas_author} "
        "pikas <:emoji_pica:1014864321349681232>**"
    )


@_saldo.error
async def saldo_error(ctx, error):
    if isinstance(error, commands.UserNotFound):
        await ctx.send(
            "😹 Todos podem usar para ver as pikas do coleguinha, mas é "
            "complicado encontrar um coleguinha que não tem **pikas** 🤡 "
            "\n\nTente novamente, mas lembre-se de verificar saldo de alguém"
            " com **pikas**"
        )


@client.command(name="addpikas")
@commands.has_guild_permissions(administrator=True)
async def _addpikas(
        ctx: commands.Context, user: discord.User = None, quantidade: int = None
):
    if not user or not quantidade:
        await ctx.send(
            f"{ctx.author.mention} O comando deve ser usado da seguinte "
            "forma `-addpikas @membro quantidade`"
        )

        return
    else:
        await alterar_saldo(user, quantidade)
        await ctx.send(
            f"{ctx.author.mention} O valor de **{quantidade} pikas** "
            ":moneybag: foi enviado com sucesso para **{user.global_name}**"
        )


@_addpikas.error
async def addpikas_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            f"{ctx.author.mention} Olá pessoa, parece que você não tem "
            "privilégios suficientes para executar esse comando 😞"
        )
    elif isinstance(error, commands.UserNotFound):
        await ctx.send(
            f"{ctx.author.mention} Olá pessoa, parece que o usuário não "
            "foi encontrado 😞"
        )


@client.command(name="removepikas")
@commands.has_guild_permissions(administrator=True)
async def _removepikas(
        ctx: commands.Context, user: discord.User = None, quantidade: int = None
):
    if not user or not quantidade:
        await ctx.send(
            f"{ctx.author.mention} O comando deve ser usado da seguinte "
            "forma `-removepikas @membro quantidade`"
        )

        return

    moedas = await checar_saldo(user)

    if moedas > quantidade:
        await alterar_saldo(user, -quantidade)
        await ctx.send(
            f"{ctx.author.mention} O valor de **{quantidade} pikas** "
            f":moneybag: foi removido de **{user.global_name}**"
        )

    else:
        await ctx.send(
            f"{ctx.author.mention}\n\n🗶Ei coleguinha, {user.mention} tem "
            f"apenas **{moedas} pikas**\nA quantidade a ser removida deve ser "
            "menor que o saldo atual do membro😋"
        )


@_removepikas.error
async def removepikas_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            f"{ctx.author.mention} Olá pessoa, parece que você não tem "
            "privilégios suficientes para executar esse comando 😞"
        )
    elif isinstance(error, commands.UserNotFound):
        await ctx.send(
            f"{ctx.author.mention} Olá pessoa, parece que o usuário não foi "
            "encontrado 😞"
        )


@client.command(name="daily")
async def _daily(ctx):
    await novo_usuario(ctx.author)
    resultado, tempo_restante, timestamp = await checar_cooldown(ctx.author)
    cargo_2x = [1047588622603407501]
    valor = random.randint(1000, 5000)
    valor_2x = random.randint(2000, 10000)
    msg_semvip = f"{ctx.author.mention} ganhou **{valor} pikas** hoje <:diabinha_pica:1132367768835076176>\nSabia que você poderia receber **2x mais pikas** com o <@&1047588622603407501>?\nAdquira agora em <#1047577913995829380>!"
    msg_vip = f"{ctx.author.mention} ganhou **{valor_2x} pikas** hoje <:diabinha_pica:1132367768835076176>\nVocê ganhou **2x mais pikas** por ter <@&1047588622603407501>"

    if not resultado:
        if any(role.id in cargo_2x for role in ctx.author.roles):
            await ctx.send(
                msg_vip, allowed_mentions=discord.AllowedMentions(roles=False)
            )
            await alterar_saldo(ctx.author, valor_2x)
            await add_cooldown(ctx.author)
        else:
            await ctx.send(
                msg_semvip,
                allowed_mentions=discord.AllowedMentions(roles=False)
            )

            await alterar_saldo(ctx.author, valor)
            await add_cooldown(ctx.author)
    else:
        embed_daily = discord.Embed(
            title="❌ Desculpe, você só pode usar o comando `daily` "
                  "uma vez por dia! :moneybag:",
            description=f"\nAinda faltam **{tempo_restante}** :alarm_clock:"
                        f" para coletar o prêmio diário de **pikas** "
                        f"novamente\nEspero você {ctx.author.mention} "
                        f"às `{timestamp}` 💕\n||Compreendo sua "
                        f"necessidade de pegar **pikas**, mas regras são regras 😏||",
            color=discord.Color.from_rgb(255, 255, 255),
        )

        await ctx.send(embed=embed_daily)


@client.command(name="pagar")
async def pagamento(ctx, usuario: discord.User, valor: int):
    moedas = await checar_saldo(ctx.author)
    if moedas >= valor:
        await alterar_saldo(ctx.author, -valor)
        await alterar_saldo(usuario, valor)
        await ctx.send(
            f"{ctx.author.mention} enviou {valor} pikas com sucesso "
            f"para {usuario} <:pica_olhos:1182843924990144602>"
        )
    else:
        await ctx.send(
            "**Você não tem pikas o suficiente para fazer esse pagamento!**"
            "\nUse o comando `-pikas` para verificar quantas pikas você tem!"
        )


@client.command(name="toppikas")
async def mostrar_rank(ctx, pagina=1, ordenar_por="moedas"):
    skip = (pagina - 1) * 5

    campo_ordenacao = ordenar_por if ordenar_por in ['moedas', 'vitorias'] else 'moedas'

    membros_servidor = [membro.id for membro in ctx.guild.members]

    pipeline = [
        {'$match': {'discord_id': {'$in': membros_servidor}}},
        {'$sort': {campo_ordenacao: -1}},
        {'$project': {'discord_id': 1, 'moedas': 1, 'vitorias': 1, '_id': 0}},
        {'$skip': skip},
        {'$limit': 5}
    ]

    resultado = usuarios.aggregate(pipeline)

    rank = []
    posicao = 1 + skip

    for usuario in usuarios.find():
        discord_id = usuario['discord_id']
        membro = ctx.guild.get_member(discord_id)

        if membro is None:
            usuarios.delete_one({'discord_id': discord_id})
            continue

    for usuario in resultado:
        discord_id = usuario['discord_id']
        moedas = usuario['moedas']
        vitorias = usuario.get('vitorias', 0)

        rank.append({
            'posicao': posicao,
            'discord_id': discord_id,
            'moedas': moedas,
            'vitorias': vitorias
        })

        posicao += 1

    if not rank:
        await ctx.send(f"**Não existem membros na página {pagina}!**")
        return

    largura_imagem = 600
    altura_imagem = 675

    fonte_nome = ImageFont.truetype("JetBrainsMono-Bold.ttf", 35)
    fonte_moedas = ImageFont.truetype("JetBrainsMono-Bold.ttf", 25)

    imagem_fundo = Image.open("background.png")
    imagem_base = Image.new("RGB", (largura_imagem, altura_imagem),
                            (40, 40, 40))
    imagem_base.paste(imagem_fundo.resize((largura_imagem, altura_imagem)),
                      (0, 0))
    desenho = ImageDraw.Draw(imagem_base)

    y_pos = 40
    for index, usuario in enumerate(rank):
        posicao = usuario["posicao"]
        nome = usuario["discord_id"]
        moedas = usuario["moedas"]
        membro = ctx.guild.get_member(nome)

        avatar_url = membro.display_avatar
        avatar = Image.open(BytesIO(requests.get(avatar_url.__str__()).content))
        avatar = avatar.resize((110, 110))

        cor_fundo_avatar = (60, 60, 60)
        desenho.rectangle([10, y_pos, 10 + 110, y_pos + 110],
                          fill=cor_fundo_avatar)

        imagem_base.paste(avatar, (10, y_pos))

        cor_texto = (255, 255, 255)

        if index == 0:
            cor_destaque = (255, 255, 0)
        elif index == 1:
            cor_destaque = (220, 220, 220)
        elif index == 2:
            cor_destaque = (255, 140, 0)
        else:
            cor_destaque = cor_texto

        desenho.text(
            (130, y_pos + 10),
            f"{posicao}. {membro.name}",
            font=fonte_nome,
            fill=cor_destaque,
        )
        desenho.text(
            (130, y_pos + 50), f"Pikas: {moedas}", font=fonte_moedas,
            fill=cor_destaque
        )
        y_pos += 120

    buffer = BytesIO()
    imagem_base.save(buffer, format="PNG")
    buffer.seek(0)

    await ctx.send(file=discord.File(buffer, filename="rank.png"))


@client.command(name="topvip")
async def rank_porao(ctx, pagina=1, ordenar_por='vitorias'):
    skip = (pagina - 1) * 5

    campo_ordenacao = ordenar_por if ordenar_por in ['moedas', 'vitorias'] else 'moedas'

    membros_servidor = [membro.id for membro in ctx.guild.members]

    pipeline = [
        {'$match': {'discord_id': {'$in': membros_servidor}}},
        {'$sort': {campo_ordenacao: -1}},
        {'$project': {'discord_id': 1, 'moedas': 1, 'vitorias': 1, '_id': 0}},
        {'$skip': skip},
        {'$limit': 5}
    ]

    resultado = usuarios.aggregate(pipeline)

    rank = []
    posicao = 1 + skip

    for usuario in usuarios.find():
        discord_id = usuario['discord_id']
        membro = ctx.guild.get_member(discord_id)

        if membro is None:
            usuarios.delete_one({'discord_id': discord_id})
            continue

    for usuario in resultado:
        discord_id = usuario['discord_id']
        moedas = usuario['moedas']
        vitorias = usuario.get('vitorias', 0)

        rank.append({
            'posicao': posicao,
            'discord_id': discord_id,
            'moedas': moedas,
            'vitorias': vitorias
        })

        posicao += 1

    if not rank:
        await ctx.send(f"**Não existem membros na página {pagina}!**")
        return

    largura_imagem = 600
    altura_imagem = 675

    fonte_nome = ImageFont.truetype("JetBrainsMono-Bold.ttf", 35)
    fonte_vitorias = ImageFont.truetype("JetBrainsMono-Bold.ttf", 25)

    imagem_fundo = Image.open("background.png")
    imagem_base = Image.new("RGB", (largura_imagem, altura_imagem),
                            (40, 40, 40))
    imagem_base.paste(imagem_fundo.resize((largura_imagem, altura_imagem)),
                      (0, 0))
    desenho = ImageDraw.Draw(imagem_base)

    y_pos = 40
    for index, usuario in enumerate(rank):
        posicao = usuario["posicao"]
        nome = usuario["discord_id"]
        vitorias = usuario["vitorias"]
        membro = client.get_user(nome)

        avatar_url = membro.display_avatar
        avatar = Image.open(BytesIO(requests.get(avatar_url.__str__()).content))
        avatar = avatar.resize((110, 110))

        cor_fundo_avatar = (60, 60, 60)
        desenho.rectangle([10, y_pos, 10 + 110, y_pos + 110],
                          fill=cor_fundo_avatar)

        imagem_base.paste(avatar, (10, y_pos))

        cor_texto = (255, 255, 255)

        if index == 0:
            cor_destaque = (255, 255, 0)
        elif index == 1:
            cor_destaque = (220, 220, 220)
        elif index == 2:
            cor_destaque = (255, 140, 0)
        else:
            cor_destaque = cor_texto

        desenho.text(
            (130, y_pos + 10),
            f"{posicao}. {membro.name}",
            font=fonte_nome,
            fill=cor_destaque,
        )
        desenho.text(
            (130, y_pos + 50),
            f"VIP: {vitorias}",
            font=fonte_vitorias,
            fill=cor_destaque,
        )
        y_pos += 120

    buffer = BytesIO()
    imagem_base.save(buffer, format="PNG")
    buffer.seek(0)

    await ctx.send(file=discord.File(buffer, filename="rank.png"))


@client.command(name="vips")
async def __saldo(ctx, membro: discord.User = None):
    if membro is None:
        saldo_author = await checar_vips(ctx.author)
        await ctx.send(
            f"{ctx.author.mention} Você possui um saldo de **{saldo_author}"
            f" VIPS <:emoji_pica:1014864321349681232>**"
        )

    else:
        saldo = await checar_vips(membro)
        await ctx.send(f"{membro.mention} tem um saldo de **{saldo} VIPS**")


@__saldo.error
async def saldo_error(ctx, error):
    if isinstance(error, commands.UserNotFound):
        await ctx.send(
            "😹Todos podem usar consultar o saldo de **VIPS** do coleguinha, "
            "mas é complicado encontrar o saldo de alguém que não **existe**"
            "🤡\n\nTente novamente, mas lembre-se de mencionar um membro existente!"
        )


class Punicoes(discord.ui.Select):
    def __init__(
            self, punicao: str, membro: discord.User, tempo_mute: int,
            id_user_interaction
    ):
        self.msg = {
            "verificacao": "Venda sem verificação",
            "idade": "Idade mínima é 16",
            "privado": "Explanar privado",
            "avatar": "Avatar impróprio",
            "offtopic": "Atrapalhar chat",
            "scam": "Venda fake",
            "calls": "Atrapalhar calls",
            "exposed": "Exposed de terceiros",
            "flood": "Flood/Spam",
            "fake": "Membro Fake",
            "14anos": "Idade insuficiente",
            "divulgacao": "Divulgação não autorizada",
            "discriminacao": "Discriminação/Assédio",
            "perseguicao": "Perseguição de membros",
            "rato": "Rato",
        }

        self.punicao = punicao
        self.membro = membro
        self.tempo = tempo_mute
        self.id_author = id_user_interaction

        options = [
            discord.SelectOption(
                value="verificacao",
                label=self.msg["verificacao"],
                emoji="<a:colorido_sim:1013521308497215651>",
            ),
            discord.SelectOption(value="idade", label=self.msg["idade"],
                                 emoji="🔞"),
            discord.SelectOption(
                value="privado",
                label=self.msg["privado"],
                emoji="<a:pepe_ban:983158328295305227>",
            ),
            discord.SelectOption(
                value="avatar",
                label=self.msg["avatar"],
                emoji="<:anime_vaca:1014871141426409574>",
            ),
            discord.SelectOption(
                value="offtopic",
                label=self.msg["offtopic"],
                emoji="<:anime_deitado:1058642904458989638>",
            ),
            discord.SelectOption(
                value="scam",
                label=self.msg["scam"],
                emoji="<:urso_besta:983194182585823263>",
            ),
            discord.SelectOption(
                value="calls",
                label=self.msg["calls"],
                emoji="<:anime_agua:983202199477817364>",
            ),
            discord.SelectOption(
                value="exposed",
                label=self.msg["exposed"],
                emoji="<:emoji_bdsm:1132367626115489852>",
            ),
            discord.SelectOption(
                value="flood",
                label=self.msg["flood"],
                emoji="<a:frase_ban:1143185480557547581>",
            ),
            discord.SelectOption(
                value="fake",
                label=self.msg["fake"],
                emoji="<:urso_pateta:1056764624457957407>",
            ),
            discord.SelectOption(
                value="14anos",
                label=self.msg["14anos"],
                emoji="<:urso_edu:983160043702722580>",
            ),
            discord.SelectOption(
                value="divulgacao",
                label=self.msg["divulgacao"],
                emoji="<:anime_pensando:984217711708110948>",
            ),
            discord.SelectOption(
                value="discriminacao",
                label=self.msg["discriminacao"],
                emoji="<:pica_pau:1130570834243747941>",
            ),
            discord.SelectOption(
                value="perseguicao",
                label=self.msg["perseguicao"],
                emoji="<:anime_omg:984217742120992769>",
            ),
            discord.SelectOption(
                value="rato",
                label=self.msg["rato"],
                emoji="<:emoji_caio:1060460880162197546>",
            ),
        ]
        super().__init__(placeholder="Selecione o motivo...", options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        membro = self.membro
        reason = self.msg[self.values[0]]
        punicao = self.punicao
        tempo = self.tempo
        author_id = self.id_author

        guild = interaction.guild
        member = guild.get_member(membro.id)
        author_member = guild.get_member(author_id)
        mutes = await checar_mutes(member)
        duracao = timedelta(minutes=tempo)
        canal_punicoes = client.get_channel(983234083918344222)
        contagem_avisos = await checar_avisos(member)
        contagem_mutes = await checar_mutes(member)

        if interaction.user.id == author_member.id:
            if member:
                if punicao == "aviso":
                    if contagem_avisos < 3 or contagem_avisos % 3 != 0:
                        await canal_punicoes.send(
                            f"O membro **{member.mention}** recebeu uma punição do "
                            f"servidor 😈 EDP 😈 aplicada por {interaction.user.mention}"
                            f"\n\n__Motivo:__  **{reason}**\n\n__Punição:__  "
                            f"**[{self.punicao.capitalize()}]\n\n**O membro "
                            f"{member.mention} já tem {contagem_avisos} Avisos "
                            f"e {contagem_mutes} Mutes"
                        )
                        await member.send(
                            f"⚠️ Você recebeu uma punição do servidor 😈 EDP 😈"
                            f"\n\n__Motivo:__  **{reason}**  \n\n__Punição:__  "
                            f"**[{self.punicao.capitalize()}]**\n\nReceber múltiplas"
                            f" punições pode acarretar em mute eterno ou banimento!"
                            f"\n\nO que fazer agora?\nQueremos ajudar você a continuar"
                            f" no servidor. Para isso, é importante:\n> 1. Conhecer "
                            f"as <#982810991194689546> da Elite e não violá-las;\n> 2."
                            f" Apelar a punição em <#1077273053806997554> caso "
                            f"acredite que cometemos um erro."
                        )
                    elif contagem_avisos == 3:
                        await canal_punicoes.send(
                            f"**O membro {member.mention} recebeu {contagem_avisos} "
                            f"avisos e ganhou uma punição mais severa de 24 horas"
                            f" aplicada por {interaction.user.mention}**"
                        )
                        await member.timeout(
                            timedelta(hours=24),
                            reason=f"**O membro {member.display_name} recebeu "
                                   f"{contagem_avisos} avisos e ganhou uma punição"
                                   f" mais severa de 24 horas**",
                        )
                        await member.send(
                            f"⚠️ Você recebeu uma punição do servidor 😈 EDP 😈"
                            f"\n\n__Motivo:__  **{reason}**  \n\n__Punição:__  "
                            f"**[Mute : 24 horas || Esse é o seu {contagem_avisos}º "
                            f"Aviso]**\n\nReceber múltiplas punições pode acarretar"
                            f" em mute eterno ou banimento!\n\nO que fazer agora?"
                            f"\nQueremos ajudar você a continuar no servidor. Para"
                            f" isso, é importante:\n> 1. Conhecer as "
                            f"<#982810991194689546> da Elite e não violá-las;\n> 2."
                            f" Apelar a punição em https://discord.gg/4sdVrdVjbr caso "
                            f"acredite que cometemos um erro."
                        )
                    elif contagem_avisos == 6:
                        await canal_punicoes.send(
                            f"**O membro {member.mention} recebeu {contagem_avisos} "
                            f"avisos e ganhou uma punição mais severa de 24 horas"
                            f" aplicada por {interaction.user.mention}**"
                        )
                        await member.timeout(
                            timedelta(hours=24),
                            reason=f"O membro {member.display_name} recebeu "
                                   f"{contagem_avisos} e recebeu uma punição mais"
                                   f" severa de 24 horas",
                        )
                        await member.send(
                            f"⚠️ Você recebeu uma punição do servidor 😈 EDP 😈"
                            f"\n\n__Motivo:__  **{reason}**  \n\n__Punição:__  "
                            f"**[Mute : 24 horas || Esse é o seu {contagem_avisos}º "
                            f"Aviso]**\n\nReceber múltiplas punições pode acarretar"
                            f" em mute eterno ou banimento!\n\nO que fazer agora?"
                            f"\nQueremos ajudar você a continuar no servidor. Para"
                            f" isso, é importante:\n> 1. Conhecer as "
                            f"<#982810991194689546> da Elite e não violá-las;\n> 2. "
                            f"Apelar a punição em https://discord.gg/4sdVrdVjbr caso "
                            f"acredite que cometemos um erro."
                        )
                    elif contagem_avisos == 9:
                        await canal_punicoes.send(
                            f"**O membro {member.mention} recebeu {contagem_avisos}"
                            f" avisos e recebeu uma punição mais severa de 24 horas"
                            f" aplicada por {interaction.user.mention}**"
                        )
                        await member.timeout(
                            timedelta(hours=24),
                            reason=f"O membro {member.display_name} recebeu"
                                   f" {contagem_avisos} e recebeu uma punição "
                                   f"mais severa de 24 horas",
                        )
                        await member.send(
                            f"⚠️ Você recebeu uma punição do servidor 😈 EDP 😈"
                            f"\n\n__Motivo:__  **{reason}**  \n\n__Punição:__  "
                            f"**[Mute : 24 horas || Esse é o seu {contagem_avisos}º "
                            f"Aviso]**\n\nReceber múltiplas punições pode acarretar "
                            f"em mute eterno ou banimento!\n\nO que fazer agora?"
                            f"\nQueremos ajudar você a continuar no servidor. Para"
                            f" isso, é importante:\n> 1. Conhecer as "
                            f"<#982810991194689546> da Elite e não violá-las;\n> 2."
                            f" Apelar a punição em https://discord.gg/4sdVrdVjbr caso "
                            f"acredite que cometemos um erro."
                        )
                    elif contagem_avisos >= 12:
                        await canal_punicoes.send(
                            f"**O membro {member.mention} recebeu um aviso aplicado por "
                            f"{interaction.user.mention} e como ele tem {contagem_avisos}"
                            f" avisos o meliante foi contemplado com um banimento!**"
                            f"*Os avisos de {member.mention} foram zerados "
                            f"devido ao __banimento__*"
                        )
                        await remover_aviso(member, 12)
                        await member.send(
                            f"⚠️ Você recebeu uma punição do servidor 😈 EDP 😈"
                            f"\n\n__Motivo:__  **{reason}**  \n\n__Punição:__  "
                            f"**[Banimento]**\n\nO que fazer agora?"
                            f" 1. Apelar a punição em https://discord.gg/4sdVrdVjbr caso "
                            f" acredite que cometemos um erro.\n 2. Aguardar até o Natal para poder"
                            f" entrar novamente em https://discord.gg/edp2"
                        )
                        await member.ban()
                    await interaction.followup.send(
                        f"Aviso enviado para **{member.display_name}**: {reason}",
                        ephemeral=True,
                    )

                elif punicao == "ban":
                    await canal_punicoes.send(
                        f"O membro **{member.mention}** recebeu uma punição do "
                        f"servidor 😈 EDP 😈 aplicada por {interaction.user.mention}"
                        f"\n\n__Motivo:__  **{reason}**\n\n__Punição:__  "
                        f"**[{self.punicao.capitalize()}]**"
                    )
                    await interaction.followup.send(
                        f"Aviso enviado para **{member.display_name}**: "
                        f"{reason}\n\n*Banimento aplicado*",
                        ephemeral=True,
                    )
                    await member.send(
                        f"⚠️ Você recebeu uma punição do servidor 😈 EDP 😈"
                        f"\n\n__Motivo:__  **{reason}**  \n\n__Punição:__  "
                        f"**[{self.punicao.capitalize()}]**\n\nO que fazer agora?"
                        f" 1. Apelar a punição em https://discord.gg/4sdVrdVjbr caso"
                        f" acredite que cometemos um erro.\n 2. Aguardar até o Natal para poder"
                        f" entrar novamente em https://discord.gg/edp2"
                    )
                    await member.ban()
                elif punicao == "mute":
                    if contagem_mutes == 3:
                        await canal_punicoes.send(
                            f"**O membro {member.mention} recebeu {contagem_mutes}"
                            f" e foi contemplado com um banimento!"
                            f" aplicado por {interaction.user.mention}**"
                        )
                        await interaction.followup.send(
                            f"Aviso enviado para **{member.display_name}**: "
                            f"{reason}\n\n*Banimento aplicado*\n\n*",
                            ephemeral=True,
                        )
                        await member.send(
                            f"⚠️ Você recebeu uma punição do servidor 😈 EDP 😈"
                            f"\n\n__Motivo:__  **{reason}**  \n\n__Punição:__  "
                            f"**[Banido]**\n\nO que fazer agora?\n"
                            f" 1. Apelar a punição em https://discord.gg/4sdVrdVjbr caso"
                            f" acredite que cometemos um erro.\n 2. Aguardar até o Natal para poder"
                            f" entrar novamente em https://discord.gg/edp2"
                        )
                        await remover_mute(member, 3)
                        await member.ban()
                    else:
                        await member.timeout(duracao, reason=reason)
                        await interaction.followup.send(
                            f"Aviso enviado para **{member.display_name}**: "
                            f"{reason}\n\n*Mute aplicado*",
                            ephemeral=True,
                        )
                        await canal_punicoes.send(
                            f"O membro **{member.mention}** recebeu uma punição do "
                            f"servidor 😈 EDP 😈 aplicada por {interaction.user.mention}"
                            f"\n\n__Motivo:__  **{reason}**\n\n__Punição:__  "
                            f"**[{self.punicao.capitalize()}] : {self.tempo} minutos"
                            f"\n\n**O membro {member.mention} já tem {contagem_avisos}"
                            f" Avisos e {contagem_mutes} Mutes"
                        )
                        await member.send(
                            f"⚠️ Você recebeu uma punição do servidor 😈 EDP 😈"
                            f"\n\n__Motivo:__  **{reason}**  \n\n__Punição:__  "
                            f"**[{punicao.capitalize()} : {self.tempo} minutos || "
                            f"Esse é o seu {mutes}º Mute]**\n\nReceber múltiplas "
                            f"punições pode acarretar em mute eterno ou banimento!"
                            f"\n\nO que fazer agora?\nQueremos ajudar você a "
                            f"continuar no servidor. Para isso, é importante:\n> 1. "
                            f"Conhecer as <#982810991194689546> da Elite e não "
                            f"violá-las;\n> 2. Apelar a punição em "
                            f"https://discord.gg/4sdVrdVjbr caso acredite que cometemos"
                            f" um erro."
                        )
            else:
                await interaction.followup.send("Membro não encontrado",
                                                ephemeral=True)
        else:
            await interaction.followup.send(
                f"{interaction.user.display_name} Você não tem permissão para "
                f"usar este Menu, somente o Moderador {author_member.display_name}"
                f" pode fazer isso!",
                ephemeral=True,
            )


class PunicoesView(discord.ui.View):
    def __init__(self, punicao: str, membro: discord.User, tempo_mute: int,
                 interacao):
        super().__init__(timeout=None)
        self.add_item(
            Punicoes(
                punicao=punicao,
                membro=membro,
                tempo_mute=tempo_mute,
                id_user_interaction=interacao,
            )
        )


@client.command(name="mod")
@commands.has_permissions(ban_members=True)
async def _punicao(ctx, punicao: str, member: discord.User, mute: int = None):
    id_author = ctx.author.id
    if mute is None:
        mute = 40320
    await novo_usuario(member)
    await adicionar_chaves(member)
    if punicao == "ban":
        await ctx.send(
            f"Selecione um motivo para aplicar o **banimento em "
            f"{member.display_name}.**\n*Essa mensagem será apagada "
            f"automaticamente em 30 segundos*",
            view=PunicoesView(
                punicao=punicao, membro=member, tempo_mute=mute,
                interacao=id_author
            ),
            delete_after=30,
        )
        await asyncio.sleep(5)
        await ctx.message.delete()

    elif punicao == "mute":
        await adicionar_mute(member)
        await ctx.send(
            f"Selecione um motivo para aplicar o **mute de {mute} minutos em "
            f"{member.display_name}.**\n*Essa mensagem será apagada "
            f"automaticamente em 30 segundos*",
            view=PunicoesView(
                punicao=punicao, membro=member, tempo_mute=mute,
                interacao=id_author
            ),
            delete_after=30,
        )
        await asyncio.sleep(5)
        await ctx.message.delete()

    elif punicao == "aviso":
        await adicionar_aviso(member)
        await ctx.send(
            f"Selecione um motivo para aplicar **um aviso para "
            f"{member.display_name}.**\n*Essa mensagem será apagada "
            f"automaticamente em 30 segundos*",
            view=PunicoesView(
                punicao=punicao, membro=member, tempo_mute=mute,
                interacao=id_author
            ),
            delete_after=30,
        )
        await asyncio.sleep(5)
        await ctx.message.delete()
    else:
        await novo_usuario(member)
        await adicionar_chaves(member)

        if punicao == "ban":
            await ctx.send(
                f"Selecione um motivo para aplicar o **banimento em "
                f"{member.display_name}.**\n*Essa mensagem será apagada "
                f"automaticamente em 30 segundos*",
                view=PunicoesView(
                    punicao=punicao, membro=member, tempo_mute=mute,
                    interacao=id_author
                ),
                delete_after=30,
            )
            await asyncio.sleep(5)
            await ctx.message.delete()

        elif punicao == "mute":
            await adicionar_mute(member)
            await ctx.send(
                f"Selecione um motivo para aplicar o **mute de {mute} "
                f"minutos em {member.display_name}.**\n*Essa mensagem será"
                f" apagada automaticamente em 30 segundos*",
                view=PunicoesView(
                    punicao=punicao, membro=member, tempo_mute=mute,
                    interacao=id_author
                ),
                delete_after=30,
            )
            await asyncio.sleep(5)
            await ctx.message.delete()

        elif punicao == "aviso":
            await adicionar_aviso(member)
            await ctx.send(
                f"Selecione um motivo para aplicar um **aviso para "
                f"{member.display_name}.**\n*Essa mensagem será apagada "
                f"automaticamente em 30 segundos*",
                view=PunicoesView(
                    punicao=punicao, membro=member, tempo_mute=mute,
                    interacao=id_author
                ),
                delete_after=30,
            )
            await asyncio.sleep(5)
            await ctx.message.delete()


@_punicao.error
async def _punicao_error(ctx, error):
    canal = client.get_channel(983234083918344222)
    if isinstance(error, commands.MissingPermissions):
        await canal.send(
            f"{ctx.author.mention} Olá pessoa, parece que você não tem "
            "privilégios suficientes para executar esse comando 😞"
        )
    elif isinstance(error, commands.UserNotFound):
        await canal.send(
            f"{ctx.author.mention} Olá pessoa, parece que o usuário não foi "
            "encontrado 😞"
        )


@client.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int):
    canal = client.get_channel(983234083918344222)
    try:
        user = await client.fetch_user(user_id)
        await ctx.guild.unban(user, reason=None)
        embed_user = discord.Embed(
            title="Membro desbanido!",
            description=f"{user_id} já pode entrar novamente no servidor!",
            color=0x00FF00,
        )
        await canal.send(embed=embed_user)
    except discord.NotFound:
        embed = discord.Embed(
            title="Erro",
            description=f"O id do usuário {user_id} não foi encontrado.",
            color=0xFF0000,
        )
        await canal.send(embed=embed)


@unban.error
async def _unban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        canal = client.get_channel(983234083918344222)
        await canal.send(
            f"{ctx.author.mention} Certifique-se de fornecer " f"um `ID` **válido**"
        )


@client.command(name="unmute")
@commands.has_permissions(ban_members=True)
async def _unmute(ctx, member: discord.Member):
    mutado = member.is_timed_out()
    canal = client.get_channel(983234083918344222)

    if mutado:
        await member.edit(timed_out_until=None)
        await asyncio.sleep(1)
        await canal.send(
            f"**A punição mute foi removida de {member.display_name}**")
        await member.send("Sua punição de **mute** foi removida!")
    else:
        await canal.send(
            f"Oppss! parece que o {member.display_name} não está mutado!")


@_unmute.error
async def _unmute_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        canal = client.get_channel(983234083918344222)
        await canal.send(
            f"{ctx.author.mention} Certifique-se de mencionar " f"um membro válido"
        )


@client.command(name="removeravisos")
@commands.has_permissions(ban_members=True)
async def _removeravisos(ctx, member: discord.Member, quantidade: int = None):
    avisos = await checar_avisos(member)
    canal = client.get_channel(983234083918344222)

    if quantidade is None or quantidade > avisos:
        await canal.send(
            f"{ctx.author.mention} Por favor insira quantos avisos deseja"
            f" remover de {member.display_name}\n\n"
            f"Atualmente o membro possui `{avisos}` **Aviso(s)**"
        )
    if avisos > 0 and quantidade <= avisos:
        await remover_aviso(member, quantidade)
        await member.send(f"Você teve **{quantidade} aviso(s)** removido(s)!")
        await canal.send(
            f"**{quantidade} aviso(s)** removido(s) de " f"{member.display_name}"
        )
    else:
        return


@_removeravisos.error
async def _removeravisos_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        canal = client.get_channel(983234083918344222)
        await canal.send(
            f"{ctx.author.mention} Certifique-se de mencionar " f"um membro válido"
        )


@client.command(name="removermutes")
@commands.has_permissions(ban_members=True)
async def _removermutes(ctx, member: discord.Member, quantidade: int = None):
    canal = client.get_channel(983234083918344222)
    mutes = await checar_mutes(member)

    if quantidade is None or quantidade > mutes:
        await canal.send(
            f"{ctx.author.mention} Por favor insira quantos mutes deseja"
            f" remover de {member.display_name}\n\n"
            f"Atualmente o membro possui `{mutes}` **Mute(s)**"
        )

    if mutes > 0 and quantidade <= mutes:
        await remover_mute(member, quantidade)
        await member.send(f"Você teve **{quantidade} mute(s)** removido(s)!")
        await canal.send(
            f"**{quantidade} mute(s)** removido de " f"{member.display_name}"
        )


@_removermutes.error
async def _removermutes_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        canal = client.get_channel(983234083918344222)
        await canal.send(
            f"{ctx.author.mention} Certifique-se de mencionar " f"um membro válido"
        )


@client.command(name="av")
async def __avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(
        title=f"Avatar de {member.display_name} 😎",
        color=0xFF0703,
    )
    embed.set_image(url=member.avatar.url)
    embed.set_footer(
        text=f"🕵️‍♂️ Após uma investigação profunda, descobri que\n "
             f"{member.display_name} é esse coiso acima.\nVamos "
             f"{ctx.author}, não se misture com essa gentalha!"
    )

    await ctx.send(embed=embed)


@client.command(name="bot_avatar")
@commands.has_guild_permissions(administrator=True)
async def addavatar(ctx: commands.Context, attachment: discord.Attachment):
    data = await attachment.read()
    await client.user.edit(avatar=data)
    await ctx.send(f"Avatar atualizado\nenviado por {ctx.author.mention}!")


@addavatar.error
async def addavatar(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Parece que você não tem permissões suficientes!")
    elif isinstance(error, commands.MissingRequiredAttachment):
        await ctx.send(
            f"Olá {ctx.author.mention}, por favor envie o avatar "
            f"que deseja usar!"
        )


@client.command(name='clear')
@commands.has_guild_permissions(manage_messages=True)
async def _purgemsg(ctx, value: commands.Range[int, 2, 1000]):
    gmt = pytz.timezone('America/Sao_Paulo')
    now = datetime.datetime.now(tz=gmt)
    log_channel = client.get_channel(983234083918344222)

    fourteendays = now - timedelta(days=14)

    messages = [message async for message in
                ctx.channel.history(limit=value,
                                    after=fourteendays,
                                    oldest_first=False)
                ]

    messages_ignored = [message async for message in
                        ctx.channel.history(limit=value,
                                            before=now,
                                            oldest_first=False)
                        ]

    await ctx.channel.delete_messages(messages)

    result = len(messages_ignored) - len(messages)
    msg = (
              f'**✅ Foram apagadas {len(messages)} mensagem(s).**\n\n'
              if len(messages) > 0 else ''
          ) + (
              f'**{result} mensagem(s)** não foram apagadas devido a '
              f'limitações do Discord\n`mais antigas que 14 dias`\n'
              if result != 0 else ''
          )

    embed = discord.Embed(description=f'{msg}Clear feito em <#{ctx.channel.id}>'
                                      f' por: {ctx.author.mention}')

    await log_channel.send(embed=embed,
                   allowed_mentions=discord.AllowedMentions(users=False)
                   )


@_purgemsg.error
async def msg_error(ctx, error):
    if isinstance(error, commands.RangeError):
        await ctx.send(f'Olá {ctx.author.mention} insira um numero de '
                       f'mensagens válido para apagar `2 a 1000`')
    elif isinstance(error, commands.MissingPermissions):
        return


client.run(os.getenv("TOKEN_BOT"))
