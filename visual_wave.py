import time, os, keyboard

os.system("cls")
'''
    cores:
    🟥🟧🟨🟩🟦🟪🟫⬛⬜
    🔴🟠🟡🟢🔵🟣🟤⚫⚪



    
'''
def exibir_painel(x):
    print(x)
    time.sleep(0.05)

def wave(x):
    loop1 = True
    os.system("cls")
    print("pressione shift para parar o programa.")
    time.sleep(1)
    os_var = 0
    while loop1 == True:
        os_var = os_var + 1
        for i in range(0, len(x)):
            exibir_painel(x[i])
            time.sleep(0.05)

        if os_var % 100 == 0:
            os_var = 0
            os.system("cls")
            
        elif keyboard.is_pressed("shift"):
            loop1 = False
            os.system("cls")

Color_Spectre_Square_Wave = [
    "🟥🟧🟨🟩🟦🟪" * 7,
    "🟧🟨🟩🟦🟪🟥" * 7,
    "🟨🟩🟦🟪🟥🟧" * 7,
    "🟩🟦🟪🟥🟧🟨" * 7,
    "🟦🟪🟥🟧🟨🟩" * 7,
    "🟪🟥🟧🟨🟩🟦" * 7
    ]

Color_Bounce_Ball_Wave = []
for i in range(0, 86):
    if i < 43:
        Color_Bounce_Ball_Wave.append(" " * (42 - i) + "🔴🟠🟡🟢🔵🟣" + " " * i)
    else:
        mirrored_i = 85 - i
        Color_Bounce_Ball_Wave.append(" " * (42 - mirrored_i) + "🔴🟠🟡🟢🔵🟣" + " " * mirrored_i)

Neutral_Color_Multiple_Worm_Square_Wave = [
    "⬛⬛⬛⬛⬜⬜" * 7,
    "⬛⬛⬛⬜⬜⬛" * 7,
    "⬛⬛⬜⬜⬛⬛" * 7,
    "⬛⬜⬜⬛⬛⬛" * 7,
    "⬜⬜⬛⬛⬛⬛" * 7,
    "⬛⬜⬜⬛⬛⬛" * 7,
    "⬛⬛⬜⬜⬛⬛" * 7,
    "⬛⬛⬛⬜⬜⬛" * 7,
    "⬛⬛⬛⬛⬜⬜" * 7,
    ]

Neutral_Color_Bounce_Single_Worm_Square_Wave = []

for i in range(0, 86):
    if i < 43:
        Neutral_Color_Bounce_Single_Worm_Square_Wave.append("⬛" * (42 - i) + "⬜⬜⬜⬜" + "⬛" * i)
    else:
        mirrored_i = 85 - i
        Neutral_Color_Bounce_Single_Worm_Square_Wave.append("⬛" * (42 - mirrored_i) + "⬜⬜⬜⬜" + "⬛" * mirrored_i)

#varíaveis de loops while.

loop = True
loop_newline = True

while loop == True:

    print("digite .help para ver os comandos.")
    opção = input("Digite a opção: ")

    """

    comandos:

    """

    if opção == ".help":
        os.system("cls")
        print(".neutral_color - exibe as ondas disponiveis pré-definidas em preto e branco.")
        print(".color - exibe as ondas disponiveis pré-definidas em cores.")
        print(".new - para você criar a sua própria onda.")
        print(".clear - limpa a tela.")
        print(".ctrl - finaliza o programa.")
    
    elif opção == ".clear":
        os.system("cls")
    
    elif opção == ".new":
        line_newline = []
        os.system("cls")

        while loop_newline == True:
            print(loop_newline)

            print("digite .newline para criar uma nova linha.")
            print("digite .showline para exibir a linha.")
            print("digite .final para finalizar as linhas.")
            print("digite .cancel para cancelar.\n")

            print("digite na linha de baixo.")
            print("⬇")

            opção_newline = input(":")

            if opção_newline == ".newline":
                input_newline = input("newline: ")
                print(input_newline)
                line_newline.append(input_newline)
            
            elif opção_newline == ".showline":
                print(line_newline)

            elif opção_newline == ".clearline":
                line_newline.clear()
                print("linha limpa.")

            elif len(line_newline) != 0:
                if opção_newline == ".final":
                    print("a linha não pode ser vazia.tente novamente.")
                    wave(line_newline)
            
            if opção_newline == ".cancel":
                loop_newline = False
    
    elif opção == ".color":
        print("➡ CSSW ou Color_Spectre_Square_Wave - para exibir as cores em onda.")
        print("➡ CBBW ou Color_Bounce_Ball_Wave - para exibir ondas coloridas com efeito de uma minhoca única.")

    elif opção == ".neutral_color":
        print("➡ NCMWSW ou Neutral_Color_Multiple_Worm_Square_Wave - para exibir ondas em preto e branco.")
        print("➡ NCBSWSW ou Neutral_Color_Bounce_Single_Worm_Square_Wave - para exibir ondas em preto e branco com efeito de uma minhoca única.")


    #opções de ondas

    #neutral color

    elif opção in ["NCMWSW", "Neutral_Color_Multiple_Worm_Square_Wave"]:
        wave(Neutral_Color_Multiple_Worm_Square_Wave)
    
    elif opção in ["NCBSWSW", "Neutral_Color_Bounce_Single_Worm_Square_Wave"]:
        wave(Neutral_Color_Bounce_Single_Worm_Square_Wave)
    
    #color

    elif opção in ["CBBW", "Color_Bounce_Ball_Wave"]:
        wave(Color_Bounce_Ball_Wave)

    elif opção in ["CSSW", "Color_Spectre_Square_Wave"]:
        wave(Color_Spectre_Square_Wave)

    #comandos de finalização

    elif opção in [".ctrl", ".Ctrl", "Ctrl", "ctrl"]:
        os.system("cls")
        loop = False

    elif keyboard.is_pressed("ctrl"):
        os.system("cls")
        loop = False
    
    else:
        print("opção inválida, tente novamente.")
        time.sleep(1.0)
        os.system("cls")