# country-dashboard
**Membros:** Noah Dias, Abner Edgar, Gabriel Jeremias
**Dataset:** paises.csv + https://github.com/AJGamer10/country-dashboard?tab=readme-ov-file
**App publicado:** https://paisesdomundo.streamlit.app
## Funcionalidades
- [x] Leitura do CSV
- [x] Conversão das colunas
- [x] Mostrar métricas sobre o dataset
- [x] Classificar os registros em faixas a partir de uma coluna numérica e mostrar a faixa na tabela
- [x] Mostra uma tabela de dados com os países e suas informações
- [x] Uma barra de pesquisa
- [x] Um filtro por categoria
- [x] Busca e filtro funcionando juntos
- [x] Uma mensagem quando nenhum resultado for encontrado
- [x] Código organizado em funções e módulos
- [x] App publicado no Streamlit Community Cloud
## Funcionalidade extra
Será feito um mecanismo de câmbio para a moeda do país
## Como rodar
Siga o passo a passo abaixo:
1. Abra o terminal dentro da pasta do projeto e crie o ambiente virtual com o seguinte comando: python -m venv .venv
2. Ainda no terminal, ative o ambiente virtual com o seguinte comando: .venv\Scripts\Activate.ps1
3. Ainda no terminal, baixe as dependências do projeto com o seguinte comando: pip install -r index/requirements.txt
4. Ainda no terminal, para abrir o site utilize o seguinte comando: streamlit run index/app.py
