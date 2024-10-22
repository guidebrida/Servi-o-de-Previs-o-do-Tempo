import xmlrpc.client


class Client:
    def __init__(self, server_url):
        # Inicializa o cliente XML-RPC com a URL do servidor
        self.client = xmlrpc.client.ServerProxy(server_url)

    def obter_previsao_tempo(self, cidade):
        try:
            # Faz a chamada XML-RPC para o servidor
            resposta = self.client.get_weather_forecast(cidade)

            # Processa e exibe a resposta
            print(f"Previsão do tempo para {cidade}:")
            print(f"Temperatura: {resposta['temperatura']}°C")
            print(f"Umidade: {resposta['umidade']}%")
            print(f"Condições: {resposta['condicoes']}")
            print(f"Previsão de chuva: {resposta['chuva']}%")
        except Exception as e:
            print(f"Erro ao obter a previsão do tempo: {e}")


if __name__ == "__main__":
    # URL do servidor onde o cliente vai se conectar
    server_url = "http://localhost:8000/"

    # Inicializa o cliente
    weather_client = WeatherClient(server_url)

    # Solicita a previsão do tempo para uma cidade
    cidade = "São Paulo"
    weather_client.obter_previsao_tempo(cidade)
