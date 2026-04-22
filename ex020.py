#Fazendo a primeira implementação de Árvore Binária

#Classe Nó
class No:
  def __init__(self, dado = None):
    self.__dado = dado
    self.__dir = None
    self.__esq = None

  # get
  @property
  def dado(self):
    return self.__dado

  # set
  @dado.setter
  def dado(self, novo):
    self.__dado = novo

  # get
  @property
  def dir(self):
    return self.__dir

  # set
  @dir.setter
  def dir(self, novo):
    self.__dir = novo

  # get
  @property
  def esq(self):
    return self.__esq

  # set
  @esq.setter
  def esq(self, novo):
    self.__esq = novo
    pass

#Classe da Árvore Binária
class Arvore_Binaria:

  def __init__(self):
    self.__root = None

  @property
  def root(self):
    return self.__root

  @root.setter
  def root(self, root):
    self.__root = No(root)

  def em_ordem(self, no):
    if no != None:
      self.em_ordem(no.esq)
      print(no.dado)
      self.em_ordem(no.dir)

  def pre_ordem(self, no):
    if no != None:
      print(no.dado)
      self.pre_ordem(no.esq)
      self.pre_ordem(no.dir)

  def pos_ordem(self, no):
    if no != None:
      self.pos_ordem(no.esq)
      self.pos_ordem(no.dir)
      print(no.dado)

#Programa Principal
def main():
    arvore = Arvore_Binaria()

    arvore.root = No("A")
    arvore.root.esq = No("B")
    arvore.root.dir = No("C")

    p = arvore.root.esq
    q = arvore.root.dir

    p.esq = No("D")
    p.dir = No("E")

    q.esq = No("F")
    q.dir = No("G")

    arvore.em_ordem(arvore.root)

if __name__ == "__main__":
    main()