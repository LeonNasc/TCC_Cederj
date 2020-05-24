from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

wordlist = ("facemask on person", "labcoat on person", "jaleco hospitalar", "safety glasses on person", "faceshield on person", "óculos segurança laboratório", "máscara n95", "avental tnt pessoa", "disposable labcoat")

for word in wordlist:
    try:
        response().download(word, 100)
    except:
        print("falha no download")
    print("Baixadas 1000 imagens de %s" % word)
