'''
O Código Morse é um sistema de representação de letras, algarismos e sinais de pontuação através
de um sinal codificado enviado de modo intermitente. Foi desenvolvido por Samuel Morse em 1837, 
criador do telégrafo elétrico, dispositivo que utiliza correntes elétricas para controlar eletroímãs 
que atuam na emissão e na recepção de sinais. 
O script tem a finalidade de decifrar uma mensagem em código morse e salvá-la em texto claro.
'''

import os
import sys
import datetime
import pandas as pd
from config import file_path, dict_morse

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços e palavras por dois espaços
    output : frase escrita em letras e algarismos
    '''
    words = msg.split("  ")  # Divide a mensagem em palavras
    decoded_message = []
    
    for word in words:
        letters = word.split(" ")  # Divide a palavra em letras
        decoded_word = [dict_morse.get(letter, '') for letter in letters]  # Pega o caractere correspondente ou vazio
        decoded_message.append("".join(decoded_word))
    
    return " ".join(decoded_message)

def save_clear_msg_csv_hdr(msg_claro):
    '''
    input : mensagem em texto claro
    output : palavra escrita em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode="a", index=False, header=hdr)

if __name__ == "__main__":
    msg_claro = decode_morse(sys.argv[1])
    save_clear_msg_csv_hdr(msg_claro)
    print(f"Mensagem decifrada: {msg_claro}")
