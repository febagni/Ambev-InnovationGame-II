# Ambev-InnovationGame-II

**Trilha:** Tracking de Mercado

A ideia de fazer um Tracking de Mercado utilizando o web scraping no lugar de pesquisas de satisfação já utilizadas pelas empresas atualmente vem da facilidade com que essas pesquisas são ignoradas, respondidas de forma não-satisfatória e o espaço amostral ser muito flutuante. É relevante ressaltar que uma má coleta de dados gera uma má análise. Assim, é preciso organizar e descrever os dados de forma inteligente e intuitiva para entender melhor os dados e, assim, fazer a análise e interpretação dos mesmos. Com um bom algoritmo, é possível transformar os dados em informações, que se traduz em uma acurácia melhor do radar de mercado, que é principal fonte de valor do nosso projeto, e que agrega valor para o trabalho realizado pelo analista (persona).

Vale ressaltar que decidimos focar o desenvolvimento no backend da solução, que envolve os temas de data science, análise e web scraping. 

Durante a mentoria, foi levantada a questão legal do scraping e de acordo com os artigos 44 e 48 da LGPD, fazer o web scraping sem consentimento do titular dos dados configura como ato irregular. 

Assim, aplicamos para o uso das APIs das plataformas e como ainda não obtivemos a resposta, fizemos um algoritmo que cria um data base artificial de forma aleatória e crua, inspirado em um Crawling que fizemos no Twitter, gerando 5000 tweets-exemplo para a demonstração no formato que seria a saída do web scraping.

Desenvolvido em Python e com o auxílio de algumas bibliotecas (Pandas, MatPlotLib, NumPy e Seaborn), conseguimos fazer a estruturação dos dados crus para a análise do post. 

Para fazer uma análise dos posts por localização, por exemplo, usando a biblioteca Folium, conseguimos plotar a distribuição dos dados por estado brasileiro em um mapa, o que facilita bastante a visualização dos dados pro analista.

Além desse exemplo, podemos usar outros filtros para análise e apresentar os dados de diversas formas. O analista pode escolher o escopo dos dados e filtros para o que deseja observar no mercado, podendo ter uma visão mais holística das tendências atuais e passadas, para traçar projeções futuras.Assim, a solução consiste em um software de web scraping que carrega e extrai dados automaticamente de várias páginas de sites com base em suas necessidades. É feito sob medida para um site específico ou pode ser configurado para funcionar com qualquer site. Com o clique de um botão você pode salvar facilmente os dados disponíveis no site em um arquivo em seu computador. Ademais, é possível aplicar filtros como, por exemplo, datas, local, palavras-chave, entre outras, para realizar uma coleta mais direcionada de acordo com os dados de interesse. 

Assim, a ferramenta serve tanto para a análise das tendências no mercado de bebidas não-alcoólicas, quanto para outros ramos e setores do mercado. Como, por exemplo, inovações no setor de delivery, que pode afetar o mercado das bebidas, nas formas de entrega ao consumidor final. Além de ramos que afetam indiretamente e que cabe ao analista estudar.

