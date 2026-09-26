def ping(ip_destino):
    print(f"Disparando contra {ip_destino} com 32 bytes de dados:")
    print(f"Resposta de {ip_destino}: bytes=32 tempo=12 ms TTL=64")
    print(f"Resposta de {ip_destino}: bytes=32 tempo=10 ms TTL=64")
    print(f"Estatisticas do Ping para {ip_destino}: Concluido com sucesso.")
url = input("Digite o endereço IP ou URL para ping: ")
ping(url)
print(" -" * 30)
ping("google.com")