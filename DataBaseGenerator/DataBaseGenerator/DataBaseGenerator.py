import cx_Oracle
import random

cx_Oracle.init_oracle_client(lib_dir=r"C:\Studia\Semestr6\Aplikacje Bazodanowe\Zadanie2\instantclient_19_10")
#dsn_tns = cx_Oracle.makedsn('redactedip', 'redactedport', 'orcltp')
#conn = cx_Oracle.connect("redactedlogin", "redactedpassword", dsn_tns, encoding="UTF-8")

f = open("Inserts.txt", "a")

cur = conn.cursor()
#getting max id value
def getMaxIDValue(tableName):
    max_id = cur.execute("SELECT MAX(ID_"+tableName+") FROM "+ tableName)
    row = cur.fetchone()

    if row[0]==None:
        return(1)
    else:
        return(row[0]+1)

def getMaxIDValueV2():
    max_id = cur.execute("SELECT MAX(lekarstwo_id_lekarstwo) FROM recepta_lekarstwo")
    row = cur.fetchone()

    if row[0]==None:
        return(1)
    else:
        return(row[0]+1)

def randomizeList(minValue, maxValue, data_list):
    list =""
    amount=random.randint(minValue, maxValue)
    if amount<0: amount=0
    for j in range(amount):
        list = list + random.choice(data_list)
        if(j!=amount-1):
            list = list +", "
    return list

def randomDate(minYear,maxYear):
    year=random.randint(minYear,maxYear)
    month=random.randint(1,12)
    day=random.randint(1,28)
    date=str(day)+"/"+str(month)+"/"+str(year)
    return date

def getPesel(date):
    
    day=(int)(date.split('/')[0])
    month=(int)(date.split('/')[1])
    year=(int)(date.split('/')[2])
    strDay=str(day)
    strMonth=str(month)
    strYear=str(year)
    pesel=strYear[2]+strYear[3]+strMonth+strDay+str(random.randint(10000,99999))
    return pesel

#kartoteka
uczulenia_list=["DWUTLENEK SIARKI","JAJKA","ŁUBIN","MIĘCZAKI","MLEKO","MUSZTARDA","ORZECHY","ORZECHY ZIEMNE (Archaidowe)","RYBY","SELER","SKORUPIAKI","SOJA","ZBOŻA ZAWIERAJĄCE GLUTEN","ZIARNA SEZAMU"]
brane_leki_list=["Adavin","Afugin","Allopurynol","Apo-Indap","Relanium","Indix Combi","Opacorden","Opokan forte","Optilamid","Orilukast","Orungal","Tamoxifen Sandoz","Tamsudil","Tanyz"]
choroby_przeszle_list=["Choroba Cushinga","Zespół IgM","Agorafobia","Depresja","Amyloidoza","Choroby wątroby","Zapalenie dróg żółciowych","Zespół Hornera","Jęczmyk","Demencja pourazowa","Zespół ogona końskiego","Ból ucha"]
choroby_przewlekle_list=["Otyłość", "Cukrzyca", "Osteoporoza", "Padaczka","Przewlekła choroba nerek", "Nadciśnienie tętnicze","Udar mózgu","Astma" ]

index_kartoteka=getMaxIDValue("KARTOTEKA")
sql_insert = """ INSERT INTO kartoteka VALUES(:1,:2,:3,:4,:5) """
kartoteka_data = []
#filling array array with data
for i in range(index_kartoteka, index_kartoteka+100):
    uczulenia=randomizeList(-2, 3, uczulenia_list)
    brane_leki=randomizeList(-3, 3, brane_leki_list)
    choroby_przeszle=randomizeList(-6, 2, choroby_przeszle_list)
    choroby_przewlekle=randomizeList(-7, 1, choroby_przewlekle_list)

    kartoteka_data.append((i,uczulenia, brane_leki, choroby_przeszle, choroby_przewlekle))
    f.write(f'INSERT INTO kartoteka VALUES({i},\'{uczulenia}\',\'{brane_leki}\',\'{choroby_przeszle}\',\'{choroby_przewlekle}\');\n')

#executing insert
cur.executemany(sql_insert, kartoteka_data)
print('INSERT CREATED')

#lekarstwo
nazwa_list=["Adavin","Afugin","Allopurynol","Apo-Indap","Relanium","Indix Combi","Opacorden","Opokan forte","Optilamid","Orilukast","Orungal","Tamoxifen Sandoz","Tamsudil","Tanyz"]
koszt_list=[59.99,19.99,79.99,14.99,120.59,34.99,24.99]
zastosowanie_list=["Wcierać w okolice obrzęku", "Jedną kroplę do każdego ucha do trzech razy dziennie", "Jedną tabletkę po każdym posiłku", "Dużą łyżkę po każdym posiłku"]
przeciwwskazania_list=["Nie dla kobiet w ciąży", "Nie zażywać po spożyciu alkoholu", "Nie dla dzieci poniżej 3 lat", "Tylko dla dorosłych"]

index_lekarstwo=getMaxIDValue("LEKARSTWO")
sql_insert = """ INSERT INTO lekarstwo VALUES(:1,:2,:3,:4,:5) """
lekarstwo_data = []

for i in range(index_lekarstwo, index_lekarstwo+100):
    nazwa=randomizeList(1, 1, nazwa_list)
    koszt=random.choice(koszt_list);
    zastosowanie=randomizeList(1, 1, zastosowanie_list)
    przeciwwskazania=randomizeList(1, 1, przeciwwskazania_list)
    lekarstwo_data.append((i,nazwa, koszt, zastosowanie, przeciwwskazania))
    f.write(f'INSERT INTO lekarstwo VALUES({i},\'{nazwa}\',{koszt},\'{zastosowanie}\',\'{przeciwwskazania}\');\n')

#executing insert
cur.executemany(sql_insert, lekarstwo_data)
print('INSERT CREATED')






#pacjent
imie_list=['Jan', 'Janusz', 'Adam', 'Wojciech', 'Jakub', 'Emilia', 'Lukasz', 'Wiktor', 'Zenon', 'Dawid', 'Kamil', 'Piotr']
nazwisko_list=['Nowak', 'Wilk', 'Fronczak', 'Kowalski', 'Adamowski', 'Froda', 'Gradys', 'Nowakowski', 'Nowy', 'Jagoda']
mail_list=["gmail.com","wp.pl","outlook.com"]

index_pacjent=getMaxIDValue("PACJENT")
sql_insert = """ INSERT INTO pacjent VALUES(:1,:2,:3,:4,to_date(:5, 'DD/MM/YYYY'),:6,:7,:8) """
pacjent_data = []

for i in range(index_pacjent, index_pacjent+100):
    imie=randomizeList(1, 1, imie_list)
    nazwisko=randomizeList(1, 1, nazwisko_list)
    data_urodzenia=randomDate(1930,2004)
    pesel=getPesel(data_urodzenia)
    telefon = f'{random.randint(100,999)}{random.randint(100,999)}{random.randint(100,999)}'
    email=f'{imie}.{nazwisko}{random.randint(1,10)}@{random.choice(mail_list)}'
    kartoteka=i

    pacjent_data.append((i,imie, nazwisko, pesel, data_urodzenia, telefon, email, kartoteka))
    f.write(f'INSERT INTO pacjent VALUES({i},\'{imie}\',\'{nazwisko}\',\'{pesel}\',TO_DATE(\'{data_urodzenia}\',\'DD/MM/YYYY\'),\'{telefon}\',\'{email}\',{kartoteka});\n')
    
print(pacjent_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, pacjent_data)
print('INSERT CREATED')

#stanowisko
tytul_list=["Doktor","Fizjoterapeuta", "Masażysta","Stażysta","Recepcjonista","Asystent"]

index_stanowisko=getMaxIDValue("stanowisko")
sql_insert = """ INSERT INTO stanowisko VALUES(:1,:2,:3) """
stanowisko_data = []

for i in range(index_stanowisko, index_stanowisko+100):
    tytul=randomizeList(1, 1, tytul_list)
    pensja=random.randint(3200,8500)

    stanowisko_data.append((i,tytul, pensja))
    f.write(f'INSERT INTO stanowisko VALUES({i},\'{tytul}\',{pensja});\n')
    
print(stanowisko_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, stanowisko_data)
print('INSERT CREATED')


#pracownik
imie_list=["Jan", "Janusz", "Adam", "Wojciech", "Jakub", "Emilia", "Lukasz", "Wiktor", "Zenon", "Dawid", "Kamil", "Piotr"]
nazwisko_list=["Nowak", "Wilk", "Fronczak", "Kowalski", "Adamowski", "Froda", "Gradys", "Nowakowski", "Nowy", "Jagoda"]
mail_list=["gmail.com","wp.pl","outlook.com"]

index_pracownik=getMaxIDValue("pracownik")
sql_insert = """ INSERT INTO pracownik VALUES(:1,:2,:3,:4,:5,to_date(:6, 'DD/MM/YYYY'),to_date(:7, 'DD/MM/YYYY'),:8) """
pracownik_data = []

for i in range(index_pracownik, index_pracownik+100):
    zatrudniony = True
    imie=randomizeList(1, 1, imie_list)
    nazwisko=randomizeList(1, 1, nazwisko_list)
    telefon = f'{random.randint(100,999)}{random.randint(100,999)}{random.randint(100,999)}'
    data_urodzenia=randomDate(1930,2004)
    pesel=getPesel(data_urodzenia)
    data_zatrudnienia=randomDate(2010,2018)
    if random.randint(1,15) == 1:
        data_zwolnienia = randomDate(2018,2020)
        zatrudniony=False
    else: 
        data_zwolnienia = ''
    stanowisko=i

    pracownik_data.append((i,imie, nazwisko, telefon, pesel, data_zatrudnienia, data_zwolnienia, stanowisko))

    if zatrudniony == True: f.write(f'INSERT INTO pracownik VALUES({i},\'{imie}\',\'{nazwisko}\',\'{telefon}\',\'{pesel}\',TO_DATE(\'{data_zatrudnienia}\',\'DD\MM\YYYY\'),null,{kartoteka});\n')
    else:f.write(f'INSERT INTO pracownik VALUES({i},\'{imie}\',\'{nazwisko}\',\'{telefon}\',\'{pesel}\',TO_DATE(\'{data_zatrudnienia}\',\'DD\MM\YYYY\'),TO_DATE(\'{data_zatrudnienia}\',\'DD\MM\YYYY\'),{kartoteka});\n')
    
print(pracownik_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, pracownik_data)
print('INSERT CREATED')

def generateRecepta(amount):
    #recepta
    index_recepta=getMaxIDValue("recepta")
    sql_insert = """ INSERT INTO recepta VALUES(:1,to_date(:2, 'DD/MM/YYYY')) """
    recepta_data = []

    for i in range(index_recepta, index_recepta+amount):
        data_waznosci=randomDate(2022,2035)

        recepta_data.append((i,data_waznosci))

        f.write(f'INSERT INTO recepta VALUES({i},to_date(\'{data_waznosci}\', \'DD/MM/YYYY\'));\n')

    #executing insert
    cur.executemany(sql_insert, recepta_data)
    return index_recepta

#recepta
index_recepta=getMaxIDValue("recepta")
sql_insert = """ INSERT INTO recepta VALUES(:1,to_date(:2, 'DD/MM/YYYY')) """
recepta_data = []

for i in range(index_recepta, index_recepta+100):
    data_waznosci=randomDate(2022,2035)

    recepta_data.append((i,data_waznosci))

    f.write(f'INSERT INTO recepta VALUES({i},to_date(\'{data_waznosci}\', \'DD/MM/YYYY\'));\n')
    
print(recepta_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, recepta_data)
print('INSERT CREATED')


#recepta_lekarstwo
index_recepta_lekarstwo=getMaxIDValueV2()
sql_insert = """ INSERT INTO recepta_lekarstwo VALUES(:1,:2) """
recepta_lekarstwo_data = []

for i in range(index_recepta_lekarstwo, index_recepta_lekarstwo+100):
    recepta_lekarstwo_data.append((i,i))
    f.write(f'INSERT INTO recepta_lekarstwo VALUES({i},{i});\n')
    
print(recepta_lekarstwo_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, recepta_lekarstwo_data)
print('INSERT CREATED')

#zabieg
nazwa_zabieg_list=["Cwiczenia fizyczne", "Ultradźwięki", "Prądy interferencyjne", "Krioterapia", "Pole magnetyczne"]
czas_list=["00:15", "00:30","00:45","01:00","01:30"]
opis_list=["Wymagany brak metalowych przedmiotów", "Oddziaływanie poprzez skórę na głębiej położone struktury ciała", "Lecznicze wykorzystanie wzajemnego nakładania się fal prądów", "Zastosowanie temperatur poniżej 0°C w celu zimnolecznictwa"]

index_zabieg=getMaxIDValue("zabieg")
sql_insert = """ INSERT INTO zabieg VALUES(:1,:2,:3,TO_DATE(:4, 'HH24:MI'),:5) """
zabieg_data = []

for i in range(index_zabieg, index_zabieg+100):
    nazwa_zabieg=randomizeList(1,1,nazwa_zabieg_list)
    koszt=random.choice(koszt_list)
    czas=random.choice(czas_list)
    opis=randomizeList(0,1,opis_list)

    zabieg_data.append((i,nazwa_zabieg,koszt,czas,opis))

    f.write(f'INSERT INTO zabieg VALUES({i},\'{nazwa_zabieg}\',{koszt},TO_DATE(\'{czas}\', \'HH24:MI\'),\'{opis}\');\n')
    
print(zabieg_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, zabieg_data)
print('INSERT CREATED')




#sala
wyposazenie_list=["Stół rehabilitacyjny", "Drabinki rehabilitacyjne", "Materace gimnastyczne","Kabina do ćwiczeń i zawieszeń", "Stół do ćwiczeń manualnych ręki","Lampa terapeutyczna IR raz UV","Zestaw do magnetoterapii","Zestaw do ultradźwięków"]
index_sala=getMaxIDValue("sala")
sql_insert = """ INSERT INTO sala VALUES(:1,:2,:3) """
sala_data = []

for i in range(index_sala, index_sala+100):
    numer_sali=random.randint(1,400)
    wyposazenie=randomizeList(1,1,wyposazenie_list)
    sala_data.append((i,numer_sali,wyposazenie))

    f.write(f'INSERT INTO sala VALUES({i},{numer_sali},\'{wyposazenie}\');\n')
    
print(sala_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, sala_data)
print('INSERT CREATED')


#wizyta
czas_pracy_list=["13:15", "12:30","15:45","16:00","17:30"]
index_wizyta=getMaxIDValue("wizyta")
index_pacjent=getMaxIDValue("pacjent")
index_pracownik=getMaxIDValue("pracownik")
index_zabieg=getMaxIDValue("zabieg")
index_recepta_old=getMaxIDValue("recepta")-100
index_sala=getMaxIDValue("sala")
sql_insert = """ INSERT INTO wizyta VALUES(:1,to_date(:2, 'dd/mm/yyyy hh24:mi'),:3,:4,:5,:6,:7) """
wizyta_data = []

for i in range(index_wizyta, index_wizyta+100):
    data_wizyta=randomDate(2007,2030)
    czas=random.choice(czas_pracy_list)
    data_wizyta=data_wizyta+" "+czas
    pacjent_id=random.randint(1,index_pacjent-1)
    pracownik_id=random.randint(1,index_pracownik-1)
    zabieg_id=random.randint(1,index_zabieg-1)
    
    #recepta_id=generateRecepta(1)
    recepta_id=index_recepta_old+i-1;
    sala_id=random.randint(1,index_sala-1)

    wizyta_data.append((i,data_wizyta,pacjent_id,pracownik_id,zabieg_id,i,sala_id))
    f.write(f'INSERT INTO wizyta VALUES({i},to_date(\'{data_wizyta}\', \'dd/mm/yyyy hh24:mi\'),{pacjent_id},{pracownik_id},{zabieg_id},{i},{sala_id});\n')
    
print(wizyta_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, wizyta_data)
print('INSERT CREATED')

conn.commit()

input("Press Enter to insert 1000")

#wizyta x1000
czas_pracy_list=["13:15", "12:30","15:45","16:00","17:30"]
index_wizyta=getMaxIDValue("wizyta")
index_pacjent=getMaxIDValue("pacjent")
index_pracownik=getMaxIDValue("pracownik")
index_zabieg=getMaxIDValue("zabieg")
index_recepta_old=getMaxIDValue("recepta")-100
index_sala=getMaxIDValue("sala")
sql_insert = """ INSERT INTO wizyta VALUES(:1,to_date(:2, 'dd/mm/yyyy hh24:mi'),:3,:4,:5,:6,:7) """
wizyta_data = []

recepta_id=generateRecepta(1000)
for i in range(index_wizyta, index_wizyta+1000):
    data_wizyta=randomDate(2007,2030)
    czas=random.choice(czas_pracy_list)
    data_wizyta=data_wizyta+" "+czas
    pacjent_id=random.randint(1,index_pacjent-1)
    pracownik_id=random.randint(1,index_pracownik-1)
    zabieg_id=random.randint(1,index_zabieg-1)
    
    #recepta_id=generateRecepta(1)
    recepta_id=index_recepta_old+i-1;
    sala_id=random.randint(1,index_sala-1)

    wizyta_data.append((i,data_wizyta,pacjent_id,pracownik_id,zabieg_id,i,sala_id))
    f.write(f'INSERT INTO wizyta VALUES({i},to_date(\'{data_wizyta}\', \'dd/mm/yyyy hh24:mi\'),{pacjent_id},{pracownik_id},{zabieg_id},{i},{sala_id});\n')
    
print(wizyta_data, "\n", sep='\n')

#executing insert
cur.executemany(sql_insert, wizyta_data)
print('INSERT CREATED')

conn.commit()
