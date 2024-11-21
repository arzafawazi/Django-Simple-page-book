from django.db import models
from django.core.validators import RegexValidator
import uuid

# Model Publisher
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=250)
    alamat = models.TextField(blank=True,null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="min 8 digit")
    telpon = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email = models.EmailField(blank=True,null=True)
    def __str__(self) -> str:
        return self.nama

# Model Book
class Book(models.Model):
    judul = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    pengarang = models.CharField(max_length=250)
    sinopsis = models.TextField(blank=True,null=True) #null = DB, blank = form
    tanggal_rilis = models.DateField()
    jumlah_halaman = models.IntegerField()
    gambar = models.ImageField(upload_to='movie/images/')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.judul
