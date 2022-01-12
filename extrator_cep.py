import re #Expressão regular RegEx

endereco = "Rua Quararibéia, 199 Bloco 02 Apto 102 - São Paulo/SP CEP:04689160"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)


