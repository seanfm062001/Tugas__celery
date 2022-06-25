@http('GET', '/prima/<int:num>')
-berfungsi untuk mencari angka prima ke berapa sebagai contoh prima ke 5 -> 11

@http('GET', '/prima/palindrom/<int:num>')
-berfungsi untuk mencari angka yang prima dan juga palindrom ke index berapa sebagai contoh prima
dan juga palindrom ke 6 --> 101

@http('POST', '/register')
-berfungsi untuk meregister akun dengan format json
{
"username" : "<username>"
"password" : "<password>"
}

@http('GET', '/logout')
-berfungsi untuk menghilangkan session akun 

@http('POST', '/login')
-berfungsi untuk mendapatkan session
{
"username" : "<username>"
"password" : "<password>"
}