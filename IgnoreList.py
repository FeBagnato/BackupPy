from os import replace

class IgnoreList:
    def __init__(self):
        self.__ignoreItens = list("")
        self.__setItens()

    def init(self):
        for itens in self.__getItens():
            replace(itens, f"ignored files/{itens.replace('/', '_')}")

    def end(self):
        for itens in self.__getItens():
            replace(f"ignored files/{itens.replace('/', '_')}", itens)

    def __setItens(self):
        arquivoItens = open("config/ignoreList.conf", 'r')
        itens = arquivoItens.readlines()

        for item in itens:
            self.__ignoreItens.append(item.replace('\n', ''))

        arquivoItens.close()

    def __getItens(self):
        return self.__ignoreItens
