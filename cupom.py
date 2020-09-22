nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def dados_loja():

    if not nome_loja:
        raise Exception("O campo nome da loja é obrigatório")

    if not logradouro:
        raise Exception("O campo logradouro do endereço é obrigatório") 

    _numero = "s/n" if numero == 0 else str(numero)

    if not municipio:
        raise Exception("O campo município do endereço é obrigatório")  

    if not estado:
        raise Exception("O campo estado do endereço é obrigatório") 

    if not cnpj:
        raise Exception("O campo CNPJ da loja é obrigatório") 

    if not inscricao_estadual:
        raise Exception("O campo inscrição estadual da loja é obrigatório")     


    typewriter = nome_loja + "\n"
    typewriter += logradouro + ", " + _numero + " " + complemento + "\n"
    typewriter += bairro + " - " + municipio + " - " + estado + "\n"
    typewriter += "CEP:" + cep + " Tel " + telefone + "\n"
    typewriter += observacao + "\n"
    typewriter += "CNPJ: " + cnpj + "\n"
    typewriter += "IE: " + inscricao_estadual + "\n"
    # Implemente aqui
    return typewriter

print (dados_loja()) 
