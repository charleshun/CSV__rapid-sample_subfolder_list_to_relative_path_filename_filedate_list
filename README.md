#Gyorsan listázza ki nagy ZIP fájlok tartalmát kicsomagolás nélkül.

## python list_zip.py your_file.zip

#CSV fájl a következő oszlopokkal:

filename+relative_path	Fájlnév és relative elérési út
filename	            Fájlnév
subdirectorys	        Szülőkönyvtárak (relatív elérési út)
size_bytes	            Méret (byte)
datetime                Fájl dátuma konvertálva datetime sítlusban
is_directory	        Könyvtár-e (True/False)

#Előnyök
- Gyors, nem csomagolja ki
- Kis memória
- CSV kimenet "> list.csv"

#Követelmények
-python 3.6+