from personagem_rpg import *


def main():
    p1 = Guerreiro(nome="Kratos", vida=2000)
    p2 = Mago(nome="Merlin", vida=3000)

    p1.atacar(p2, forca=1000)
    p2.curar()
    p2.atacar(p1, forca=20000)

    # Agora vai funcionar perfeitamente!
    p1.morreu(p1, reviveu=2000)
    p1.atacar(p2, forca=2000)
    p2.curar()


if __name__ == "__main__":
    main()
