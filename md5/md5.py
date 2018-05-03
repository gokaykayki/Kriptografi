from hashlib import md5


def get_file():        # Dosya okuma fonksiyonu
    with open('text.txt', 'r') as f:  # !!! Belge ismini buradan düzenleyin 
        text = f.read()
        print("--- Başlangıç metni---\n\n{}\n\n".format(text))
        return text


def hashing(text):        # md5 fonksiyonu
    return md5(text).hexdigest()


def main():
    num_list = []
    hex_list = []
    strng = ''

    n = input('Times?: ')   # döngü sayısını al
    text = get_file()

    for i in range(0, int(n)):
        hash_string = hashing(text.encode('utf-8'))
        num_list.append(int(hash_string[6], 16))     # 7. karakteri listeye ekle (16'lık tabanda ise 10'luk tabana çevirir)
        hex_list.append(hash_string[6])
        strng += hash_string[6]
        text = hash_string         # Hash değerimiz yeni text metnimiz oluyor

    print("7. karakterlerin 16'lık tabandaki listesi: {}".format(hex_list))
    print("Karakterlerin 10'luk tabana çevrilmiş listesi: {}".format(num_list))
    print("\n16'lık tabanda oluşturulan sayı: {}".format(strng))
    print("16'lık tabanda oluşturulan sayının 10'luk tabana çevrilmiş hali: {}".format(int(strng, 16)))


if __name__ == "__main__":
    main()
