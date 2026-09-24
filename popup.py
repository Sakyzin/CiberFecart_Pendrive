import tkinter as tk
from PIL import Image, ImageTk
import random
import os

PASTA_IMAGENS = r"C:/Users/fecartciber/Documents/teste/imagens"

IMAGENS = [
    os.path.join(PASTA_IMAGENS, "Imagem1.png"),
    os.path.join(PASTA_IMAGENS, "Imagem2.png"),
    os.path.join(PASTA_IMAGENS, "Imagem3.png"),
    os.path.join(PASTA_IMAGENS, "Imagem4.png"),
    os.path.join(PASTA_IMAGENS, "Imagem5.png"),
    os.path.join(PASTA_IMAGENS, "Imagem6.png"),
]

AVISO = os.path.join(PASTA_IMAGENS, "AVISO.png")
FINAL = os.path.join(PASTA_IMAGENS, "FINAL.png")

QUANTIDADE = 150
INTERVALO = 40

root = tk.Tk()
root.withdraw()

janelas = []


def fechar_tudo(event=None):
    for janela in janelas:
        try:
            janela.destroy()
        except:
            pass

    try:
        root.destroy()
    except:
        pass


def abrir_imagem_especial(caminho):

    if not os.path.exists(caminho):
        print("Imagem não encontrada:", caminho)
        return

    tela_largura = root.winfo_screenwidth()
    tela_altura = root.winfo_screenheight()

    # 85% da tela
    largura = int(tela_largura * 0.85)
    altura = int(tela_altura * 0.85)

    # Centraliza
    x = (tela_largura - largura) // 2
    y = (tela_altura - altura) // 2

    janela = tk.Toplevel(root)

    # Remove barra de título e bordas
    janela.overrideredirect(True)

    # Mantém por cima
    janela.attributes("-topmost", True)

    janela.geometry(
        f"{largura}x{altura}+{x}+{y}"
    )

    imagem_original = Image.open(caminho)

    # Mantém a proporção da imagem
    imagem_original.thumbnail(
        (largura, altura),
        Image.Resampling.LANCZOS
    )

    imagem = ImageTk.PhotoImage(imagem_original)

    label = tk.Label(
        janela,
        image=imagem,
        bg="black",
        borderwidth=0,
        highlightthickness=0
    )

    label.image = imagem
    label.pack(
        expand=True,
        fill="both"
    )

    # ESC fecha tudo
    janela.bind("<Escape>", fechar_tudo)
    label.bind("<Escape>", fechar_tudo)

    # Permite que a janela receba o ESC
    janela.focus_force()

    janelas.append(janela)

    return janela


def mostrar_final():
    abrir_imagem_especial(FINAL)


def mostrar_aviso():

    abrir_imagem_especial(AVISO)

    # 5 segundos depois
    root.after(
        5000,
        mostrar_final
    )


def criar_popup(numero=0):

    if numero >= QUANTIDADE:
        mostrar_aviso()
        return

    caminho = random.choice(IMAGENS)

    if not os.path.exists(caminho):

        print(
            "Imagem não encontrada:",
            caminho
        )

        root.after(
            INTERVALO,
            criar_popup,
            numero + 1
        )

        return

    # Tamanho aleatório
    largura = random.randint(200, 550)
    altura = random.randint(150, 450)

    tela_largura = root.winfo_screenwidth()
    tela_altura = root.winfo_screenheight()

    x = random.randint(
        0,
        max(0, tela_largura - largura)
    )

    y = random.randint(
        0,
        max(0, tela_altura - altura)
    )

    janela = tk.Toplevel(root)

    # REMOVE a barra superior e as bordas
    janela.overrideredirect(True)

    janela.geometry(
        f"{largura}x{altura}+{x}+{y}"
    )

    imagem_original = Image.open(caminho)

    imagem_original.thumbnail(
        (largura, altura),
        Image.Resampling.LANCZOS
    )

    imagem = ImageTk.PhotoImage(imagem_original)

    label = tk.Label(
        janela,
        image=imagem,
        bg="black",
        borderwidth=0,
        highlightthickness=0
    )

    label.image = imagem

    label.pack(
        expand=True,
        fill="both"
    )

    # ESC fecha tudo
    janela.bind("<Escape>", fechar_tudo)
    label.bind("<Escape>", fechar_tudo)

    janelas.append(janela)

    root.after(
        INTERVALO,
        criar_popup,
        numero + 1
    )


root.bind(
    "<Escape>",
    fechar_tudo
)

criar_popup()

root.mainloop() 