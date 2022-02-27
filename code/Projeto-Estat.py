# -*- coding: utf-8 -*-

%pip install wbdata
import pandas as pd
import wbdata as wb
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('default') 

#Iniciarei observando PIB per capita ao longo dos países.
#importando agora os dados internacionais de PIB per capita pela API do Banco Mundial.
pib_growth = {'NY.GDP.PCAP.KD.ZG':'GDP per capita growth (annual %)'} 
pib_nivel = {'NY.GDP.PCAP.KD':'GDP per capita (constant 2010 US$)'}

df_mundo_pib_growth = wb.get_dataframe(indicators = pib_growth, country = 'all')
#print(df_mundo_pib_growth)

df_mundo_pib_nivel = wb.get_dataframe(indicators = pib_nivel, country = "all")
#print(df_mundo_pib_nivel)

#Aqui eu filtro os países com maiores e menores PIB per capita em 2010 e em 1960
print(df_mundo_pib_nivel.filter(like='2010',axis=0).dropna().sort_values(by=['GDP per capita (constant 2010 US$)']).tail(15))
print(df_mundo_pib_nivel.filter(like='1960',axis=0).dropna().sort_values(by=['GDP per capita (constant 2010 US$)']).tail(15))
print(df_mundo_pib_nivel.filter(like='2010',axis=0).dropna().sort_values(by=['GDP per capita (constant 2010 US$)']).head(15))
print(df_mundo_pib_nivel.filter(like='1960',axis=0).dropna().sort_values(by=['GDP per capita (constant 2010 US$)']).head(15))

todos_os_paises = wb.get_country(country_id=None) #lista de países e IDs
#print(todos_os_paises)

#Além dos 5 países do topo e da cauda de cada ano, foram selecionados também Brasil, Coreia do Sul
#Em uma primeira análise, tinha-se também Qatar, Etiópia e Suíça, removidos por apresentar grandes intervalos sem dados (NaN).
#Países selecionados. 
countries = ['BRA','MWI','LSO','CHN','BDI','IND','COD','NER','USA','LUX','AUS','NOR','DNK','KOR']


df_pib_nivel = wb.get_dataframe(indicators = pib_nivel, country = countries)  
#print(df_pib_nivel)

#Usando agora apenas os dados de 1965 a 2010 com intervalos de 5 e 5 anos para homogeneizar as duas bases de dados.
df_pib_nivel_2 = df_pib_nivel.reset_index()
df_pib_nivel_3 = df_pib_nivel_2[df_pib_nivel_2.date.isin(['1965','1970','1975','1980','1985','1990','1995','2000','2005','2010'])] 

#Reorganizando o Dataframe com os países lado a lado
Australia_nivel =     df_pib_nivel_3[0:10].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Australia'})[['date','Australia']].set_index('date')
Burundi_nivel =       df_pib_nivel_3[10:20].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Burundi'})[['date','Burundi']].set_index('date')
Brazil_nivel =        df_pib_nivel_3[20:30].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Brazil'})[['date','Brazil']].set_index('date')
China_nivel=          df_pib_nivel_3[30:40].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'China'})[['date','China']].set_index('date')
Congo_Dem_Rep_nivel = df_pib_nivel_3[40:50].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Congo Dem Rep'})[['date','Congo Dem Rep']].set_index('date')
Denmark_nivel =       df_pib_nivel_3[50:60].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Denmark'})[['date','Denmark']].set_index('date')
India_nivel =         df_pib_nivel_3[60:70].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'India'})[['date','India']].set_index('date') 
Korea_Rep_nivel =     df_pib_nivel_3[70:80].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Korea Rep'})[['date','Korea Rep']].set_index('date')
Lesotho_nivel =       df_pib_nivel_3[80:90].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Lesotho'})[['date','Lesotho']].set_index('date')
Luxembourg_nivel =    df_pib_nivel_3[90:100].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Luxembourg'})[['date','Luxembourg']].set_index('date')
Malawi_nivel =        df_pib_nivel_3[100:110].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Malawi'})[['date','Malawi']].set_index('date')
Niger_nivel =         df_pib_nivel_3[110:120].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Niger'})[['date','Niger']].set_index('date')
Norway_nivel =        df_pib_nivel_3[120:130].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'Norway'})[['date','Norway']].set_index('date')
United_States_nivel = df_pib_nivel_3[130:140].sort_values(by=['date']).rename(columns={'GDP per capita (constant 2010 US$)':'United States'})[['date','United States']].set_index('date')

df_pib_nivel_4 = pd.concat([Australia_nivel,Burundi_nivel,Brazil_nivel,China_nivel,Congo_Dem_Rep_nivel,
                            Denmark_nivel, India_nivel, Korea_Rep_nivel, Lesotho_nivel,Luxembourg_nivel,
                            Malawi_nivel, Niger_nivel, Norway_nivel, United_States_nivel], axis=1)
print(df_pib_nivel_4)

#Visualizando primeiro o pib per capita dos países no topo da lista
fig, ax = plt.subplots()

df_pib_nivel_4["Australia"].plot(ax=ax, legend=False, linestyle="dashed")
df_pib_nivel_4["United States"].plot(ax=ax, legend=False, linestyle="dashed")
df_pib_nivel_4["Denmark"].plot(ax=ax, legend=False, linestyle="dotted")
df_pib_nivel_4["Luxembourg"].plot(ax=ax, legend=False, linestyle="dotted")
df_pib_nivel_4["Norway"].plot(ax=ax, legend=False, linestyle="dotted")

ax.set_title('Países no topo da lista')
ax.set_ylabel("GDP per capita (constant 2010 US$)")
plt.legend()

#Visualizando agora a cauda da lista
fig, ax = plt.subplots()

df_pib_nivel_4["India"].plot(ax=ax, legend=False, linestyle="solid")
df_pib_nivel_4["Burundi"].plot(ax=ax, legend=False, linestyle="dashed")
df_pib_nivel_4["Congo Dem Rep"].plot(ax=ax, legend=False, linestyle="dotted")
df_pib_nivel_4["Lesotho"].plot(ax=ax, legend=False, linestyle="dotted")
df_pib_nivel_4["Malawi"].plot(ax=ax, legend=False, linestyle="dashed")
df_pib_nivel_4["Niger"].plot(ax=ax, legend=False, linestyle="dotted")
df_pib_nivel_4["China"].plot(ax=ax, legend=False, linestyle="solid")

ax.set_title('Países na cauda da lista')
ax.set_ylabel("GDP per capita (constant 2010 US$)")
plt.legend()

#Visualizando países diversificados na lista
fig, ax = plt.subplots()

df_pib_nivel_4["India"].plot(ax=ax, legend=False, linestyle="solid")
df_pib_nivel_4["Burundi"].plot(ax=ax, legend=False, linestyle="dashed")
df_pib_nivel_4["China"].plot(ax=ax, legend=False, linestyle="solid")
df_pib_nivel_4["Australia"].plot(ax=ax, legend=False, linestyle="dashed")
df_pib_nivel_4["Korea Rep"].plot(ax=ax, legend=False, linestyle="dotted")
df_pib_nivel_4["Brazil"].plot(ax=ax, legend=False, linestyle="dotted")

ax.set_title('Países diversificados na lista')
ax.set_ylabel("GDP per capita (constant 2010 US$)")
plt.legend()

#Observando agora as taxas de variação.
df_pib_growth = wb.get_dataframe(indicators = pib_growth, country = countries)  
#print(df_pib_growth)

#Usando agora apenas os dados de 1965 a 2010 com intervalos de 5 e 5 anos para homogeneizar as duas bases de dados.
df_pib_growth_2 = df_pib_growth.reset_index()
df_pib_growth_3 = df_pib_growth_2[df_pib_growth_2.date.isin(['1965','1970','1975','1980','1985','1990','1995','2000','2005','2010'])]    

#Reorganizando o Dataframe com os países lado a lado
Australia_growth =     df_pib_growth_3[0:10].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Australia'})[['date','Australia']].set_index('date')
Burundi_growth =       df_pib_growth_3[10:20].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Burundi'})[['date','Burundi']].set_index('date')
Brazil_growth =        df_pib_growth_3[20:30].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Brazil'})[['date','Brazil']].set_index('date')
China_growth=          df_pib_growth_3[30:40].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'China'})[['date','China']].set_index('date')
Congo_Dem_Rep_growth = df_pib_growth_3[40:50].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Congo Dem Rep'})[['date','Congo Dem Rep']].set_index('date')
Denmark_growth =       df_pib_growth_3[50:60].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Denmark'})[['date','Denmark']].set_index('date')
India_growth =         df_pib_growth_3[60:70].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'India'})[['date','India']].set_index('date') 
Korea_Rep_growth =     df_pib_growth_3[70:80].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Korea Rep'})[['date','Korea Rep']].set_index('date')
Lesotho_growth =       df_pib_growth_3[80:90].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Lesotho'})[['date','Lesotho']].set_index('date')
Luxembourg_growth =    df_pib_growth_3[90:100].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Luxembourg'})[['date','Luxembourg']].set_index('date')
Malawi_growth =        df_pib_growth_3[100:110].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Malawi'})[['date','Malawi']].set_index('date')
Niger_growth =         df_pib_growth_3[110:120].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Niger'})[['date','Niger']].set_index('date')
Norway_growth =        df_pib_growth_3[120:130].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'Norway'})[['date','Norway']].set_index('date')
United_States_growth = df_pib_growth_3[130:140].sort_values(by=['date']).rename(columns={'GDP per capita growth (annual %)':'United States'})[['date','United States']].set_index('date')


df_pib_growth_4 = pd.concat([Australia_growth, Burundi_growth, Brazil_growth, China_growth, Congo_Dem_Rep_growth,
                             Denmark_growth, India_growth, Korea_Rep_growth, Lesotho_growth, Luxembourg_growth,
                             Malawi_growth, Niger_growth, Norway_growth, United_States_growth], axis=1)
print(df_pib_growth_4)

#Visualizando primeiro crescimento do pib per capita dos países no topo da lista
df_pib_growth_head = df_pib_growth_4[['Australia','United States','Denmark','Luxembourg','Norway']]
df_pib_growth_head.plot(kind='bar')
plt.title('Países no topo da lista')
plt.ylabel('GDP per capita growth')

#Visualizando agora a cauda da lista
df_pib_growth_tail = df_pib_growth_4[['India','Burundi','Congo Dem Rep','Lesotho','Malawi','Niger','China']]
df_pib_growth_tail.plot(kind='bar').legend(loc='lower right',ncol=3)
plt.title('Países na cauda da lista')
plt.ylabel('GDP per capita growth')

#Visualizando países diversificados
df_pib_growth_diverso = df_pib_growth_4[['India','Burundi','China','Australia','Korea Rep','Brazil']]
df_pib_growth_diverso.plot(kind='bar').legend(loc='upper center',ncol=2)
plt.title('Países diversificados na lista')
plt.ylabel('GDP per capita growth')


#Agora irei coletar dados de educação para buscar entender melhor o PIB per capita.

# Estou aqui importando a base de dados de educação de Barro e Lee "Education Attainment for Total Population Aged 25-64" disponível em < http://www.barrolee.com/ >.
# O único tratamento no excel dado foi desfazer as células mescladas.
df_educ = pd.read_excel(r"C:/Users/renan/OneDrive/Documentos/Economia/BarroLeeTratado.xls", sheet_name="Sheet1", header=5)
#print(df_educ.head(25))

#Aqui o Dataframe é filtrado apenas com as colunas, os países e os anos selecionados
df_educ2 = df_educ[df_educ.Year.isin([1950,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010])].fillna(method='ffill')
df_educ3 = df_educ2[df_educ2.Year.isin([1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010])]
df_educ4 = df_educ3[['Country','Year','Avg. Years of Total Schooling']]
df_educ5 = df_educ4[df_educ4.Country.isin(['Australia','Burundi','Brazil','China',
                                           'Democratic Republic of the Congo','Denmark',
                                           'India','Republic of Korea','Lesotho','Luxembourg',
                                           'Malawi','Niger','Norway','USA'])].sort_values(by=['Country','Year'])
print(df_educ5)
print(df_educ5.Country[109:154])
#Reorganizando o Dataframe com os países lado a lado
Australia_educ =     df_educ5[0:11].rename(columns={'Avg. Years of Total Schooling':'Australia'})[['Year','Australia']].set_index('Year')
Brazil_educ =        df_educ5[11:22].rename(columns={'Avg. Years of Total Schooling':'Brazil'})[['Year','Brazil']].set_index('Year')
Burundi_educ =       df_educ5[22:33].rename(columns={'Avg. Years of Total Schooling':'Burundi'})[['Year','Burundi']].set_index('Year')
China_educ=          df_educ5[33:44].rename(columns={'Avg. Years of Total Schooling':'China'})[['Year','China']].set_index('Year')
Congo_Dem_Rep_educ = df_educ5[44:55].rename(columns={'Avg. Years of Total Schooling':'Congo Dem Rep'})[['Year','Congo Dem Rep']].set_index('Year')
Denmark_educ =       df_educ5[55:66].rename(columns={'Avg. Years of Total Schooling':'Denmark'})[['Year','Denmark']].set_index('Year')
India_educ =         df_educ5[66:77].rename(columns={'Avg. Years of Total Schooling':'India'})[['Year','India']].set_index('Year') 
Lesotho_educ =       df_educ5[77:88].rename(columns={'Avg. Years of Total Schooling':'Lesotho'})[['Year','Lesotho']].set_index('Year')
Luxembourg_educ =    df_educ5[88:99].rename(columns={'Avg. Years of Total Schooling':'Luxembourg'})[['Year','Luxembourg']].set_index('Year')
Malawi_educ =        df_educ5[99:110].rename(columns={'Avg. Years of Total Schooling':'Malawi'})[['Year','Malawi']].set_index('Year')
Niger_educ =         df_educ5[110:121].rename(columns={'Avg. Years of Total Schooling':'Niger'})[['Year','Niger']].set_index('Year')
Norway_educ =        df_educ5[121:132].rename(columns={'Avg. Years of Total Schooling':'Norway'})[['Year','Norway']].set_index('Year')
Korea_Rep_educ =     df_educ5[132:143].rename(columns={'Avg. Years of Total Schooling':'Korea Rep'})[['Year','Korea Rep']].set_index('Year')
United_States_educ = df_educ5[143:154].rename(columns={'Avg. Years of Total Schooling':'United States'})[['Year','United States']].set_index('Year')

df_educ6 = pd.concat([Australia_educ,Burundi_educ,Brazil_educ,China_educ,Congo_Dem_Rep_educ,
                      Denmark_educ, India_educ, Korea_Rep_educ, Lesotho_educ,
                      Luxembourg_educ, Malawi_educ, Niger_educ, Norway_educ, United_States_educ], axis=1)
df_educ7 = df_educ6[df_educ6.index.isin([1965,1970,1975,1980,1985,1990,1995,2000,2005,2010])]
print(df_educ7)

#Visualizando primeiro o nível de educação dos países no topo da lista de PIB per capita
fig, ax = plt.subplots()

df_educ7["Australia"].plot(ax=ax, legend=False, linestyle="dashed")
df_educ7["United States"].plot(ax=ax, legend=False, linestyle="dashed")
df_educ7["Denmark"].plot(ax=ax, legend=False, linestyle="dotted")
df_educ7["Luxembourg"].plot(ax=ax, legend=False, linestyle="dotted")
df_educ7["Norway"].plot(ax=ax, legend=False, linestyle="dotted")

ax.set_title('Países no topo da lista')
ax.set_ylabel("Média de anos de escolaridade")
plt.legend()

#Visualizando agora a cauda da lista
fig, ax = plt.subplots()

df_educ7["India"].plot(ax=ax, legend=False, linestyle="solid")
df_educ7["Burundi"].plot(ax=ax, legend=False, linestyle="dashed")
df_educ7["Congo Dem Rep"].plot(ax=ax, legend=False, linestyle="dotted")
df_educ7["Lesotho"].plot(ax=ax, legend=False, linestyle="dotted")
df_educ7["Malawi"].plot(ax=ax, legend=False, linestyle="dashed")
df_educ7["Niger"].plot(ax=ax, legend=False, linestyle="dotted")
df_educ7["China"].plot(ax=ax, legend=False, linestyle="solid")

ax.set_title('Países na cauda da lista')
ax.set_ylabel("Média de anos de escolaridade")
plt.legend()

#Visualizando países diversificados na lista
fig, ax = plt.subplots()

df_educ7["India"].plot(ax=ax, legend=False, linestyle="solid")
df_educ7["Burundi"].plot(ax=ax, legend=False, linestyle="dashed")
df_educ7["China"].plot(ax=ax, legend=False, linestyle="solid")
df_educ7["Australia"].plot(ax=ax, legend=False, linestyle="dashed")
df_educ7["Korea Rep"].plot(ax=ax, legend=False, linestyle="dotted")
df_educ7["Brazil"].plot(ax=ax, legend=False, linestyle="dotted")

ax.set_title('Países diversificados na lista')
ax.set_ylabel("Média de anos de escolaridade")
plt.legend()

#Construindo agora um Dataframe com a variação dos anos de escolaridade.
df_educ_diff = df_educ6.diff().drop(1960)
print(df_educ_diff)

#Visualizando primeiro a variação dos anos de escolaridade dos países no topo da lista.
df_educ_diff_head = df_educ_diff[['Australia','United States','Denmark','Luxembourg','Norway']]
df_educ_diff_head.plot(kind='bar')
plt.title('Países no topo da lista')
plt.ylabel('Variação dos anos de escolaridade')

#Visualizando agora a cauda da lista
df_educ_diff_tail = df_educ_diff[['India','Burundi','Congo Dem Rep','Lesotho','Malawi','Niger','China']]
df_educ_diff_tail.plot(kind='bar').legend(loc='lower left',ncol=3)
plt.title('Países na cauda da lista')
plt.ylabel('Variação dos anos de escolaridade')

#Visualizando países diversificados
df_educ_diff_diverso = df_educ_diff[['India','Burundi','China','Australia','Korea Rep','Brazil']]
df_educ_diff_diverso.plot(kind='bar').legend(loc='lower right',ncol=2)
plt.title('Países diversificados na lista')
plt.ylabel('Variação dos anos de escolaridade')

#df_mundo_pib_nivel.filter(like='2010',axis=0).dropna().sort_values(by=['GDP per capita (constant 2010 US$)']).tail(15).to_csv(r'C:\Users\renan\OneDrive\Documentos\Economia\Mestrado\Estatistica\Projeto\tail_mundo_pib_2010.csv')
#df_mundo_pib_nivel.filter(like='1960',axis=0).dropna().sort_values(by=['GDP per capita (constant 2010 US$)']).tail(15).to_csv(r'C:\Users\renan\OneDrive\Documentos\Economia\Mestrado\Estatistica\Projeto\tail_mundo_pib_1960.csv')
#df_mundo_pib_nivel.filter(like='2010',axis=0).dropna().sort_values(by=['GDP per capita (constant 2010 US$)']).head(15).to_csv(r'C:\Users\renan\OneDrive\Documentos\Economia\Mestrado\Estatistica\Projeto\head_mundo_pib_2010.csv')
#df_mundo_pib_nivel.filter(like='1960',axis=0).dropna().sort_values(by=['GDP per capita (constant 2010 US$)']).head(15).to_csv(r'C:\Users\renan\OneDrive\Documentos\Economia\Mestrado\Estatistica\Projeto\head_mundo_pib_1960.csv')   
#df_pib_nivel_4.to_csv(r'C:\Users\renan\OneDrive\Documentos\Economia\Mestrado\Estatistica\Projeto\pib_nivel.csv')
#df_pib_growth_4.to_csv(r'C:\Users\renan\OneDrive\Documentos\Economia\Mestrado\Estatistica\Projeto\pib_growth.csv')
#df_educ7.to_csv(r'C:\Users\renan\OneDrive\Documentos\Economia\Mestrado\Estatistica\Projeto\educacao.csv')
#df_educ_diff.to_csv(r'C:\Users\renan\OneDrive\Documentos\Economia\Mestrado\Estatistica\Projeto\educ_var.csv')
