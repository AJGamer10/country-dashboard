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
        raw_cotacao = line.get("cotacao_brl")
        if raw_cotacao and raw_cotacao != "N/A":
            try:
                cotacao_val = float(raw_cotacao)
            except ValueError:
                cotacao_val = None
        else:
            cotacao_val = None
        country = {
            "pais": line["pais"],
            "regiao": line["regiao"],
            "populacao": line["populacao"],
            "area_mi2": line["area_mi2"],
            "densidade": line["densidade"],
            "pib_per_capita": line["pib_per_capita"],
            "alfabetizacao": line["alfabetizacao"],
            "telefones_por_mil": line["telefones_por_mil"],
            "natalidade": line["natalidade"],
            "mortalidade": line["mortalidade"],
            "mortalidade_infantil": line["mortalidade_infantil"],
            "moeda": line.get("moeda", "N/A"),
            "cotacao_brl": cotacao_val,
        }
        countries.append(country)

    return countries

def load_countries():
    """Lê o CSV e já devolve os paises prontos para usar."""
    return prepare_countries(read_countries())


if __name__ == "__main__":
    pass
