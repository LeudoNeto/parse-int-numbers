def parse_int(string):
    resposta = 0
    ate19 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    dezenas = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    palavras = string.split()
    for x in palavras:
        if x == 'and':
            palavras.remove(x)
    if 'thousand' in string:
        milhar = 0
        posmil = palavras.index('thousand')
        if 'hundred' in palavras[:posmil]:
            for x in range(1,10):
                if palavras[0] == ate19[x]:
                    milhar += x*100
            if palavras.index('thousand') != palavras.index('hundred')+1:
                if palavras[2] in ate19:
                    for x in range(0,20):
                        if palavras[2] == ate19[x]:
                            milhar += x
                elif palavras[2] in dezenas:
                    for x in range(0,8):
                        if palavras[2] == dezenas[x]:
                            milhar += (x+2)*10
                else:
                    for x in range(0,9):
                        for y in range(0,8):
                            if palavras[2] == f'{dezenas[y]}-{ate19[1:10][x]}':
                                milhar += (y+2)*10 + x+1
        else:
            if palavras[0] in ate19:
                for x in range(0,20):
                    if palavras[0] == ate19[x]:
                        milhar += x
            elif palavras[0] in dezenas:
                for x in range(0,8):
                    if palavras[0] == dezenas[x]:
                            milhar += (x+2)*10
            else:
                for x in range(0,9):
                    for y in range(0,8):
                        if palavras[0] == f'{dezenas[y]}-{ate19[1:10][x]}':
                            milhar += (y+2)*10 + x+1
        resposta += milhar*1000
        palavras2 = palavras.copy()
        for x in palavras2[:posmil+1]:
            palavras.remove(x)
    if 'hundred' in palavras:
        for x in range(1,10):
            if palavras[0] == ate19[x]:
                resposta += x*100
        palavras.pop(0)
        palavras.pop(0)
    if len(palavras) > 0:
        if palavras[0] in ate19:
            for x in range(0,20):
                if palavras[0] == ate19[x]:
                    resposta += x
        elif palavras[0] in dezenas:
            for x in range(0,8):
                if palavras[0] == dezenas[x]:
                    resposta += (x+2)*10
        else:
            for x in range(0,9):
                for y in range(0,8):
                    if palavras[0] == f'{dezenas[y]}-{ate19[1:10][x]}':
                        resposta += (y+2)*10 + x+1
    if 'million' in string:
        resposta *= 1000000
    return resposta

#example:
print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))