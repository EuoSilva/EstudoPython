import csv
import os
from datetime import datetime
import random
from colorama import init, Fore, Style
init(autoreset=True)

arquivo_csv = "tarefas.csv"
tarefas = []
campos = ["tarefa", "concluida", "data_criacao", "prioridade", "prazo_entrega", "categoria"]

def carregar_tarefas():
    global tarefas
    tarefas.clear()
    if os.path.exists(arquivo_csv):
        with open(arquivo_csv, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                tarefas.append({
                    "tarefa": linha.get("tarefa", ""),
                    "concluida": linha.get("concluida", "False") == "True",
                    "data_criacao": linha.get("data_criacao", "N/A"),
                    "prioridade": linha.get("prioridade", "baixa"),
                    "prazo_entrega": linha.get("prazo_entrega", "Sem prazo"),
                    "categoria": linha.get("categoria", "geral")
                })

def tarefa_do_dia():
    pendentes = [t for t in tarefas if not t["concluida"]]
    if pendentes:
        t = random.choice(pendentes)
        print(f"\n✨ Sua tarefa do dia: {t['tarefa']} (Prioridade: {t['prioridade']})")

def mostrar_alerta_vencidas():
    vencidas = [
        t for t in tarefas
        if t["prazo_entrega"] != "Sem prazo"
        and not t["concluida"]
        and datetime.strptime(t["prazo_entrega"], "%d/%m/%y") < datetime.now()
    ]
    if vencidas:
        print(f"\n⚠️ Você tem {len(vencidas)} tarefa(s) vencida(s)!")

def colorir_prioridade(prioridade):
    prioridade = prioridade.lower()
    if prioridade == 'alta':
        return f"{Fore.RED}{prioridade.capitalize()}{Style.RESET_ALL}"
    elif prioridade == 'media':
        return f"{Fore.YELLOW}{prioridade.capitalize()}{Style.RESET_ALL}"
    elif prioridade == 'baixa':
        return f"{Fore.GREEN}{prioridade.capitalize()}{Style.RESET_ALL}"
    else:
        return prioridade

def salvar_tarefas():
    with open(arquivo_csv, "w", newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for t in tarefas:
            escritor.writerow(t)

def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    print("6. Listar por prioridade")
    print("7. Editar uma tarefa")
    print("8. Filtrar tarefas por prazo")
    print("9. Filtrar por categoria")

def filtrar_por_prazo():
    prazo_filtro = input("Digite o prazo (dd/mm/aa) ou 'vencido' para ver tarefas vencidas: ")

    if prazo_filtro.lower() == 'vencido':
        print("\n--- TAREFAS VENCIDAS ---")
        for i, t in enumerate(tarefas):
            if t["prazo_entrega"] != "Sem prazo":
                try:
                    prazo = datetime.strptime(t["prazo_entrega"], "%d/%m/%y")
                    if prazo < datetime.now() and not t["concluida"]:
                        status = '✅' if t["concluida"] else "❌"
                        print(f"{i + 1}. {t['tarefa']} [{status}] - Prioridade: {t['prioridade']} - Prazo: {t['prazo_entrega']} - Criada em: {t['data_criacao']}")
                except ValueError:
                    continue
    else:
        try:
            prazo_filtrado = datetime.strptime(prazo_filtro, "%d/%m/%y")
            print(f"\n--- TAREFAS COM PRAZO {prazo_filtrado.strftime('%d/%m/%y')} ---")
            for i, t in enumerate(tarefas):
                if t["prazo_entrega"] != "Sem prazo":
                    try:
                        prazo = datetime.strptime(t["prazo_entrega"], "%d/%m/%y")
                        if prazo.date() == prazo_filtrado.date():
                            status = '✅' if t["concluida"] else "❌"
                            print(f"{i + 1}. {t['tarefa']} [{status}] - Prioridade: {t['prioridade']} - Prazo: {t['prazo_entrega']} - Criada em: {t['data_criacao']}")
                    except ValueError:
                        continue
        except ValueError:
            print("⚠️ Formato de data inválido! Use dd/mm/aa.")

carregar_tarefas()

while True:
    tarefa_do_dia()
    mostrar_alerta_vencidas()
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        tarefa = input("Digite uma tarefa: ")
        categoria = input("Digite uma categoria (trabalho, estudo, etc...): ") or "geral"
        prioridade = input("Digite uma prioridade (baixa, media, alta): ").lower().replace('é', 'e')

        if prioridade not in ['baixa', 'media', 'alta']:
            print("❗Prioridade inválida!")
            continue

        prazo_entrega = input("Digite o prazo de entrega (ou deixe em branco): ") or "Sem prazo"
        if prazo_entrega != "Sem prazo":
            try:
                datetime.strptime(prazo_entrega, "%d/%m/%y")
            except ValueError:
                print("❗Data inválida! Tarefa não salva!")
                continue

        data_criacao = datetime.now().strftime("%d/%m/%y %H:%M")
        tarefas.append({
            "tarefa": tarefa,
            "concluida": False,
            "data_criacao": data_criacao,
            "prioridade": prioridade,
            "prazo_entrega": prazo_entrega,
            "categoria": categoria
        })
        salvar_tarefas()
        print("✅ Tarefa adicionada!")

    elif escolha == '2':
        print("\n--- TAREFAS ---")
        for i, t in enumerate(tarefas):
            status = '✅' if t["concluida"] else "❌"
            prioridade_colorida = colorir_prioridade(t['prioridade'])
            print(f"{i + 1}. {t['tarefa']} [{status}] - Prioridade: {prioridade_colorida:<6} - Prazo: {t['prazo_entrega']} - Criada em: {t['data_criacao']}")

    elif escolha == '3':
        try:
            numero = int(input("Número da tarefa concluída: ")) - 1
            if 0 <= numero < len(tarefas):
                tarefas[numero]["concluida"] = True
                salvar_tarefas()
                print("✅ Tarefa marcada como concluída!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")

    elif escolha == '4':
        try:
            numero = int(input("Número da tarefa a remover: ")) - 1
            if 0 <= numero < len(tarefas):
                removida = tarefas.pop(numero)
                salvar_tarefas()
                print(f"🗑️ Tarefa '{removida['tarefa']}' removida!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")

    elif escolha == '5':
        print("Até mais! 👋")
        break

    elif escolha == '6':
        prioridade_desejada = input("Digite a prioridade (baixa, media, alta): ").lower()
        print(f"\n--- TAREFAS COM PRIORIDADE {prioridade_desejada.upper()} ---")
        encontrou = False
        for i, t in enumerate(tarefas):
            if t["prioridade"].lower() == prioridade_desejada:
                status = '✅' if t["concluida"] else "❌"
                prioridade_colorida = colorir_prioridade(t['prioridade'])
                print(f"{i + 1}. {t['tarefa']} [{status}] - Prioridade: {prioridade_colorida} - Prazo: {t['prazo_entrega']} - Criada em: {t['data_criacao']}")
                encontrou = True
        if not encontrou:
            print("Nenhuma tarefa com essa prioridade.")

    elif escolha == '7':
        try:
            numero = int(input("Número da tarefa a editar: ")) - 1
            if 0 <= numero < len(tarefas):
                print("Deixe em branco se não quiser alterar algum campo.")
                nova_tarefa = input("Novo nome da tarefa: ")
                nova_prioridade = input("Nova prioridade (baixa, media, alta): ").lower()
                nova_conclusao = input("Tarefa concluída? (s/n): ").lower()
                novo_prazo = input("Novo prazo para entrega: ")

                if nova_tarefa:
                    tarefas[numero]["tarefa"] = nova_tarefa
                if nova_prioridade in ['baixa', 'media', 'alta']:
                    tarefas[numero]["prioridade"] = nova_prioridade
                if nova_conclusao == 's':
                    tarefas[numero]["concluida"] = True
                elif nova_conclusao == 'n':
                    tarefas[numero]["concluida"] = False
                if novo_prazo:
                    try:
                        datetime.strptime(novo_prazo, "%d/%m/%y")
                        tarefas[numero]["prazo_entrega"] = novo_prazo
                    except ValueError:
                        print("⚠️ Prazo inválido. Mantido o anterior.")
                salvar_tarefas()
                print("✏️ Tarefa atualizada com sucesso!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")

    elif escolha == '8':
        filtrar_por_prazo()

    elif escolha == '9':
        categoria = input("Digite a categoria que deseja filtrar: ").lower()
        print(f"\n--- TAREFAS DA CATEGORIA: {categoria.upper()} ---")
        encontrou = False
        for i, t in enumerate(tarefas):
            if t["categoria"].lower() == categoria:
                status = '✅' if t["concluida"] else "❌"
                print(f"{i + 1}. {t['tarefa']} [{status}] - prioridade {t['prioridade']} - Prazo: {t['prazo_entrega']}")
                encontrou = True
        if not encontrou:
            print("Nenhuma tarefa encontrada para essa categoria.")
    else:
        print("Número inválido!")

