"""Leitura dos arquivos CSV do projeto."""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
FOLDER = Path(__file__).parent
COUNTRIES_PATH = FOLDER / "paises.csv"


def read_countries():
    """Lê o CSV de países e devolve uma lista de dicionários.

    Os valores vêm do jeito que estão no arquivo, ou seja, como texto
    """
    countries = []
    try:
        with open(COUNTRIES_PATH, "r", encoding="utf-8") as files:
            reader = csv.DictReader(files)
            for line in reader:
                countries.append(line)
    except FileNotFoundError:
        print("O arquivo paises.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return countries

def converter_preco(preco):
    """Converte um preço do site em número: "£51.77" -> 51.77"""
    return float(preco.replace("£", ""))



def prepare_countries(lines):
    """Recebe as linhas lidas do CSV e devolve os paises formatados."""
    countries = []
    for line in lines:
        country = {
            "titulo": line["titulo"],
            "preco": line["preco"],
            "categoria": line["categoria"],
            "nota": line["nota"],
            "url": line["url"]
        }
        countries.append(country)

    return countries

def load_countries():
    """Lê o CSV e já devolve os paises prontos para usar."""
    return prepare_countries(read_countries())


if __name__ == "__main__":
    pass
