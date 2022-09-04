# Laporan Proyek Machine Learning - Ahmad Reinaldi Akbar

## _Project Overview_

Hotel merupakan tempat yang paling dicari oleh para _traveller_ ketika mereka pergi untuk liburan baik itu ke luar kota atau ke luar negeri. Sehingga dibutuhkan sebuah sistem untuk memberikan rekomendasi hotel sesuai tempat tujuan pengguna untuk memesan kamar di hotel tersebut.Sistem rekomendasi hotel berdasarkan tempat tujuan dapat membantu dan memudahkan para _traveller_ untuk memesan kamar hotel yang mereka inginkan. Dengan data yang diambil dari web traveloka, proyek ini bertujuan untuk membantu pengguna dalam memilih hotel yang diinginkan.

## _Business Understanding_

Proyek ini berisi pembuatan sistem rekomendasi pada dataset hotel. Sistem akan memberikan rekomendasi kepada _user_ berdasarkan tempat tujuan user.

### _Problem Statements_

Masalah yang akan diselesaikan:
- Metode machine learning apa yang harus digunakan untuk menyelesaikan kasus sistem rekomendasi hotel?

### _Goals_

Tujuan yang ingin dicapai:
- Metode machine learning yang digunakan adalah metode _content based filtering_ karena berdasarkan dataset yang digunakan, sistem akan memberikan rekomendasi hotel sesuai kesamaan tempat tujuan pengguna.

## _Data Understanding_
Dataset yang digunakan pada proyek ini merupakan dataset mengenai Hotel yang ada dibeberapa negara di dunia. Data yang digunakan dibuat dengan menggunakan teknik _web scraping_. Web Scraping merupakan suatu teknik yang digunakan untuk mendapatkan suatu data atau informasi pada suatu website secara otomatis [1].
Berikut beberapa variabel yang terdapat di dalam dataset Hotel Rating:
- _name_ : nama hotel
- _adress_ : alamat hotel
- _country_ : Negara asal hotel
- _impression_ : kesan pelanggan hotel
- _rating_ : penilaian terhadap hotel dari 1-10

Untuk lebih jelasnya data yang terdapat pada dataset tersebut dapat dilihat pada gambar berikut:
![image](https://user-images.githubusercontent.com/62003049/188322470-48878f70-c0b7-44e7-8934-fe927e8b9b21.png)

Untuk melihat info tipe data pada dataset ini dapat dilihat pada gambar berikut:
![image](https://user-images.githubusercontent.com/62003049/188323070-ff0f56f2-ec0c-4bf0-98ff-e8baf42309bc.png)

## _Data Preparation_
Pada proyek ini dilakukan proses _data preparation_ yaitu mengonversi setiap data series menjadi dalam bentuk list pada setiap variabel yang ada pada dataset:
![image](https://user-images.githubusercontent.com/62003049/188323707-61bd5580-847b-4b68-bd6e-318a0e4a8778.png)

Kemudian dilakukan pembuatan dictionary baru dari dataset yang ada:
![image](https://user-images.githubusercontent.com/62003049/188323733-c8604da7-99a7-4ff3-9168-4862f696cbf1.png)

## _Modeling_
Model _Machine Learning_ yang digunakan pada proyek ini _Content-Based_ filtering berdasarkan tempat atau negara hotel tersebut. Langkah - langkah yang dilakukan pada saat pembuatan model tersebut adalah:

- Pertama, kita ubah kategori menjadi angka dengan TfidfVectorizer()
![image](https://user-images.githubusercontent.com/62003049/188323573-54ac2117-c304-435a-9772-952f9ee64847.png)
- Kedua, kita menghitung cosine_similarity dari data hasil TfidfVectorizer()
![image](https://user-images.githubusercontent.com/62003049/188323622-c377d7eb-3b8f-4042-80a5-a603f5af6577.png)
- Ketiga, kita menggabungkan data Cosine dengan nama hotel menjadi satu dataframe
![image](https://user-images.githubusercontent.com/62003049/188323605-0a7b3154-d891-4b04-97ca-2ee55a4ff16e.png)
- Keempat, kita membuat fungsi yang menggunakan nama hotel yang ada di data
![image](https://user-images.githubusercontent.com/62003049/188323640-0fd4227f-832e-4e1d-883b-f0904615768b.png)


## _Evaluation_
Model yang telah dibuat dapat memberikan rekomendasi nama hotel berdasarkan kesamaan tempat ketika user menggunakan nama hotel pada suatu tempat/negara. Namun, data yang dimiliki pada dataset masih sangat terbatas sehingga diperlukan _improve_ atau penambahan jumlah dataset agar lebih bervariasi lagi.

Hasil rekomendasi dapat dilihat pada gambar dibawah ini.

![image](https://user-images.githubusercontent.com/62003049/188322445-d4992dee-5fac-4e73-98f1-10f052683b0a.png)

##Conclusion
Proyek pembuatan Sistem Rekomendasi hotel telah berhasil dibuat, hanya saja dikarenakan dataset yang digunakan merupakan dataset yang dibuat sendiri, sehingga data yang dimiliki masih sedikit dan masih perlu ditambah lagi sehingga kedepannya sistem rekomendasi yang dibuat dapat berdasarkan vaiabel yang lain. 

##Reference
[1] Floresi, V. A., Permatasari, P. A., Jasa, L. (2020). Penerapan Web Scraping Sebagai Media Pencarian dan Menyimpan Artikel Ilmiah Secara Otomatis Berdasarkan Keyword. Majalah Ilmiah Teknologi Elektro, 19(2). 157-162.
