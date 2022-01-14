class IgnoreList:
    def __init__(self):
        self.__ignoreItens = list("")
        self.__setItens()

    def isItenInIgnoreList(self, iten, pasta):
        itenInList = bool(False)
        for count in range(len(self.__getItens())):
            if pasta in self.__getItens()[count] and self.__getItens()[count]\
                    .endswith(f"/{iten}"):
                        itenInList = True
                        break

        return itenInList

    def __setItens(self):
        arquivoItens = open("config/ignoreList.conf", 'r')
        itens = arquivoItens.readlines()

        for item in itens:
            self.__ignoreItens.append(item.replace('\n', ''))

        arquivoItens.close()

    def __getItens(self):
        return self.__ignoreItens
