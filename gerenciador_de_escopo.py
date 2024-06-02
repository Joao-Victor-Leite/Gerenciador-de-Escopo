from menu import menu
import funcoes as f

diretorio = './tests/'
arquivo_caminho = menu(diretorio)

arquivo_conteudo = []
pilha = []
tabela_simbolos = {}

arquivo_conteudo = f.guardar_arquivo(arquivo_caminho, arquivo_conteudo)

for elemento in arquivo_conteudo:
    if elemento.startswith("BLOCO"):
        partes = elemento.split("_", 1)
        if len(partes) > 1:
            nome_bloco = "_" + partes[1]
            pilha.append(nome_bloco)
            tabela_simbolos = {}
            pilha.append(tabela_simbolos)

    elif elemento.startswith("FIM"):
        partes = elemento.split("_", 1)
        if len(partes) > 1:
            nome_bloco = "_" + partes[1]
            while nome_bloco in pilha:
                pilha.pop()
    
    elif elemento.startswith("NUMERO"):
        if "=" not in elemento:
            var_nome = elemento[6:]
            f.declarar_variavel_tabela(tabela_simbolos, var_nome, "NUMERO")
        else:
            if "," in elemento:
                partes = elemento[6:].split(',')
                for parte in partes:
                    if "=" in parte:
                        var_nome, var_valor = parte.split('=')
                        f.declarar_variavel_tabela(tabela_simbolos, var_nome, "NUMERO")
                        f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
                    else:
                        var_nome = parte
                        f.declarar_variavel_tabela(tabela_simbolos, var_nome, "NUMERO")
            else:
                var_nome, var_valor = elemento[6:].split('=', 1)
                f.declarar_variavel_tabela(tabela_simbolos, var_nome, "NUMERO")
                f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
    
    elif elemento.startswith("CADEIA"):
        if "=" not in elemento:
            var_nome = elemento[6:]
            f.declarar_variavel_tabela(tabela_simbolos, var_nome, "CADEIA")
        else:
            if "," in elemento:
                partes = elemento[6:].split(',')
                for parte in partes:
                    if "=" in parte:
                        var_nome, var_valor = parte.split('=')
                        f.declarar_variavel_tabela(tabela_simbolos, var_nome, "CADEIA")
                        f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
            else:
                var_nome, var_valor = elemento[6:].split('=', 1)
                f.declarar_variavel_tabela(tabela_simbolos, var_nome, "CADEIA")
                f.atribuir_valor_variavel(tabela_simbolos, var_nome, var_valor)
    
    elif elemento.startswith("PRINT"):
        var_nome = elemento[5:]
        if f.procurar_variavel_em_pilha(pilha, var_nome):
            var_valor = f.procurar_valor_variavel_em_pilha(pilha, var_nome)
            if var_valor or var_valor == 0:
                print(var_valor)
        else:
            print(f"ERRO: Variavel {var_nome} nao declarada")

    elif "=" in elemento:
        var_destino, var_origem = elemento.split('=')
        if f.procurar_variavel_em_pilha(pilha, var_destino):
            if f.procurar_tipo_variavel_em_pilha(pilha, var_destino) == "CADEIA" and var_origem.startswith('"') and var_origem.endswith('"'):
                f.declarar_variavel_tabela(tabela_simbolos, var_destino, "CADEIA")
                f.atribuir_valor_variavel(tabela_simbolos, var_destino, var_origem)
            elif f.procurar_tipo_variavel_em_pilha(pilha, var_destino) == "NUMERO" and f.e_numero(var_origem):
                f.declarar_variavel_tabela(tabela_simbolos, var_destino, "NUMERO")
                f.atribuir_valor_variavel(tabela_simbolos, var_destino, var_origem)
            else:
                if f.procurar_variavel_em_pilha(pilha, var_origem):
                    tipo_var_origem = f.procurar_tipo_variavel_em_pilha(pilha, var_origem)
                    tipo_var_destino = f.procurar_tipo_variavel_em_pilha(pilha, var_destino)
                    if tipo_var_origem == tipo_var_destino:
                        valor_var_origem = f.procurar_valor_variavel_em_pilha(pilha, var_origem)
                        f.atribuir_valor_variavel(tabela_simbolos, var_destino, valor_var_origem)
                    else:
                        print(f"ERRO: Tipos incompatíveis - {tipo_var_origem} e {tipo_var_destino}")