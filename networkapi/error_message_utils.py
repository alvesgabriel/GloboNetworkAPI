# -*- coding:utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from networkapi.infrastructure import xml_utils

error_messages = {
    1: u'Falha ao acessar a fonte de dados',
    2: u'Falha ao executar o script. Causa: %s',
    3: u'Falha ao executar a leitura do XML de requisição. Causa: %s',
    4: u'Falha ao gerar o XML de resposta. Causa: %s',
    100: u'Tipo de equipamento não cadastrado',
    101: u'Model of equipment not registered',
    102: u'Group of equipment not registered',
    103: u'Identificador do tipo de equipamento é obrigatório',
    104: u'Identificador do modelo do equipamento é obrigatório',
    105: u'Nome do equipamento é obrigatório',
    106: u'Identificador do grupo do equipamento é obrigatório',
    107: u'Equipamento do grupo “Equipamentos Orquestração” somente poderá ser criado com tipo igual a “Servidor Virtual"',
    108: u'the VLAN name duplicated within an environment informed',
    109: u'Não existe número de VLAN disponível nos intervalos de %d até %d e de %d até %d para o ambiente informado',
    110: u'Ambiente com Divisão DC diferente de BE e FE',
    111: u'Type of network not registered',
    112: u'Environment not registered',
    113: u'O nome da VLAN é obrigatório',
    114: u'O identificador do ambiente é obrigatório',
    115: u'O identificador da VLAN é obrigatório',
    116: u'VLAN not registered',
    117: u'Equipment %s not registered',
    118: u'IP %s not registered for the equipment %s',
    119: u'IP not registered',
    120: u'IP already registered for the equipment',
    121: u'VLAN não validada',
    122: u'VLAN já ativada',
    123: u'The identifier of the IP is required',
    124: u'Healthcheck_expect não cadastrado',
    125: u'Invalid value of the finality',
    126: u'Invalid value of the client',
    127: u'Invalid value of the environment',
    128: u'Invalid value of the cache',
    129: u'Invalid value of the method_bal',
    130: u'Formato do valor do transbordo %s inválido',
    131: u'Valor do método de balanceamento inválido',
    132: u'Invalid value of the persistence',
    133: u'Valor do tipo do healthcheck inválido ou inconsistente em relação ao valor do healthcheck_expect',
    134: u'Valor do healthcheck inconsistente em relação ao valor do tipo do healthcheck',
    135: u'Invalid value of the timeout',
    136: u'Invalid value of the host',
    137: u'Invalid value of the maximum number of connections',
    138: u'Valor da variável porta_servico %s inválido',
    139: u'Não existe ligação no front cadastrada para a interface do equipamento',
    140: u'O sufixo do reals_name é obrigatório para criar ou alterar o vip %s do grupo virtual',
    141: u'Interface não cadastrada',
    142: u'Interface não está relacionada com o host',
    143: u'Interface do switch está com o campo protegida setado',
    144: u'A ligação no front da interface não tem nenhuma interface que representa um switch',
    145: u'O nome da interface é obrigatório',
    146: u'Equipamento já está cadastrado no grupo',
    147: u'O identificador do equipamento é obrigatório',
    148: u'Existe mais de um equipamento com o mesmo nome',
    149: u'Equipamento com nome duplicado',
    150: u'%s',
    151: u'Valor do real %s inválido',
    152: u'Request VIP is not registered.',
    153: u'IP %s.%s.%s.%s not registered for the environment %s',
    154: u'O valor da indicação de ativo do usuário é inválido',
    156: u'Equipamento %s já está cadastrado no ambiente %s',
    157: u'Equipamento %s não está cadastrado para o ambiente %s',
    158: u'Tipo de roteiro %s não cadastrado',
    159: u'O identificador do grupo layer 3 é obrigatório',
    160: u'Grupo layer 3 %s não cadastrado',
    161: u'O identificador do ambiente lógico é obrigatório',
    162: u'Ambiente lógico %s não cadastrado',
    163: u'O identificador da divisão DC é obrigatório',
    164: u'Divisão DC %s não cadastrada',
    165: u'Roteiro %s não cadastrado',
    166: u'O nome da marca é obrigatório',
    167: u'Marca %s não cadastrada',
    168: u'O nome do grupo layer 3 é obrigatório',
    169: u'Nome %s já cadastrado para outro grupo layer 3',
    170: u'O protocolo é obrigatório',
    171: u'Tipo de acesso %s não cadastrado',
    172: u'O nome do ambiente lógico é obrigatório',
    173: u'Nome %s já cadastrado para outro ambiente lógico',
    174: u'O nome da divisão DC é obrigatório',
    175: u'Nome %s já cadastrado para outra divisão DC',
    176: u'O nome do tipo de rede é obrigatório',
    177: u'User %s not registered',
    178: u'O user do usuário é obrigatório',
    179: u'User %s já está cadastrado para outro usuário',
    180: u'User Group %s not registered',
    181: u'Nome do grupo de usuário é obrigatório',
    182: u'Grupo de usuário com o nome %s já cadastrado',
    183: u'Usuário %s já está cadastrado no grupo %s',
    184: u'Usuário %s não pertence ao grupo %s',
    185: u'Equipamento %s não pertence ao grupo %s',
    186: u'The IP of the request VIP %s could not be changed because the VIP is already created',
    187: u'Interface com o nome %s já cadastrada para o equipamento %s',
    188: u'Interface %s não está associada ao equipamento %s',
    189: u'Permissão administrativa %s não cadastrada',
    190: u'Roteiro %s não associado ao equipamento %s',
    191: u'Requisição de VIP %s não validada',
    192: u'Requisição de VIP %s já criada',
    193: u'Tipo de roteiro com nome %s já cadastrado',
    194: u'O identificador do tipo de roteiro é obrigatório',
    195: u'O nome do roteiro é obrigatório',
    196: u'O tipo de roteiro %s não pôde ser excluído porque tem roteiro associado',
    197: u'O roteiro %s não pôde ser excluído porque tem equipamento associado',
    198: u'Roteiro %s já está associado ao equipamento %s',
    199: u'A marca %s não pôde ser excluída porque tem modelo associado',
    200: u'O nome do modelo é obrigatório',
    201: u'O identificador da marca é obrigatório',
    202: u'O modelo %s não pôde ser excluído porque tem equipamento associado',
    203: u'Tipo de acesso com o protocolo %s já cadastrado',
    204: u'O tipo de acesso %s não pôde ser excluído porque tem equipamento associado',
    205: u'The fqdn is required',
    206: u'The user is required',
    207: u'The password is required',
    208: u'O identificador do tipo de acesso é obrigatório',
    209: u'Equipamento %s não está associado ao tipo de acesso %s',
    210: u'O valor da indicação de protegida da interface é obrigatório',
    211: u'O valor da indicação de protegida da interface é inválido',
    212: u'Interface da ligação front não cadastrada',
    213: u'Interface da ligação back não cadastrada',
    214: u'Interface %s não pôde ser excluída porque tem outra interface associada',
    215: u'Tipo de rede %s não pôde ser excluído porque tem rede associada',
    216: u'Divisão DC %s não pôde ser excluída porque tem ambiente associado',
    217: u'Ambiente lógico %s não pôde ser excluído porque tem ambiente associado',
    218: u'Grupo layer 3 %s não pôde ser excluído porque tem ambiente associado',
    219: u'Ambiente com o mesmo grupo layer 3, ambiente lógico e divisão DC já cadastrado',
    220: u'Ambiente %s não pôde ser excluído porque tem vlan ou equipamento associado',
    221: u'O nome do usuário é obrigatório',
    222: u'O e-mail do usuário é obrigatório',
    223: u'O valor da indicação de ativo do usuário é obrigatório',
    224: u'O usuário %s não pôde ser excluído porque tem event_log ou grupo associado',
    225: u'A indicação de leitura do grupo do usuário é obrigatória',
    226: u'A indicação de escrita do grupo do usuário é obrigatória',
    227: u'A indicação de edição do grupo do usuário é obrigatória',
    228: u'A indicação de exclusão do grupo do usuário é obrigatória',
    229: u'O valor da indicação de leitura do grupo do usuário é inválido',
    230: u'O valor da indicação de escrita do grupo do usuário é inválido',
    231: u'O valor da indicação de edição do grupo do usuário é inválido',
    232: u'O valor da indicação de exclusão do grupo do usuário é inválido',
    233: u'O identificador do roteiro é obrigatório',
    234: u'O identificador do usuário é obrigatório',
    235: u'O identificador do grupo de usuário é obrigatório',
    236: u'O nome do grupo de equipamento é obrigatório',
    237: u'A função da permissão administrativa é obrigatória',
    238: u'A indicação de leitura da permissão administrativa é obrigatória',
    239: u'A indicação de escrita da permissão administrativa é obrigatória',
    240: u'O valor da indicação de leitura da permissão administrativa é inválido',
    241: u'O valor da indicação de escrita da permissão administrativa é inválido',
    242: u'Equipamento %s já está associado ao tipo de acesso %s',
    243: u'O identificador da requisição de VIP é obrigatório',
    244: u'O valor da indicação de validado da requisição de VIP é inválido',
    245: u'O valor da indicação de vip_criado da requisição de VIP é inválido',
    246: u'A indicação de validado da requisição de VIP é obrigatória',
    247: u'A indicação de vip_criado da requisição de VIP é obrigatória',
    248: u'O identificador da permissão administrativa é obrigatório',
    249: u'O nome do tipo de roteiro é obrigatório',
    250: u'Roteiro com o nome %s e tipo de roteiro %s já cadastrado',
    251: u'Marca com o nome %s já cadastrada',
    252: u'Modelo com o nome %s e a marca %s já cadastrado',
    253: u'Tipo de rede com o nome %s já cadastrado',
    254: u'Grupo de equipamento com o nome %s já cadastrado',
    255: u'O identificador da interface é obrigatório',
    256: u'O identificador do tipo de rede é obrigatório',
    257: u'Permissão administrativa com grupo de usuário %s e função %s já cadastrada',
    258: u'Rights Group Equipment %s not registered',
    259: u'A indicação de leitura do direito grupo equipamento é obrigatória',
    260: u'A indicação de escrita do direito grupo equipamento é obrigatória',
    261: u'A indicação de alterar_config do direito grupo equipamento é obrigatória',
    262: u'A indicação de exclusão do direito grupo equipamento é obrigatória',
    263: u'O valor da indicação de leitura do direito grupo equipamento é inválido',
    264: u'O valor da indicação de escrita do direito grupo equipamento é inválido',
    265: u'O valor da indicação de alterar_config do direito grupo equipamento é inválido',
    266: u'O valor da indicação de exclusão do direito grupo equipamento é inválido',
    267: u'Direitos Grupo Equipamento com o grupo de usuário %s e o grupo de equipamento %s já cadastrado',
    268: u'O identificador dos direitos grupo equipamento é obrigatório',
    269: u'Parameter %s is invalid. Value: %s',
    270: u'The VIP %s could not be changed because the VIP has not been created',
    271: u'Groups of equipment registered with the IP of the VIP request is not allowed of acess.',
    272: u'List the Reals_priority  is higher or lower than list the real_server.',
    273: u'Lock wait timeout exceeded; try restarting transaction.',
    274: u'List the Reals_weight  is higher or lower than list the real_server.',
    275: u'The healthcheck_type parameter not exist.',
    276: u'The healthcheck_type parameter is not HTTP, then healthcheck and id_healthcheck_expect must be None.',
    277: u'The healthcheck_type parameter is HTTP, then healthcheck and id_healthcheck_expect must NOT be None.',
    278: u'List the ports  is higher or lower than list the real_server.',
    279: u'The VLAN name must be a string with a maximum of 50 characters and can not be empty.',
    280: u'The description of the VLAN must be a string with a maximum of 200 characters.',
    281: u'Network IPv4 is not registered.',
    282: u'The identifier RedeIPv4 is mandatory',
    283: u'Environment VIP not registered',
    284: u'There networkIPv4 associated with environment vip',
    285: u'There networkIPv6 associated with environment vip',
    286: u'Network IPv6 is not registered.',
    287: u'At least one of the parameters have to be informed to query',
    288: u'IP is not associated with the equipment',
    289: u'Option VIP is not registered.',
    290: u'Option vip is already associated with the environment vip',
    291: u'Option vip is not associated with the environment vip',
    292: u'IPv6 %s not registered for the environment %s',
    293: u'Vlan is currently in active/deployed state. It needs to be undeployed before deletion.',
    294: u'Invalid Environment Configuration or not registered',
    295: u'Unavailable address to create a NetworkIPv4',
    296: u'Unavailable address to create a NetworkIPv6',
    297: u'The Request VIP - IPv4 can not change to a Request VIP - IPv6',
    298: u'The Request VIP - IPv6 can not change to a Request VIP - IPv4',
    299: u'Network already activated',
    300: u'Invalid Request VIP IP version, try to use %s',
    301: u'IP Configuration is not registred.',
    302: u'Environment Configuration already exists',
    303: u'EquipmentAccess is not registred.',
    304: u'TypeAccess is not registred',
    305: u'Network %s don\'t have associate IPs',
    306: u'Vlan já cadastrada com o número %s',
    307: u'%s',
    308: u'Não existe associação de Ip e Equipamento para o IP %s',
    309: u'Failure to remove an association between an equipment and a group because the equipment is related only to one group.',
    310: u'Não foi possível excluir o grupo %s por alguns equipamentos estarem associados apenas a este grupo. Equipamentos: %s',
    311: u'Já existe uma Vlan com o arquivo_acl = %s',
    312: u'Tipo de Equipamento com nome %s, já cadastrado.',
    313: u'%s.',  # Healthcheck já cadastrado
    314: u'%s',  # Erro Vlan
    315: u'%s',  # Erro Vlan
    316: u'Não existe Ambiente VIP cadastrado com os valores fornecidos: finalidade - %s ,cliente - %s, ambiente - %s.',
    317: u'Ip não encontrado para equipamento %s e ambiente vip %s.',
    318: u'O Ip %s e o Equipamento %s, não estão associados.',
    319: u'There is a request VIP pointing to this %s, the %s id = %s can not be excluded.',
    320: u'There are equipment related Ips, which are not part of the Environment Ip.',
    321: u'Não há rede %s no ambiente vip fornecido.',
    322: u'Requisição de VIP %s não criada',
    323: u'Ambiente %s não pôde ser excluído pois a rede %s da vlan %s tem um ip associado com a requisição vip %s.',
    324: u'Ambiente %s não pôde ser excluído pois a vlan %s está ativa.',
    325: u'Invalid value of the priority.',
    # VipRequest Real server equipment error
    326: u'Não foi possível recuperar o equipamento %s associado a um real server.',
    # VipRequest Real server equipment ip association error
    327: u'Não foi possível recuperar o ip %s e equipamento %s associados ao real server.',
    # VipRequest Real server ip doesn't exist
    328: u'Não foi possível recuperar o IP %s associado ao real server %s.',
    329: u'Existe uma inconsistência de prioridade de real server no banco de dados.',
    330: u'Existe uma inconsistência de peso (weight) de real server no banco de dados.',
    331: u'Existe uma inconsistência de portas de real server no banco de dados.',
    332: u'Existe uma inconsistência na requisição vip, o parâmetro %s é inválido. Valor: %s.',
    # 333:u'Alteração de real server realizada com sucesso, mas ocorreram
    # erros de script com o(s) real(s) %s e ip(s) %s.',
    333: u'Alteração de real server concluída com falha, ocorreram erros de script com o(s) real(s) %s e ip(s) %s.',
    334: u'%s',
    335: u'Existe uma rede com mesma faixa relacionada com ambiente vip',
    336: u"Não foi possivel desassociar ambiente %s, pois existem ips sendo utilizados pelas requisições vip's. IPv4[ %s ] - IPV6[ %s ]",
    337: u'Valor do parâmetro %s inválido. Valor: %s.',
    338: u'Ocorreu um erro ao salvar o filtro no banco de dados. Verifique se o nome é único.',
    339: u'Não foi possível recuperar o filtro especificado do banco de dados.',
    340: u'Ocorreu um erro ao salvar o filtro editado no banco de dados.',
    341: u'Ocorreu um erro ao remover o filtro no banco de dados.',
    342: u'Não foi possível recuperar o tipo de equipamento especificado do banco de dados.',
    343: u'A associação entre o filtro %s e o tipo de equipamento %s já existe.',
    344: u'%s',
    345: u"Não foi possivel remover o equipamento %s, pois existem ips sendo utilizados por requisições vip's. IPv4[ %s ] - IPV6[ %s ]",
    346: u"Um dos equipamentos associados com o ambiente desta rede também está associado com outro ambiente que tem uma rede com essa mesma faixa, adicione filtros nos ambientes se necessário.",
    347: u"O equipamento que está sendo associado já possui um ip na mesma faixa em outra rede, se necessário adicione filtros nos ambientes.",
    348: u"O tipo de equipamento %s não pode ser desassociado do filtro %s.",
    349: u"O filtro %s não pode ser desassociado do ambiente pois está em uso.",
    350: u'Permissão %s não cadastrada.',
    351: u'Permissão Administrativa com função %s já cadastrada.',
    352: u"Não foi possível desassociar o ip %s do equipamento %s pois o ip está sendo utilizado na requisição vip %s e o equipamento é o único balanceador associado a este ip.",
    353: u'Valores duplicados para Porta Real, Porta Vip e IP do Real na mesma Requisição VIP.',
    354: u'Não foi possível excluir o ip de id %s pois ele está sendo usado em uma requisição VIP.',
    355: u'Não foi possível excluir a rede de id %s pois há um ip nela sendo usado em uma requisição VIP.',
    356: u'Não foi possível excluir a vlan de id %s pois há uma rede que possui um ip sendo usado em uma requisição VIP.',
    357: u'Esse ambiente já possui blocos cadastrados.',
    358: u'Regra inválida ou não cadastrada.',
    359: u'Bloco inválido ou não cadastrado.',
    360: u'Essa requisição vip não possui uma regra.',
    361: u'Esse bloco já está cadastrado na regra.',
    362: u'A regra relacionada a esse vip não possui blocos previamente cadastrados.',
    363: u'Não foi possível remover a rede pois ela está inativa.',
    364: u'Acl não foi criada',
    367: u'O ambiente desta Vlan já possui uma ACL com o nome = %s',
    368: u'Nao foi possivel remover a vlan pois ela esta inativa.',
    369: u'Nao foi possivel remover a vlan pois as seguintes redes nao puderam ser removidas: %s.',
    370: u'Nao foi possivel excluir o vip %s. Remova-o dos equipamentos primeiro.',
    371: u'Bloco não pode ser adicionado porque já existe uma regra para ser aplicada e o valor do parametro override é zero.',
    372: u'Server Pool Does Not Exists',
    373: u'Equipamento(s) do Server Pool: %s não pertence ao mesmo ambiente do Ambiente Vip: %s.',
    374: u'Está requisição vip não possui nenhum server pool cadastrado.',
    375: u'Pool can not be excluded because it is associated with a VIP',
    376: u'Numero de Rack %s ja existe.',
    377: u'Endereco MAC invalido',
    378: u'Rack nao pode ser incluido',
    379: u'Rack nao existe',
    380: u'Arquivo de configuracao do equipamento %s criado',
    381: u'Nome %s ja existe.',
    382: u'Os arquivos de configuracao do Rack %s nao podem ser gerados. %s',
    383: u'Nao foi possivel aplicar a configuracao do rack %s. %s',
    384: u'Erro ao editar ServerPool: %s',
    385: u'Não foi possível desassociar o ip %s do equipamento %s pois o ip está sendo utilizado nos server pools (id:identifier) %s.',
    386: u'Não foi possível excluir a rede %s pois o ip %s contido nela esta sendo usado nos Server Pools (id:identifier) %s.',
    387: u'Não foi possível excluir a vlan %s pois ela possui a rede %s e essa rede possui o ip %s contido nela, e esse ip esta sendo usado nos Server Pools (id:identifier) %s.',
    389: u'Não foi possível excluir o vip %s pois o ip %s do mesmo esta sendo usado nos Server Pools (id:identifier) %s.',
    390: u'Não foi possível excluir o vip %s pois os seguintes vips %s estão usando o mesmo ip %s.',
    391: u'Failure accessing Foreman server: %s',
    392: u'Environment is already associated with the environment vip',
    393: u'Environment is not associated with the environment vip',
    394: u'O ambiente %s não pode ser desvinculado pois existem server pools com reals vinculados a este ambiente.',
    396: u'A operação não pode ser realizada pois o ambiente "%s" do ip %s não possui permissão com um dos ambientes vips "%s".',
    397: u'O Rack, que o servidor está, não foi cadastrado.',
    400: u'Nao foi possivel adicionar o Rack',
    401: u'As mudancas nao foram salvas',
    405: u'Channel não pode ser criado. %s',
    406: u'Channel não pode ser editado. %s',
    407: u'Erro ao remover a variável.',
    410: u'Channel não pode ser deletado. %s',
    413: u'Interface não pode ser desconectada. Remova o Port Channel primeiro.',
    414: u'A rede a ser cadastrada não pertence a rede do ambiente. Cadastre o range desejado no ambiente',
    415: u'O ambiente não está configurado. É necessário efetuar a configuração.'
}


def error_dumps(code, *args):

    if isinstance(code, tuple):
        code = code[0]

    message = error_messages.get(code, '')
    if len(args) > 0:
        message = message % args

    error_map = dict()
    error_map['codigo'] = '%04d' % code
    error_map['descricao'] = message

    map = dict()
    map['erro'] = error_map

    return xml_utils.dumps_networkapi(map)


if __name__ == '__main__':
    print error_dumps(u'0001', u'Falha ao acessar a fonte de dados')
    print error_dumps(1)
    print error_dumps(3, 'Causa')
    print error_messages[99]
