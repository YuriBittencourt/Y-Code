entrada = open("source.txt","r")
comparar = open("saidaKaratsuba.txt","r")
saida = open("comparacao.txt","w")

for line in entrada:
    valorKaratsuba=comparar.readline()
    values=line.split(" ")
    valorMult=int(values[0])*int(values[1])

    if valorMult == int(valorKaratsuba):
       saida.write(valorKaratsuba)
    else:
       saida.write("esperado: " + valorMult + " recebido: " + valorKaratsuba)

entrada.close()
comparar.close()
saida.close()
