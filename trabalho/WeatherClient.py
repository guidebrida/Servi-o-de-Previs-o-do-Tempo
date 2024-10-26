import xmlrpc.client


class WeatherClient:
    def __init__(self, server_url):
        # Inicializa o cliente XML-RPC com a URL do servidor
        self.client = xmlrpc.client.ServerProxy(server_url)

    def obter_previsao_tempo(self, cidade):
        try:
            # Faz a chamada XML-RPC para o servidor
            resposta = self.client.get_weather_forecast(cidade)

            # Retorna a resposta para exibição no menu
            return {
                "cidade": cidade,
                "previsao": resposta
            }
        except Exception as e:
            return {"erro": f"Erro ao obter a previsão do tempo: {e}"}


def exibir_previsao_tempo(previsao):
    # Exibe a previsão do tempo
    for dia in previsao:
        print(f"Data: {dia['data']}")
        print(f"Temperatura: {dia['temperatura']}°C")
        print(f"Umidade: {dia['umidade']}%")
        print(f"Condições: {dia['condicoes']}")
        print(f"Previsão de chuva: {dia['chuva']}%\n")


def main():
    server_url = "http://localhost:8000/"
    weather_client = WeatherClient(server_url)

    # Lista de cidades para o menu
    cidades = [
        "Florianópolis", "Joinville", "Blumenau", "Chapecó", "Lages",
        "Criciúma", "Itajaí", "Balneário Camboriú", "São José", "Tubarão"
    ]

    while True:
        print("Menu de Consulta de Previsão do Tempo")
        print("Selecione uma cidade para consultar a previsão:")

        # Exibe o menu de cidades
        for idx, cidade in enumerate(cidades):
            print(f"{idx + 1}. {cidade}")

        print("0. Sair")
        escolha_cidade = int(input("Digite o número da cidade: "))

        if escolha_cidade == 0:
            break

        if 1 <= escolha_cidade <= len(cidades):
            cidade_selecionada = cidades[escolha_cidade - 1]
            previsao = weather_client.obter_previsao_tempo(cidade_selecionada)

            if "erro" in previsao:
                print(previsao["erro"])
            else:
                # Pergunta se o usuário quer ver a previsão para um dia específico ou todos os dias
                escolha_dia = input("Deseja ver a previsão para um dia específico? (s/n): ").strip().lower()

                if escolha_dia == 's':
                    dia_especifico = input("Digite a data (YYYY-MM-DD): ").strip()
                    previsao_especifica = [dia for dia in previsao["previsao"] if dia["data"] == dia_especifico]

                    if previsao_especifica:
                        print(f"\nPrevisão do tempo para {cidade_selecionada} no dia {dia_especifico}:")
                        exibir_previsao_tempo(previsao_especifica)
                    else:
                        print(f"Nenhuma previsão encontrada para a data {dia_especifico}.")
                else:
                    print(f"\nPrevisão do tempo para {cidade_selecionada} nos próximos 10 dias:")
                    exibir_previsao_tempo(previsao["previsao"])

        else:
            print("Escolha inválida, tente novamente.")


if __name__ == "__main__":
    main()
