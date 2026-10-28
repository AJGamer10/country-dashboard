"""Dashboard de Países: app Streamlit.
"""

import streamlit as st
from math import trunc, pow

import dados

def build_table(countries):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    table = []
    for country in countries:
        cotacao = country.get("cotacao_brl")

        if cotacao is not None:
            cotacao_fmt = f"R$ {float(cotacao):.2f}"
        else:
            cotacao_fmt = "N/A"
        line = {
            "País": country["pais"],
            "Região": country["regiao"],
            "Moeda": country.get("moeda", "N/A"),
            "Cotação em R$": cotacao_fmt,
            "População": country["populacao"],
            "Área por m²": country["area_mi2"],
            "Densidade demografica": country["densidade"],
            "PIB per capita": country["pib_per_capita"],
            "Alfabetização": country["alfabetizacao"],
            "Telefones por mil": country["telefones_por_mil"],
            "Natalidade": country["natalidade"],
            "Mortalidade": country["mortalidade"],
            "Mortalidade infantil": country["mortalidade_infantil"]
        }
        table.append(line)
    return table

def search_for_name(countries, search):
    """Devolve só os países cujo nome contém o texto buscado."""
    founded = []
    for country in countries:
        if search.lower().strip() in country["pais"].lower().strip():
            founded.append(country)

    return founded

def list_regions(countries):
    """Devolve as reagiões dos países, sem repetição e em ordem alfabética."""
    regions = []
    for country in countries:
        region = format_region(country["regiao"])
        if region not in regions:
            regions.append(region)

    regions.sort()
    return regions


def list_nome_moeda(countries):
    """Devolve os nomes e moedas dos países, sem repetição e em ordem alfabética."""
    nomes_moedas = []
    for country in countries:
        nome_moeda = [country["pais"], country.get("moeda", "N/A"), float(country["cotacao_brl"])]
        if nome_moeda not in nomes_moedas:
            nomes_moedas.append(nome_moeda)

    nomes_moedas.sort()
    return nomes_moedas

def cambio(cotacao, real):
    calculo = real/cotacao
    return round(calculo, 2)

def filter_for_region(countries, region):
    """Devolve só os países da região escolhida. Com "Todas", devolve todos."""
    if region == "Todas":
        return countries

    result = []
    for country in countries:
        if country["regiao"] == region:
            result.append(country)

    return result

def format_region(region: str):
    """Traduz os nomes das regiões"""
    match region:
        case "ASIA (EX. NEAR EAST)":
            return "ASIA (EXC. ORIENTE PRÓXIMO)"
        case "BALTICS":
            return "BALTICOS"
        case "C.W. OF IND. STATES":
            return "COM. DOS ESTADOS INDEP."
        case "EASTERN EUROPE":
            return "EUROPA ORIENTAL"
        case "LATIN AMER. & CARIB":
            return "AMÉRICA LAT. E CARIBE"
        case "NEAR EAST":
            return "ORIENTE PROXIMO"
        case "NORTHERN AFRICA":
            return "ÁFRICA DO NORTE"
        case "NORTHERN AMERICA":
            return "AMÉRICA DO NORTE"
        case "OCEANIA":
            return "OCEANIA"
        case "SUB-SAHARAN AFRICA":
            return "ÁFRICA SUBSAARIANA"
        case "WESTERN EUROPE":
            return "EUROPA OCIDENTAL"
        case _:
            pass

def format_num(num: int):
    """Adiciona notação pela quantidade de classes numéricas"""
    thousend_separator = ["", " mil", " milhões", " bilhões"]
    error_correct = [3, 6, 9]
    thousend_separators_amount = trunc(len(str(num))/3)-1 if len(str(num)) in error_correct else trunc(len(str(num))/3)
    return f"{round(num / (pow(1000, thousend_separators_amount)), 2)}" + thousend_separator[thousend_separators_amount]
    
            

def main():
    st.set_page_config(page_title="Países do Mundo", page_icon="🌎​", layout="wide")
    st.title("Países do Mundo")

    countries = dados.load_countries()

    with st.sidebar:
        st.title("Câmbio")
        search_sidebar = st.selectbox(
            "Buscar países",
            ["Selecionar"] + list_nome_moeda(countries),
            format_func=lambda country: country if isinstance(country, str) else country[0],
        )
        if search_sidebar != "Selecionar":
            reais = st.number_input("Valor em Reais", min_value=0.0, value=0.0, step=0.01, format="%.2f")
            conversao = cambio(search_sidebar[2], reais)
            st.text_input(
                f"Conversão para {search_sidebar[1]}",
                value=f"{conversao:.2f}",
                disabled=True,
            )


    col1, col2, col3, col4 = st.columns(4)
    countries_amount = len(countries)
    col1.metric("Total de países", countries_amount)

    col_search, col_regions = st.columns(2)

    search = col_search.text_input("Buscar países")
    region = col_regions.selectbox("Filtrar por Região", ["Todas"] + list_regions(countries))

    countries_region = filter_for_region(countries, region)
    founded = search_for_name(countries_region, search)

    countries_amount = len(founded)

    if countries_amount == 0:
        st.warning("Nenhum país encontrado")
    else:
        st.write(f"Países encontrados: {countries_amount}")
        st.dataframe(build_table(founded))

if __name__ == "__main__":
    main()