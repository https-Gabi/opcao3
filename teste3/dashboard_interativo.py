import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# dados
file_path = "3/Data/data32413.csv"
df = pd.read_csv(file_path)

# faixas etárias
def categorize_age(age):
    if 18 <= age <= 24:
        return "18-24"
    elif 25 <= age <= 31:
        return "25-31"
    elif 32 <= age <= 38:
        return "32-38"
    elif 46 <= age <= 52:
        return "46-52"
    elif 53 <= age <= 60:
        return "53-60"
    else:
        return "Outros"

df["Faixa Etária"] = df["Idade"].apply(categorize_age)

# título do dashboard
st.title("Dashboard Interativo: Comportamento de Uso de Dispositivos")

# filtros 
st.sidebar.header("Filtros")
sistema_operacional = st.sidebar.multiselect(
    "Sistema Operacional",
    options=df["Sistema Operacional"].unique(),
    default=df["Sistema Operacional"].unique(),
)

gênero = st.sidebar.multiselect(
    "Gênero",
    options=df["Gender"].unique(),
    default=df["Gender"].unique(),
)


df_filtered = df[
    (df["Sistema Operacional"].isin(sistema_operacional)) &
    (df["Gender"].isin(gênero))
]

st.write(f"### Dados Filtrados ({len(df_filtered)} registros)")
st.dataframe(df_filtered)

# visualizaçõe 
st.write("## Visualizações")

# distribuição de tempo de tela
st.write("### Distribuição de Tempo de Tela (Frequência x Horas)")
fig, ax = plt.subplots()
sns.histplot(df_filtered["Tempo de tela ligada (horas/dia)"], bins=10, kde=True, ax=ax, color='blue')
ax.set_title("Distribuição de Tempo de Tela")
ax.set_xlabel("Tempo de Tela Ligada (horas/dia)")
ax.set_ylabel("Frequência")
st.pyplot(fig)

# tempo médio de uso por faixa etária
st.write("### Tempo Médio de Uso por Faixa Etária")
fig, ax = plt.subplots()
df_filtered.groupby("Faixa Etária")["Tempo de tela ligada (horas/dia)"].mean().plot.bar(ax=ax, color='green')
ax.set_title("Tempo Médio de Tela por Faixa Etária")
ax.set_ylabel("Tempo Médio de Tela (horas/dia)")
st.pyplot(fig)

# número de apps instalados por idade
st.write("### Número de Apps Instalados por Idade")
fig, ax = plt.subplots()
df_filtered.groupby("Idade")["Número de aplicativos instalados"].mean().plot(ax=ax, marker='o')
ax.set_title("Número Médio de Apps Instalados por Idade")
ax.set_ylabel("Média de Apps Instalados")
ax.set_xlabel("Idade")
st.pyplot(fig)

# tempo médio de uso por gênero
st.write("### Tempo Médio de Uso por Gênero")
fig, ax = plt.subplots()
df_filtered.groupby("Gender")["Tempo de tela ligada (horas/dia)"].mean().plot.bar(ax=ax, color='orange')
ax.set_title("Tempo Médio de Tela por Gênero")
ax.set_ylabel("Tempo Médio de Tela (horas/dia)")
st.pyplot(fig)

# uso médio por sistema operacional
st.write("### Uso Médio por Sistema Operacional")
fig, ax = plt.subplots()
df_filtered.groupby("Sistema Operacional")["Tempo de tela ligada (horas/dia)"].mean().plot.bar(ax=ax, color='purple')
ax.set_title("Uso Médio por Sistema Operacional")
ax.set_ylabel("Tempo Médio de Tela (horas/dia)")
st.pyplot(fig)

# uso médio de bateria por dispositivo
st.write("### Uso Médio de Bateria por Dispositivo")
fig, ax = plt.subplots()
df_filtered.groupby("Modelo do dispositivo")["Drenagem da bateria (mAh/dia)"].mean().plot.bar(ax=ax, color='red')
ax.set_title("Uso Médio de Bateria por Dispositivo")
ax.set_ylabel("Drenagem Média de Bateria (mAh/dia)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig)

# uso médio de dados móveis por sistema operacional
st.write("### Uso Médio de Dados Móveis por Sistema Operacional")
fig, ax = plt.subplots()
df_filtered.groupby("Sistema Operacional")["Uso de dados (MB/dia)"].mean().plot.bar(ax=ax, color='cyan')
ax.set_title("Uso Médio de Dados Móveis por Sistema Operacional")
ax.set_ylabel("Uso Médio de Dados (MB/dia)")
st.pyplot(fig)

# uso médio de dados móveis por dispositivo
st.write("### Uso Médio de Dados Móveis por Dispositivo")
fig, ax = plt.subplots()
df_filtered.groupby("Modelo do dispositivo")["Uso de dados (MB/dia)"].mean().plot.bar(ax=ax, color='magenta')
ax.set_title("Uso Médio de Dados Móveis por Dispositivo")
ax.set_ylabel("Uso Médio de Dados (MB/dia)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig)

# app drain vs. número de apps instalados
st.write("### Relação: App Drain vs. Número de Apps Instalados")
fig, ax = plt.subplots()
sns.scatterplot(
    x="Número de aplicativos instalados",
    y="Drenagem da bateria (mAh/dia)",
    data=df_filtered,
    ax=ax,
    hue="Sistema Operacional"
)
ax.set_title("App Drain vs. Número de Apps Instalados")
ax.set_xlabel("Número de Apps Instalados")
ax.set_ylabel("Drenagem de Bateria (mAh/dia)")
st.pyplot(fig)

# renagem de bateria vs. data 
st.write("### Relação: Drenagem de Bateria vs. Uso de Dados")
fig, ax = plt.subplots()
sns.scatterplot(
    x="Uso de dados (MB/dia)",
    y="Drenagem da bateria (mAh/dia)",
    data=df_filtered,
    ax=ax,
    hue="Sistema Operacional"
)
ax.set_title("Drenagem de Bateria vs. Uso de Dados")
ax.set_xlabel("Uso de Dados (MB/dia)")
ax.set_ylabel("Drenagem de Bateria (mAh/dia)")
st.pyplot(fig)
