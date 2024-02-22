import pymongo
from dotenv import load_dotenv
import os
from datetime import datetime
import pytz

load_dotenv()

cliente = pymongo.MongoClient(os.getenv('MONGODB'))
bancodedados = cliente['economia']
usuarios = bancodedados['usuarios']


async def novo_usuario(usuario):
    filtro = {'discord_id': usuario.id}
    if usuarios.count_documents(filtro) == 0:
        objeto = {
            'discord_id': usuario.id,
            'moedas': 0,
            'cooldown': 0,
            'vitorias': 0,
            'timestamp': '',
        }
        usuarios.insert_one(objeto)
        await adicionar_chaves(usuario)
        return objeto
    else:
        await adicionar_chaves(usuario)
        return False


async def checar_saldo(usuario):
    await novo_usuario(usuario)
    filtro = {'discord_id': usuario.id}
    resultado = usuarios.find(filtro)
    return resultado.__getitem__(0)['moedas']


async def checar_vips(usuario):
    await novo_usuario(usuario)
    if usuario is None:
        return 0
    filtro = {'discord_id': usuario.id}
    resultado = usuarios.find(filtro)
    if 'vitorias' in resultado.__getitem__(0):
        return resultado.__getitem__(0)['vitorias']
    else:
        return 0


async def checar_vips2(usuario):
    filtro = {'discord_id': usuario.id}
    resultado = usuarios.find(filtro)
    if 'vitorias' in resultado[0] and resultado[0]['vitorias'] > 0:
        return True
    else:
        return False


async def add_vip(usuario, quantidade):
    await novo_usuario(usuario)
    vips_atuais = await checar_vips(usuario)
    filtro = {'discord_id': usuario.id}
    relacao = {'$set':{'vitorias': vips_atuais+quantidade}}

    usuarios.update_one(filtro,relacao)


async def remove_vip(usuario, quantidade):
    await novo_usuario(usuario)
    vips_atuais = await checar_vips(usuario)
    if vips_atuais < quantidade:
        return
    filtro = {'discord_id': usuario.id}
    relacao = {'$set':{'vitorias': vips_atuais-quantidade}}

    usuarios.update_one(filtro,relacao)


async def alterar_saldo(usuario, quantidade):
    await novo_usuario(usuario)
    moedas_atuais = await checar_saldo(usuario)
    filtro = {'discord_id': usuario.id}
    relacao = {'$set':{'moedas': moedas_atuais+quantidade}}

    usuarios.update_one(filtro,relacao)


async def add_cooldown(usuario):
    filtro = {'discord_id': usuario.id}
    gmt = pytz.timezone('America/Sao_Paulo')
    usuarios.update_one(filtro, {'$set': {'cooldown': int(datetime.now(gmt).timestamp() * 1000)}})
    usuarios.update_one(filtro, {'$set': {'timestamp': datetime.now(gmt).time().strftime('%H:%M')}})


async def checar_cooldown(usuario):
    await novo_usuario(usuario)
    filtro = {'discord_id': usuario.id}
    resultado = usuarios.find(filtro)
    gmt = pytz.timezone('America/Sao_Paulo')

    if resultado and 'timestamp' in resultado[0]:
        ultimo_uso = resultado[0]['cooldown']
        timestamp = resultado[0]['timestamp']
        tempo_atual = int(datetime.now(gmt).timestamp() * 1000)
        diferenca_tempo = tempo_atual - ultimo_uso
        tempo_de_cooldown = 24 * 60 * 60 * 1000
        horas_restantes = tempo_de_cooldown - diferenca_tempo

        if diferenca_tempo < tempo_de_cooldown:
            tempo_em_horas = int(horas_restantes / (1000 * 60 * 60))
            if tempo_em_horas >= 1:
                restando = f'{tempo_em_horas:02d} horas'
                return True, restando, timestamp
            else:
                minutos_restantes = int(horas_restantes / (1000 * 60))
                restando = f'{minutos_restantes:02d} minutos'
                return True, restando, timestamp
        else:
            print('Cooldown expirado')
            return False, 0, ''


async def incrementar_vitorias(usuario):
    filtro = {'discord_id': usuario.id}
    atualizacao = {'$inc': {'vitorias': 1}}
    usuarios.update_one(filtro, atualizacao)


async def decrementar_vitorias(usuario):
    filtro = {'discord_id': usuario.id}
    resultado = usuarios.find(filtro)
    if 'vitorias' in resultado[0] and resultado[0]['vitorias'] > 0:
        atualizacao = {'$inc': {'vitorias': -1}}
        usuarios.update_one(filtro, atualizacao)
    else:
        return


async def adicionar_chaves(usuario):
    filtro = {'discord_id': usuario.id}
    resultado = list(usuarios.find(filtro))

    if len(resultado) > 0:
        usuario_atual = resultado[0]

        if 'contagem_de_mute' not in usuario_atual:
            usuarios.update_one(filtro, {'$set': {'contagem_de_mute': 0}})

        if 'contagem_de_avisos' not in usuario_atual:
            usuarios.update_one(filtro, {'$set': {'contagem_de_avisos': 0}})


async def adicionar_aviso(usuario):
    filtro = {'discord_id': usuario.id}
    usuarios.update_one(filtro, {'$inc': {'contagem_de_avisos': 1}})


async def remover_aviso(usuario, quantidade:int):
    filtro = {'discord_id': usuario.id}
    usuarios.update_one(filtro, {'$inc': {'contagem_de_avisos': - quantidade}})


async def adicionar_mute(usuario):
    filtro = {'discord_id': usuario.id}
    usuarios.update_one(filtro, {'$inc': {'contagem_de_mute': 1}})


async def remover_mute(usuario, quantidade:int):
    filtro = {'discord_id': usuario.id}
    usuarios.update_one(filtro, {'$inc': {'contagem_de_mute': - quantidade}})


async def checar_mutes(usuario):
    await novo_usuario(usuario)
    filtro = {'discord_id': usuario.id}
    resultado = usuarios.find(filtro)
    return resultado.__getitem__(0)['contagem_de_mute']


async def checar_avisos(usuario):
    await novo_usuario(usuario)
    filtro = {'discord_id': usuario.id}
    resultado = usuarios.find(filtro)
    return resultado.__getitem__(0)['contagem_de_avisos']
