"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados

def build_table(countries):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    table = []
    for country in countries:
        line = {
            "País": country["pais"],
            "Região": country["regiao"],
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
        if country["regiao"] not in regions:
            regions.append(country["regiao"])

    regions.sort()
    return regions

def filter_for_region(countries, region):
    """Devolve só os países da região escolhida. Com "Todas", devolve todos."""
    if region == "Todas":
        return countries

    result = []
    for country in countries:
        if country["regiao"] == region:
            result.append(country)

    return result

def main():
    st.set_page_config(page_title="Dashboard de Países", page_icon="🌎​", layout="wide")
    st.title("🌎​ Dashboard de Países")

    countries = dados.load_countries()

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