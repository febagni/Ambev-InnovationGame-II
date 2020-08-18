
import pandas as pd
import numpy as np

anos = np.random.randint(2012,2020,size=(5000,1))
anos 
possiveis_estados = ['AC','AL','AP','AM','BA','CE','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO','DF']
array_iteravel = list(np.random.randint(0,len(possiveis_estados),size=5000))
regiao = [possiveis_estados[x] for x in array_iteravel]

retweets = np.random.randint(0,20,size=5000)
replys = np.random.randint(0,10,size=5000)
favoritos = np.random.randint(0,50,size=5000)
random_ids = np.random.randint(100000000,999999999,size=5000)
from faker import Faker
faker = Faker()
random_first_name = [faker.first_name().lower() for x in range(5000)]
random_last_name = [faker.last_name().lower() for x in range(5000)]
random_name = [random_first_name[x] + random_last_name[x] for x in range(len(random_first_name))]
random_username = [random_name[x] + str(np.random.randint(0,100)) for x in range(5000)]
random_dates = []

while (len(random_dates) < 5000):
    x = str(faker.date_of_birth())
    if(int(x[0:4]) > 2012):
        random_dates.append(x)

users_ids = np.random.randint(1000000,9999999,size=5000)
random_text = [str(faker.word()) + " " + str(faker.word()) + " " + str(faker.word()) + " " + str(faker.word()) + " #bebida #saudavel" for x in range(5000)]
data = {"username" : random_username,
        "ID" : random_ids,
        "user_id" : users_ids,
        "text" : random_text,
        "date" : random_dates,
        "location" : regiao,
        "nbr_retweet" : retweets,
        "nbr_favorite" : favoritos,
        "nbr_reply" : replys,
        "is_reply" : replys > 0,
        "is_retweet" : retweets > 0}
df = pd.DataFrame(data)
df.to_csv(r'data.csv')