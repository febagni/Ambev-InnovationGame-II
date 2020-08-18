import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

opcao = input("Dados de todos os anos (opcao 0) ou especifico (opcao 1): ")

df = pd.read_csv('data.csv')
df['number_of_tweets'] = df['date'].apply(lambda x: x[0:4])

if (opcao == str(0)):
    dt = df['number_of_tweets'].value_counts()
    dt = pd.DataFrame(dt)
    dt.index.name = 'year'
    dt.reset_index(inplace=True)
    sns_plot = sns.lineplot('year', 'number_of_tweets', data=dt)
    plt.savefig("Numero_de_tweets_por_ano.png")

if (opcao == str(1)):
    ano = input("Entre o ano:")
    df_19 = df[df['number_of_tweets'] == str(ano)]
    df_19['number_of_tweets_19'] = df_19['date'].apply(lambda x: x[5:7])
    dt_19 = df_19['number_of_tweets_19'].value_counts()
    dt_19 = pd.DataFrame(dt_19)
    dt_19.index.name = 'mes'
    dt_19.reset_index(inplace=True)
    sns_plot = sns.lineplot('mes', 'number_of_tweets_19', data=dt_19)
    plt.savefig("Numero_de_tweets_em_" + str(ano) + ".png")
