# projeto_5
# Análise Exploratório de Anúncios de Vendas de Carros
Este é um projeto de análise de dados que utiliza um aplicativo web interativo para visualizar informações de um conjunto de dados sobre anúncios de vendas de veículos nos EUA
O objetivo do aplicativo é permitir que o usuário explore visualmente características dos veículos de forma rápida e interativa através de gráficos.

## Funcionalidadess.

O aplicativo web oferece as seguintes funcionalidades:
* **Carregamento de dados:** Os dados são lidos a partir de um arquivo 'vehicles.csv'.
* **Histograma:** Ao marcar uma caixa de seleção, é gerado um histograma para visualizar a distribuição de quilometragem dos veículos.
* **Dispersão:** Ao marcar outra caixa de seleção, é gerado um gráfico de dispersão para explorar a relação entre a quilometragem e o preço dos veículos.
* **Interface Interativa:** Os gráficos são gerados sob demanda, de acordo com a seleção do usuário, proporcionando uma experiência de análise mais dinâmica.

## Tecnologia utilizada
* Python
* Streamlit (para criação do aplicativo web)
* Pandas (para manipulação dos dados)
* Plotly express (para a criação de gráficos interativos)

## Como executar o projeto>
Para executar este aplicativo em seu ambiente local, siga os passos abaixo:
1. **Clone o Repositório**
'''bash
git clone [https://github.com/TodiBoas/projeto_5.git](https://github.com/TodiBoas/projeto_5.git)
cd projeto_5
'''

2. **Crie e ative um ambiente virtual:**
'''bash
python -m venv .venv
source .venv/Scripts/activate
'''

3. **Instale as dependências:**
'''bash
pip install - requirements.txt
'''

4. **Execute o aplicativo Streamlit:**
'''bash
streamlit run app.py
'''
Após executar o comando, uma aba será aberta no seu navegador com o aplicativo.