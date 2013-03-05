=============
django-ipaymu
=============

*Note: This documentation is mainly in Indonesian because of this Django App might be useful only for Indonesian Django developer.*

**django-ipaymu** adalah aplikasi Django yang memanfaatkan layanan API Ipaymu supaya bisa diintegrasikan dengan web aplikasi/website yang dibuat menggunakan Django framework.

Aplikasi ini dibuat berdasarkan dokumentasi API Ipaymu berikut ini:

* Dokumentasi API (https://ipaymu.com/dokumentasi-api/)
* Cara Integrasi Webstore – Tingkat Lanjut (https://ipaymu.com/cara-integrasi-webstore-tingkat-lanjut/)

Fitur
-----
**django-ipaymu** dapat dipergunakan untuk melakukkan beberapa hal berikut:

* **Cek Saldo**
  
  Fitur cek saldo ini disediakan dalam bentuk fungsi siap pakai, dengan fungsi ini data saldo bisa di dapatkan hanya dengan menyediakan API key yang disediakan Ipaymu, dan output fungsi ini bisa dimanfaatkan/dirender melalui template sesuai kebutuhan.

* **Cek Transaksi**

  Sama dengan cek saldo, fitur ini juga disediakan dalam bentuk fungsi.

* **Mengintegrasikan sistem pembayaran Ipaymu dan notifikasi pembayaran**

  Fitur ini disediakan dengan cara yang lebih kompleks tetapi tetap fleksibel dan juga powerful. Dengan integrasi ini, akses ke Ipaymu di handle oleh django-ipaymu, pengguna hanya akan berhadapan dengan data hasil transaksi yang bisa diolah sesuai keperluan.

Requirement
-----------

* Django 1.3+
* Requests 1.1.0 (http://docs.python-requests.org/en/latest/)

Instalasi
---------

Sisa dokumentasi ini masih dalam pembuatan, begitu juga dengan **django-ipaymu** yang masih tahap awal development..
