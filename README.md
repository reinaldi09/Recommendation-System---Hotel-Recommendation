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
Pada proyek ini dilakukan proses _data preparation_ yaitu
   Pembagian dataset dengan fungsi train_test_split dari _library_ sklearn Proses pembagian dataset ini bertujuan untuk memisahkan antara data yang akan dilakukan proses training dan data yang akan digunakan untuk pengujian. Tentunya data yang digunakan untuk proses pengujian haruslah data yang belum pernah dilihat oleh model sebelumnya, sehingga proses pemisahan data ini sangat penting.
   
Berikut ini program yang digunakan pada proses splitting data:
   ![image](https://user-images.githubusercontent.com/62003049/187921201-9c296291-28aa-42c0-a01d-cb8dd769b8ff.png)

## _Modeling_
Model _Machine Learning_ yang digunakan pada proyek ini ada 2 jenis algoritma yang akan dibandingkan berdasarkan hasil prediksi masing-masing algoritma. Algoritma yang pertama digunakan adalah algoritma _random forest_ dan algoritma _boosting_.

Pada Algoritma _Random Forest_, parameter yang digunakan adalah sebagai berikut
- n_estimators=25
- max_depth=32
- random_state=16
- n_jobs=-1
Untuk lebih jelasnya dapat dilihat pada cuplikan kode dibawah ini:
![image](https://user-images.githubusercontent.com/62003049/187921844-cf1c7d27-99dd-4cae-a8ee-86bbd6f497a6.png)

Sedangkan pada Algoritma _Boosting_, parameter yang digunakan adalah sebagai berikut
- learning_rate = 0.05
- random_state = 16
Untuk lebih jelasnya dapat dilihat pada cuplikan kode dibawah ini:
![image](https://user-images.githubusercontent.com/62003049/187921949-c2d1929a-f16c-4980-ae0c-d086ec53fa0f.png)

## _Evaluation_
Model yang telah dibuat dapat memprediksi nilai dari kualitas wine yang ada pada dataset. Karena pada proyek kali ini menggunakan 2 jenis algoritma, maka akan dibandingkan hasil prediksi dari masing-masing algoritma. Metrik yang digunakan pada setiap algoritma adalah MSE atau mean squared error.

Mse merupakan metrik yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi. MSE didefinisikan dalam persamaan berikut:

![image](https://user-images.githubusercontent.com/62003049/187825463-410f0055-ac49-4af8-a56b-a5e280e62eda.png)

Keterangan:
N = jumlah dataset
yi = nilai sebenarnya
y_pred = nilai prediksi

![image](https://user-images.githubusercontent.com/62003049/187925940-3528f511-4845-43e1-a1ac-ba94198998ec.png)

Berdasarkan hasil training model, didapatkanlah jumlah error yang paling kecil adalah _Boosting Algorithm_.

##Conclusion
Proyek pembuatan Sistem Rekomendasi hotel telah berhasil dibua, hanya saja dikarenakan dataset yang digunakan merupakan dataset yang dibuat sendiri, sehingga data yang dimiliki masih sedikit dan masih perlu ditambah lagi. Hasil rekomendasi dapat dilihat pada gambar dibawah ini.

![image](https://user-images.githubusercontent.com/62003049/188322445-d4992dee-5fac-4e73-98f1-10f052683b0a.png)

##Reference
[1] Floresi, V. A., Permatasari, P. A., Jasa, L. (2020). Penerapan Web Scraping Sebagai Media Pencarian dan Menyimpan Artikel Ilmiah Secara Otomatis Berdasarkan Keyword. Majalah Ilmiah Teknologi Elektro, 19(2). 157-162.
