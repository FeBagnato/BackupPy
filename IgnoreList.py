class IgnoreList:
    def __init__(self):
        self.__ignoreItens = list("")
        self.__setItens()

    def __setItens(self):
        arquivoItens = open("config/ignoreList.conf", 'r')
        itens = arquivoItens.readlines()

        for item in itens:
            self.__ignoreItens.append(item.replace('\n', ''))

        arquivoItens.close()

    def getItens(self):
        return self.__ignoreItens
