XOR шифрование
http://kmb.ufoctf.ru/crypto/xor/main.html

f(s, key) = s' 
f(s', key) = s

Ключ шифрования нам известен
Нужно было просто произвести обратные действия 
Прочитать зашифрованный файл(s') -> xor_str(s', key) -> получить исходный файл
Утилита file подсказала, что это:
solve: PC bitmap, Windows 3.x format, 1360 x 307 x 24
А значит файл нужно открыть в просмотрщик изображений 

Для того, чтобы ваша ОСь понимала это можно добавить расширение .bmp 

Школа кибербезопасности в вк:
https://vk.com/getcybber

Youtube канал:
https://www.youtube.com/channel/UC7Oi6wWHvhzhfkmgsXnriHw?view_as=subscriber

