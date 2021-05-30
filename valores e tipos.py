Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10
10
>>> 5 / 2
2.5
>>> 
>>> type(10)
<class 'int'>
>>> type(5 / 2)
<class 'float'>
>>> 
>>> 10 / 3
3.3333333333333335
>>> 
>>> 10 // 3
3
>>> 10 % 3
1
>>> 
>>> peso = 78
>>> altura = 1.83
>>> IMC = peso / (altura ** 2)
>>> IMC
23.291229956104985
>>> 
>>> 
>>> IMCInteiro = int(IMC)
>>> 
>>> IMCInteiro
23
>>> 
>>> 
>>> 
>>> texto = "Bom dia, tudo bem?"
>>> 
>>> len(texto)
18
>>> len(IMC)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    len(IMC)
TypeError: object of type 'float' has no len()
>>> len(str(IMC))
18
>>> 
>>> 
>>> temp = str(texto)
>>> 
>>> temp
'Bom dia, tudo bem?'
>>> len(temp)
18
>>> 