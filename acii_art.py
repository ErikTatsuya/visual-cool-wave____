from PIL import Image

# Conjunto de caracteres para mapear os níveis de brilho.
# Quanto mais denso o caractere, mais escuro o pixel.
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Redimensiona a imagem mantendo a proporção."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """Converte a imagem para escala de cinza."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Mapeia os pixels da imagem para o conjunto de caracteres ASCII."""
    pixels = image.getdata()
    characters = ""
    for pixel_value in pixels:
        characters += ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256]
    return characters

def main(image_path):
    # Tenta abrir a imagem.
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Não foi possível abrir a imagem. Erro: {e}")
        return

    # Processa a imagem.
    image = resize_image(image)
    image = grayify(image)

    # Converte os pixels para caracteres.
    ascii_text = pixels_to_ascii(image)

    # O texto será uma única string longa. Para imprimi-lo como uma imagem,
    # dividimos a string por linhas baseadas na nova largura.
    img_width = image.width
    ascii_art = ""
    for i in range(0, len(ascii_text), img_width):
        ascii_art += ascii_text[i:i + img_width] + "\n"

    # Imprime e salva o resultado.
    print(ascii_art)

    # Você também pode salvar o resultado em um arquivo de texto.
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)

# Use o nome da sua imagem aqui. Certifique-se de que a imagem
# está na mesma pasta que o script.
if __name__ == '__main__':
    main("image.png") # Mude para o nome do seu arquivo de imagem.