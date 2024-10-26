from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime, timedelta
import random

class WeatherServer:
    def __init__(self):
        # Inicializando o banco de dados fictício de previsão do tempo para 10 dias
        self.dados_previsao = {
            "Florianópolis": self.gerar_previsao("Florianópolis"),
            "Joinville": self.gerar_previsao("Joinville"),
            "Blumenau": self.gerar_previsao("Blumenau"),
            "Chapecó": self.gerar_previsao("Chapecó"),
            "Lages": self.gerar_previsao("Lages"),
            "Criciúma": self.gerar_previsao("Criciúma"),
            "Itajaí": self.gerar_previsao("Itajaí"),
            "Balneário Camboriú": self.gerar_previsao("Balneário Camboriú"),
            "São José": self.gerar_previsao("São José"),
            "Tubarão": self.gerar_previsao("Tubarão"),
        }

    def gerar_previsao(self, cidade):
        # Gera dados fictícios de previsão do tempo para os próximos 10 dias
        previsao = []
        base_date = datetime.now().date()

        for dia in range(10):
            data = base_date + timedelta(days=dia)
            previsao.append({
                "data": data.strftime("%Y-%m-%d"),
                "temperatura": self.gerar_temperatura(),
                "umidade": self.gerar_umidade(),
                "condicoes": self.gerar_condicoes(),
                "chuva": self.gerar_chuva()
            })

        return previsao

    def gerar_temperatura(self):
        # Gera uma temperatura aleatória entre 15 e 30 graus Celsius
        return round(15 + (30 - 15) * random.random())

    def gerar_umidade(self):
        # Gera uma umidade aleatória entre 50 e 90%
        return round(50 + (90 - 50) * random.random())

    def gerar_condicoes(self):
        # Gera condições do tempo aleatórias
        condicoes = ["Ensolarado", "Parcialmente Nublado", "Nublado", "Chuvoso"]
        return random.choice(condicoes)

    def gerar_chuva(self):
        # Gera uma previsão de chuva aleatória entre 0% e 100%
        return round(0 + (100 - 0) * random.random())

    def get_weather_forecast(self, cidade):
        # Retorna os dados da previsão do tempo para a cidade solicitada
        return self.dados_previsao.get(cidade, [])

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
