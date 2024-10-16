#peça um valor em dias e converta para semnanas e dias

dias = int(input('Digite um valor em dias:'))
semanas = dias // 7
dias = dias % 7
print(f'{dias} dias equivalem a {semanas} semanas e {dias} dias')
