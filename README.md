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
Dataset yang digunakan pada proyek ini merupakan dataset mengenai Hotel yang ada dibeberapa negara di dunia. Data yang digunakan dibuat dengan menggunakan teknik _web scraping_. Web Scraping merupakan suatu teknik yang digunakan untuk mendapatkan suatu data atau informasi pada suatu website secara otomatis [1]. Pada dataset ini berisi 5 kolom dan 138 baris data. [Hotel Dataset Review](https://drive.google.com/file/d/1w9UA2mLMrrX5Z8YCwqiIdZVkYFmwjmqC/view?usp=sharing)

Berikut beberapa variabel yang terdapat di dalam dataset Hotel Rating:
- _name_ : nama hotel
- _adress_ : alamat hotel
- _country_ : Negara asal hotel
- _impression_ : kesan pelanggan hotel
- _rating_ : penilaian terhadap hotel dari 1-10

Untuk lebih jelasnya data yang terdapat pada dataset tersebut dapat dilihat pada gambar berikut:
|index|name|address|country|impression|rating|
|---|---|---|---|---|---|
|0|Mercure Welcome Melbourne|265 Little Bourke Street, Chinatown Melbourne, Melbourne, Victoria, Australia, 3000|Australia|Impressive|8\.6|
|1|Song Hotel Sydney|5-11 Wentworth Avenue, Sydney CBD, Sydney, New South Wales, Australia, 2000|Australia|Impressive|8\.3|
|2|Mercure Melbourne Therry Street|43 Therry Street, Melbourne CBD, Melbourne, Victoria, Australia, 3000|Australia|Impressive|8\.6|
|3|Essence Hotel Carlton|609 Swanston Street, Carlton, Melbourne, Victoria, Australia, 3053|Australia|Impressive|8\.5|
|4|ibis budget Sydney Airport|5 Ross Smith Avenue, Botany Bay, Sydney, New South Wales, Australia, 2020|Australia|Convenient|7\.9|
|5|The Village Melbourne|167 Franklin Street, Melbourne CBD, Melbourne, Victoria, Australia, 3000|Australia|Impressive|8\.4|
|6|Arrow on Swanston|488 Swanston Street, Carlton, Melbourne, Victoria, Australia, 3053|Australia|Impressive|8\.4|
|7|ibis Melbourne Hotel and Apartments|15-21 Therry Street, Melbourne CBD, Melbourne, Victoria, Australia, 3000|Australia|Impressive|8\.6|
|8|ibis Sydney World Square|382 Pitt Street, Sydney CBD, Sydney, New South Wales, Australia, 2000|Australia|Impressive|8\.4|
|9|YEHS Hotel Sydney CBD|88 Liverpool St\., Sydney CBD, Sydney, New South Wales, Australia, 2000|Australia|Impressive|8\.6|
|10|Hilton Sydney|488 George Street, Sydney CBD, Sydney, New South Wales, Australia, 2000|Australia|Impressive|8\.9|

Untuk melihat info tipe data pada dataset ini dapat dilihat pada gambar berikut:
![image](https://user-images.githubusercontent.com/62003049/188323070-ff0f56f2-ec0c-4bf0-98ff-e8baf42309bc.png)

## _Data Preparation_
Pada proyek ini dilakukan proses _data preparation_ yaitu mengonversi setiap data series menjadi dalam bentuk list pada setiap variabel yang ada pada dataset:

![image](https://user-images.githubusercontent.com/62003049/188323707-61bd5580-847b-4b68-bd6e-318a0e4a8778.png)

Kemudian merupakan proses _data cleaning_, data pada dataset dihapus salah satu kolom yang tidak digunakan untuk proses rekomendasi yaitu kolom impresi dengan dilakukan pembuatan dictionary baru dari dataset yang ada:

|index|name|ountries|rating|
|---|---|---|---|
|0|Mercure Welcome Melbourne|Australia|8\.6|
|1|Song Hotel Sydney|Australia|8\.3|
|2|Mercure Melbourne Therry Street|Australia|8\.6|
|3|Essence Hotel Carlton|Australia|8\.5|
|4|ibis budget Sydney Airport|Australia|7\.9|
|5|The Village Melbourne|Australia|8\.4|
|6|Arrow on Swanston|Australia|8\.4|
|7|ibis Melbourne Hotel and Apartments|Australia|8\.6|
|8|ibis Sydney World Square|Australia|8\.4|
|9|YEHS Hotel Sydney CBD|Australia|8\.6|
|10|Hilton Sydney|Australia|8\.9|

## _Modeling_
Model _Machine Learning_ yang digunakan pada proyek ini _Content-Based_ filtering berdasarkan tempat atau negara hotel tersebut. Model dibuat menggunakan perhitungan derajat kesamaan (similarity degree) antar hotel dengan teknik cosine similarity. Langkah - langkah yang dilakukan pada saat pembuatan model tersebut adalah:

- Pertama, kita ubah kategori menjadi angka dengan TfidfVectorizer()
![image](https://user-images.githubusercontent.com/62003049/188323573-54ac2117-c304-435a-9772-952f9ee64847.png)
- Kedua, kita menghitung cosine_similarity dari data hasil TfidfVectorizer()
![image](https://user-images.githubusercontent.com/62003049/188323622-c377d7eb-3b8f-4042-80a5-a603f5af6577.png)
- Ketiga, kita menggabungkan data Cosine dengan nama hotel menjadi satu dataframe
![image](https://user-images.githubusercontent.com/62003049/188323605-0a7b3154-d891-4b04-97ca-2ee55a4ff16e.png)

Dengan cosine similarity, kesamaan antara satu hotel dengan hotel lain telah berhasil diidentifikasi. Shape (138, 138) merupakan ukuran matriks similarity dari data dimiliki. 
Angka 1.0 pada tabel mengindikasikan bahwa hotel pada kolom X (horizontal) memiliki kesamaan dengan hotel pada baris Y (vertikal).

- Keempat, kita membuat fungsi yang menggunakan nama hotel yang ada di data
![image](https://user-images.githubusercontent.com/62003049/188323640-0fd4227f-832e-4e1d-883b-f0904615768b.png)

Hasil rekomendasi yang digunakan merupakan top-N recommendation dapat dilihat pada gambar dibawah ini.

|index|name|ountries|
|---|---|---|
|0|CLARO Kendari|Indonesia|
|1|Whiz Prime Hotel Pajajaran Bogor|Indonesia|
|2|CLARO Makassar|Indonesia|
|3|Starlet Hotel Serpong|Indonesia|
|4|Horison Ultima Bandung|Indonesia|
|5|1O1 URBAN Jakarta Kelapa Gading \(The BnB\)|Indonesia|
|6|Lumire Hotel & Convention Center|Indonesia|
|7|MG Suites Hotel Semarang|Indonesia|
|8|Best Western Premier The Hive|Indonesia|
|9|Red Planet Bekasi|Indonesia|


## _Evaluation_
Model yang telah dibuat dapat memberikan rekomendasi nama hotel berdasarkan kesamaan tempat ketika user menggunakan nama hotel pada suatu tempat/negara. Namun, data yang dimiliki pada dataset masih sangat terbatas sehingga diperlukan _improve_ atau penambahan jumlah dataset agar lebih bervariasi lagi. Berikut ini _metric evaluation_ yang digunakan adalah _precision_  yang dapat dilihat pada gambar dibawah ini.

![image](https://user-images.githubusercontent.com/62003049/188518580-1ddaec29-ef59-4674-8e2a-5df7d06c4186.png)

Dari test dengan nama , program dapat memberikan 10 nama hotel hasil rekomendasi berdasarkan negara yang sama. Presisi yang dihasilkan selama ini adalah 100%, karena 10 nama hotel yang diberikan berada di wilayah yang sama dengan nama hotel yang diinput.

## _Conclusion_
Proyek pembuatan Sistem Rekomendasi hotel telah berhasil dibuat, hanya saja dikarenakan dataset yang digunakan merupakan dataset yang dibuat sendiri, sehingga data yang dimiliki masih sedikit dan masih perlu ditambah lagi sehingga kedepannya sistem rekomendasi yang dibuat dapat berdasarkan vaiabel yang lain. 

## _Reference_
[1] Floresi, V. A., Permatasari, P. A., Jasa, L. (2020). Penerapan Web Scraping Sebagai Media Pencarian dan Menyimpan Artikel Ilmiah Secara Otomatis Berdasarkan Keyword. Majalah Ilmiah Teknologi Elektro, 19(2). 157-162.
