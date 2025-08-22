# 🌍 Dashboard Interativo COVID-19

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-orange)
![Plotly](https://img.shields.io/badge/Plotly-Express-green)

Um **dashboard interativo** construído com **Streamlit**, **Pandas** e **Plotly**, que permite acompanhar a evolução global e detalhada da pandemia de COVID-19.
O projeto apresenta métricas principais, gráficos de evolução e tabelas com os países mais afetados.

---

## 📌 Funcionalidades

* 🌐 Visualização de métricas globais (casos confirmados, mortes e recuperados).
* 📈 Evolução acumulada de casos globais ao longo do tempo.
* 🔍 Análise detalhada por país, incluindo:

  * Métricas principais (KPIs).
  * Gráfico de evolução diária.
  * Tabela detalhada de dados históricos.
* 🏆 Top 10 países com maior número de casos confirmados.
* 🖥 Interface interativa e amigável com **Streamlit Tabs**.
* 🛠 Filtros dinâmicos na barra lateral.

---

## 🎨 Visual do Dashboard

### 1️⃣ Visão Global

![Exemplo Gráfico Global](https://via.placeholder.com/800x400.png?text=Gráfico+Global)

* Mostra evolução acumulada de casos confirmados, mortes e recuperados.
* KPIs principais com destaque para números globais.

### 2️⃣ Análise Detalhada por País

![Exemplo Gráfico País](https://via.placeholder.com/800x400.png?text=Gráfico+País)

* Seleção do país na barra lateral.
* Gráfico de evolução diária e tabela detalhada de histórico.

> Obs: Substitua essas imagens pelos screenshots reais do seu dashboard.

---

## 🛠 Tecnologias

* **Python 3.10+**
* **Streamlit** – Dashboard interativo.
* **Pandas** – Manipulação e tratamento de dados.
* **Plotly Express** – Visualização interativa de gráficos.

---

## 📁 Estrutura do Projeto

```
covid-dashboard/
│
├─ covid_19_data.csv         # Arquivo de dados CSV da COVID-19
├─ app.py                    # Código principal do dashboard
├─ requirements.txt          # Dependências do projeto
└─ README.md                 # Documentação
```

---

## ⚡ Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/covid-dashboard.git
cd covid-dashboard
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o dashboard:

```bash
streamlit run app.py
```

---

## 🧩 Estrutura do Código

* `load_data()` – Carrega e trata os dados com tipos otimizados.
* `get_countries()` – Retorna países disponíveis (cacheado).
* `get_global_metrics()` – Métricas globais pré-calculadas.
* `global_evolution()` – Dados globais agrupados para gráficos.
* `country_metrics()` – Métricas e evolução por país (cacheado).

---

## 🚀 Melhorias de Performance

* **Cache otimizado** para funções e dados repetitivos.
* **Tipos numéricos menores (`int32`)** → menos uso de memória.
* **Cálculos pré-processados** para métricas globais e por país.
* **Uso de `st.metric`** para KPIs mais rápido que HTML customizado.
* **Código modular e limpo**, fácil manutenção.
* **Lazy loading de gráficos e tabelas** para grandes datasets.

---

## 📚 Referências

* [Streamlit Documentation](https://docs.streamlit.io/)
* [Pandas Documentation](https://pandas.pydata.org/)
* [Plotly Express Documentation](https://plotly.com/python/plotly-express/)

---

## 👤 Autor

**Kelven Silva**

* Desenvolvedor Python e Analista de Dados
* LinkedIn: [linkedin.com/in/kelvensilva](https://linkedin.com/in/kelvensilva)

---

## 📌 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Como Contribuir

1. Faça um fork do projeto.
2. Crie uma branch para sua feature: `git checkout -b feature/nome-da-feature`.
3. Faça commit das suas alterações: `git commit -m 'Adicionei nova feature'`.
4. Envie para o repositório remoto: `git push origin feature/nome-da-feature`.
5. Abra um Pull Request.

Contribuições são bem-vindas para melhorar o dashboard e a experiência do usuário!
