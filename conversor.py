import requests

def obter_cotacao(moeda_origem, moeda_destino):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao acessar a API.")
        return None

    dados = resposta.json()
    chave = f"{moeda_origem}{moeda_destino}"
    
    if chave in dados:
        return float(dados[chave]['bid'])
    else:
        print("Moeda não encontrada.")
        return None

def converter_moeda():
    print("=== Conversor de Moedas ===")
    moeda_origem = input("De qual moeda você quer converter? (ex: BRL, USD, EUR): ").upper()
    moeda_destino = input("Para qual moeda você quer converter? (ex: USD, BRL, EUR): ").upper()
    valor = float(input("Digite o valor a ser convertido: "))

    cotacao = obter_cotacao(moeda_origem, moeda_destino)

    if cotacao:
        convertido = valor * cotacao
        print(f"\n{valor:.2f} {moeda_origem} = {convertido:.2f} {moeda_destino}")
    else:
        print("Conversão não realizada.")

if __name__ == "__main__":
    while True:
        converter_moeda()
        repetir = input("\nDeseja converter outro valor? (s/n): ").lower()
        if repetir != 's':
            break
