class classe():
    def __init__(self,nome,idade,tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):

        match tipo:
            case "mago":
                print("O Mago atacou usando magia")    
            case "guerreiro":
                print("O Guerreiro atacou usando espada")
            case "monge":
                print("O Monge atacou usando artes marciais")   
            case "ninja":
                print("O Ninja atacou usando shuriken")    

nome = input("Digite o nome do herói: ")
idade = input("Digite a idade do herói: ")
tipo = input("Digite a classe do herói: ")

heroi = classe(nome,idade,tipo)

heroi.atacar()

