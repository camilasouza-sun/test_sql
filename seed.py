import mysql.connector

# 1. Conexão com o MySQL Workbench
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # <--- COLOQUE A SENHA DO SEU MYSQL WORKBENCH AQUI
    database="empilhadeira",
)
cursor = conexao.cursor()


# Função para mostrar todos os dados salvos
def mostrar_tabela():
  print("\n" + "=" * 100)
  print("DADOS SALVOS NO MYSQL - EMPILHADEIRA STEAM EP-3")
  print("=" * 100)
  cursor.execute("SELECT * FROM dados")
  registros = cursor.fetchall()

  if not registros:
    print("A tabela ainda está vazia.")
  else:
    for linha in registros:
      print(f"ID: {linha} | Data/Hora: {linha}")
      print(
          f"  Estado: {linha} | Status: {linha} | Bateria: {linha}%"
      )
      print(
          f"  Peso: {linha}g | Altura: {linha}cm | Tempo: {linha} min"
          f" | Distância: {linha}m"
      )
      print(
          f"  Ambiente: {linha}°C | Umidade: {linha}% | Wi-Fi: {linha}"
          f" | Bluetooth: {linha} | Buzzer: {linha}"
      )
      print("-" * 100)
  print("\n")


# 2. Menu interativo no VS Code
while True:
  print("1 - Adicionar novo dado da Empilhadeira")
  print("2 - Ver dados da tabela MySQL")
  print("3 - Sair")
  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    print("\n--- Novo Registro Completo ---")
    ligada = input("Empilhadeira está (Ligada ou Desligada): ")
    peso = float(input("Peso carregado em gramas (ex: 250.5): "))
    altura = float(input("Altura do garfo em cm (ex: 15.0): "))
    bateria = int(input("Nível da bateria em % (ex: 85): "))
    status = input("Status (Operando, Parada, Carregando ou Alerta): ")
    temperatura = float(input("Temperatura do ambiente em °C (ex: 24.5): "))
    umidade = float(input("Umidade do ambiente em % (ex: 60.0): "))
    wifi = input("Sinal do Wi-Fi (Bom, Moderado ou Ruim): ")
    bluetooth = input("Conexão Bluetooth (Boa, Moderada ou Ruim): ")
    buzzer = input("Buzzer está funcionando? (Funcionando ou Com defeito): ")
    tempo = int(input("Tempo de utilização em minutos (ex: 45): "))
    distancia = float(input("Distância percorrida em metros (ex: 12.5): "))

    sql = """
        INSERT INTO dados (
            empilhadeira_ligada, peso_carga_g, altura_garfo_cm, nivel_bateria_pct,
            status_operacao, temperatura_c, umidade_pct, sinal_wifi,
            conexao_bluetooth, status_buzzer, tempo_utilizacao_min, distancia_percorrida_m
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    valores = (
        ligada,
        peso,
        altura,
        bateria,
        status,
        temperatura,
        umidade,
        wifi,
        bluetooth,
        buzzer,
        tempo,
        distancia,
    )

    cursor.execute(sql, valores)
    conexao.commit()
    print("\n✅ Todos os dados foram salvos com sucesso no MySQL!")

    # Exibe o resultado imediatamente no terminal
    mostrar_tabela()

  elif opcao == "2":
    mostrar_tabela()

  elif opcao == "3":
    print("Encerrando programa...")
    break
  else:
    print("Opção inválida. Digite 1, 2 ou 3.\n")

conexao.close()