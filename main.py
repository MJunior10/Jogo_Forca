import openai
from config import client

def obter_palavra(tema):
    
    prompt = f"Dado o tema '{tema}', forneça uma palavra para jogo da forca sem nenhuma explicação."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que sugere palavras para jogo da forca."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=10,
            temperature=0.5,
        )
        palavra = response.choices[0].message["content"].strip().lower()
        return palavra
    except Exception as e:
        print(f"Erro ao obter palavra: {e}")
        return None


def jogo_da_forca():
   
    tema = input("Digite o tema do jogo da forca: ")
    palavra = obter_palavra(tema)

    if not palavra:
        print("Não foi possível obter uma palavra. Tente novamente mais tarde.")
        return

    tentativas = 6
    letras_erradas = []
    letras_corretas = []

    while tentativas > 0:
        print("\n" + "=" * 30)
        print(f"Tentativas restantes: {tentativas}")
        print("Letras erradas:", ", ".join(letras_erradas))

        
        palavra_oculta = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_oculta += letra
            else:
                palavra_oculta += "_"

        print("Palavra:", " ".join(palavra_oculta))

        
        if palavra_oculta == palavra:
            print("Parabéns! Você acertou a palavra!")
            break

        
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

       
        if letra in palavra:
            letras_corretas.append(letra)
        else:
            letras_erradas.append(letra)
            tentativas -= 1

       
        if tentativas == 0:
            print("\nVocê perdeu! A palavra era:", palavra)
            break

if __name__ == "__main__":
    jogo_da_forca()
