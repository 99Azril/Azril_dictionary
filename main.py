meme_dict = {
            "KEJU": "Makanan yang terbuat dari susu",
            "TEMPE": "Makanan yang terbuat dari kedelai",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print("arti kata", word, "adalah", meme_dict[word])
else:
    print("kata tidak ditemukan")
