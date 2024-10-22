from xmlrpc.server import SimpleXMLRPCServer

class server:
    def __init__(self):
        # Inicializando o banco de dados fictício de previsão do tempo
        self.dados_previsao = {
            "São Paulo": {
                "temperatura": 25,
                "umidade": 70,
                "condicoes": "Ensolarado",
                "chuva": 10
            },
            "Rio de Janeiro": {
                "temperatura": 30,
                "umidade": 60,
                "condicoes": "Parcialmente Nublado",
                "chuva": 20
            }
        }

    def get_weather_forecast(self, cidade):
        # Retorna os dados da previsão do tempo para a cidade solicitada
        return self.dados_previsao.get(cidade, {
            "temperatura": "Desconhecida",
            "umidade": "Desconhecida",
            "condicoes": "Cidade não encontrada",
            "chuva": "Desconhecida"
        })

def run_server():
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Servidor de previsão do tempo em execução...")

    # Inicializando a instância do servidor de previsão do tempo
    weather_server = WeatherServer()

    # Registrando os métodos da classe WeatherServer para serem acessíveis pelo cliente
    server.register_instance(weather_server)

    # Mantém o servidor rodando
    server.serve_forever()

if __name__ == "__main__":
    run_server()
