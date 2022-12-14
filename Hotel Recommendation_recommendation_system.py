# -*- coding: utf-8 -*-
"""Copy of Submission 2 - Recommendation System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xvjBQxAZ36mqwttFvkEyfuECXRf-w6UR

#Open Dataset from csv file
"""

import pandas as pd
# hotel = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Datafiniti_Hotel_Reviews.csv')
hotel = pd.read_csv('/content/cleaned_data.csv')
hotel

"""#Data Understanding"""

hotel.info()

hotel

hotel.head()

hotel.isnull().sum()

hotel.describe()

hotel.impression.unique()

"""#Data Preparation"""

# Mengonversi data series ‘country’ menjadi dalam bentuk list
country = hotel['country'].tolist()
 
# Mengonversi data series ‘name’ menjadi dalam bentuk list
name = hotel['name'].tolist()
 
# Mengonversi data series ‘rating’ menjadi dalam bentuk list
rating = hotel['rating'].tolist()
 
print(len(country))
print(len(name))
print(len(rating))

# Membuat dictionary untuk data ‘name’, ‘countries’, dan ‘rating’
hotel_new = pd.DataFrame({
    'name': name,
    'ountries': country,
    'rating': rating
})
hotel_new

hotel_new['ountries'].value_counts()

"""#ML Modeling

Using content based filtering to make recommendation system
"""

data = hotel_new
data.sample(5)

"""**Using TF-IDF Vectorized**"""

from sklearn.feature_extraction.text import TfidfVectorizer
 
# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()
 
# Melakukan perhitungan idf pada data cuisine
tf.fit(data['ountries']) 
 
# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['ountries']) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# # Membuat dataframe untuk melihat tf-idf matrix
# # Kolom diisi dengan jenis masakan
# # Baris diisi dengan nama resto
 
# pd.DataFrame(
#     tfidf_matrix.todense(), 
#     columns=tf.get_feature_names(),
#     index=data.name
# ).sample(22, axis=1).sample(10, axis=0)

"""**Using Cosine Similarity**"""

from sklearn.metrics.pairwise import cosine_similarity
 
# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama resto
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['name'], columns=data['name'])
print('Shape:', cosine_sim_df.shape)
 
# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

cosine_sim_df.loc["NASA BANGKOK"]

def hotel_recommendations(name, similarity_data=cosine_sim_df, items=data[['name', 'ountries']], k=10):

 
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,name].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(name, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)

hotel.loc[1]

data[data.name.eq('Maharadja Hotel')]

"""**Model Testing**"""

# Mendapatkan rekomendasi restoran yang mirip dengan KFC
hotel_recommendations('Maharadja Hotel')

sim_to_nasa=hotel_recommendations("NASA BANGKOK")
sim_to_nasa

sim_claro= hotel_recommendations("CLARO Makassar")
sim_claro

k=10

#Precision = total jawaban benar/ total jawaban
sim_to_nasa=hotel_recommendations("NASA BANGKOK")
precision = sim_to_nasa["ountries"].loc[sim_to_nasa["ountries"]=="Thailand"].value_counts()[0]/k
precision