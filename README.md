
# Mini-project report 
Members: Eric Brenander, Erik Borgström, Robin Bergvall and Edvinas Andrijaitis  
Program: Software Technology  
Course: 1DV501  
Date of submission: 2021-11-XX

## Introduktion 
Uppgiften som tilldelades gick ut på att i grupp lösa fem uppgifter. Dessa uppgifter innehöll till stor del moment som använts tidigare, men hashning, binära sökträd samt grafer introducerades. Dessa moment var som sagt nya och bidrog till att gruppen fick hjälpas åt för att lösa dom.

Målet med projektet var att lösa de angivna uppgifterna men också få en bättre förstålse för hur man jobbar och samarbetar i en grupp. Ett annat mål med projektet var hur man uttnyttjar och använder gitlab.

# Del 1: Räkna unika ord 1

Textfilen new_holy har 11 080 ord och new_eng har 1 946 691 ord.
Problemet löstes i 3 delar som finns i metoden top_ten(lst).

### Del 1. 
Koden nedan används för att lägga till alla element i den givna listan till ett dictionary som definieras i metoden.
```python
dict_of_words = {}
for x in lst:
    if dict_of_words.get(x) is None:
        dict_of_words[x] = 1
    else:
        dict_of_words[x] += 1
```
### Del 2. 
Dictionary sorteras genom att skapa en lista av tuples. Med lambda sorteras den sedan efter value och genom reverse=True sorteras det från högsta värdet till det lägsta. Sen castar vi tillbaka listan till en dictionary
```python
dict_of_words = dict(sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True))
```
### Del 3. 
Nu när dictionary innehåller alla ord sorterat med det största värdet så ska den filtreras och ta det största värde som har ett ord med mer än 4 karaktärer i en ny dictionary. En ny iteration görs och den kommer löpa så länge den nya dictionary inte har 10 ord i sig. Efter iteration är slut så returneras det nya dictionary
```python
top_words = {}
for key, value in dict_of_words.items():
    if len(top_words) == 10:
        break
    if len(key) > 4:
        top_words[key] = value
```

**Output efter körning:**

| Text filer:   | eng_news_100K-sentences| holy_grail    |
|:-------------:|:----------------------:|:-------------:|
| Unika ord     |               89665 st |       1862 st |
|				|						 |				 |
| Top tio:      | their             6143 | arthur    261 |
|               | about             4606 | launcelot 101 |
|               | there             3926 | knight     84 |
|               | would             3877 | galahad    81 |
|               | people            3799 | father     74 |
|               | which             3571 | bedevere   68 |
|               | after             3014 | knights    65 |
|               | years             2985 | robin      58 |
|               | first             2887 | guard      58 |
|               | other             2754 | right      57 |



# Del 2: Implementera data strukturer
För att lösa uppgift två krävdes en implementering av hashning samt binärt söksystem från ett givet skelett för att kunna bygga olika listor.
För att testköra koden användes en main fil. Denna fil skulle ge en output som agerade kontroll för uppgiften.

## Hashning

### get_hash()
Metoden "get_hash" kalkylerar hashvärdet på elementet som metoden tar emot. Detta använder sedan programmet i olika metoder, exempelvis för att lägga till samt söka upp olika element.
Denna metod tar ascii koden för vardera bokstav i elementet och summerar detta. Summan av detta modulus längden av vårt hashträd("antal buckets") skapar hashvärdet.

```python
def get_hash(self, word):
    value = 0
    for i in word:
        value += ord(i)
    return value % len(self.buckets)
```

### add()
Metoden "add" använder sig av metoden "get_hash". Metoden tar emot elementet, frågar sedan efter värdet för ordet och placerar därefter elementet i rätt "bucket". En bucket är en lista inuti en lista. Metoden kontrollerar då ifall elementet redan existerar i listan eller inte genom metoden "contains". Om elementet inte existerar i korrekt bucket, kollar metoden om antalet element är lika med antalet buckets. Om detta är fallet triggas metoden "rehash" (förklaras nedan) och metoden startar om med samma element som placeras i rätt bucket. Existerar ordet redan så ignoreras elementet.

```python
def add(self, word):

    value = self.get_hash(word)
    if self.contains(word) is False:
        if self.size == len(self.buckets):
            self.rehash()
            self.add(word)
        else:
            self.buckets[value].append(word)
            self.size += 1
```

### rehash()
Rehash metoden är en grundläggande del av programmet och används när antalet element överskrider mängden buckets. Detta för att åstadkomma en jämn fördelning av elementen mellan de olika bucketsarna. Anledningen till den jämna fördelningen är för att korta ner tiden det tar att hitta element när man söker i hashningen. Metoden fungerar genom att kopiera den gamla listan och lägga till dessa element till en ny lista med dubbelt så många buckets via metoden "add". När detta görs kommer elementet att få ett nytt hashvärde och därav placeras in i en ny bucket.

```python
def rehash(self):
    l1 = self.buckets
    self.buckets = [[] for x in range(0, len(self.buckets) * 2)]
    self.size = 0
    for i in l1:
        for word in i:
            self.add(word)
```

### hash.main
Resultatet enligt kommentarerna av hash.main skiljde sig från gruppens resulat i avseendet att elementen placerades i en annan ordning. Detta sker troligtvis pågrund av olika tillvägagångsätt vid kalkylering av hashvärde.

## Binärt söksystem

### put() 

Denna metod gör flera kontroller. Först kontrollerar den om den givna key är densamma som nodens den är på. Om den är samma tilldelas noden den givna valuen. Annars så är det inte rätt nod, då jämförs ifall key är mindre eller större än nodens key. Senare kollar noden om sitt barn antingen åt vänster eller höger finns. Om den finns så anropar man barnets put med samma key och value, om barnet inte finns så skapas en ny nod med angivna key och value.

```python
def put(self, key, value):
    if key == self.key:
        self.value = value
    elif key < self.key:
        if self.left is None:
            self.left = Node(key, value)
        else:
            self.left.put(key, value)
    elif key > self.key:
        if self.right is None:
            self.right = Node(key, value)
        else:
            self.right.put(key, value)
```
### max_depth() 

Denna metod kontrollerar ifall den nuvvarande noden har barn, ifall den har barn så kör den barnets max_depth() och sparar det returnerade värdet. Den jämför med var barns returnerade värde och returnerar själv det största plus 1 då den räknar med sig själv. Viktigt att notera är att barnen kommer kontrollera sina barns max_depth() osv tills inga fler barn finns.

```python
def max_depth(self):
    left = 0
    right = 0
    if self.left is not None:
        left = self.left.max_depth()
    if self.right is not None:
        right = self.right.max_depth()

    if left > right:
        return left + 1
    else:
        return right + 1
```
### bst_main
Den mest märkbara skillnaden i bst_main är to_string metoden, den returnerar en sträng i detta formatet: "{ (Zoe,41) }". Det gick inte att hitta en lösning att returnera tuples på detta sätt då det istället blev: "{ (Zoe, 41) }". För att lösa detta så returneras ingen tuple från noderna, istället adderas värderna till en sträng och () läggs till i samma sträng.

# Del 3: Räkna unika ord 2

Del 3 var i princip samma uppgift som den första men här användes istället hashningen och det binära sökrädet.  
Båda filerna matades in, med hashningen beräknade vi hur många unika ord det var via get_Size()-metoden och via det binära sökträdet hittade vi top tio orden med fler än fyra bokstäver.

**Output efter körning:**

| Text filer:   | eng_news_100K-sentences| holy_grail    |
|:-------------:|:----------------------:|:-------------:|
| Unika ord     |               89665 st |       1862 st |
|				|						 |				 |
| Top tio:      | their             6143 | arthur    261 |
|               | about             4606 | launcelot 101 |
|               | there             3926 | knight     84 |
|               | would             3877 | galahad    81 |
|               | people            3799 | father     74 |
|               | which             3571 | bedevere   68 |
|               | after             3014 | knights    65 |
|               | years             2985 | robin      58 |
|               | first             2887 | guard      58 |
|               | other             2754 | right      57 |

**Max bucket size och Max depth:**

| Text filer:   | eng_news_100K-sentences| holy_grail    |
|:-------------:|:----------------------:|:-------------:|
| Max bucket size:| 320 | 17 |
| Max depth:| 43 | 24 |

# Del 4: Grafritning

### Word count vs Word length
Här användes programmet för att skapa ett binärt sökträd. För varje element kollade programmet hur långt elementet är (i detta fall bokstäver) och tilldelar sedan elementet en plats i det binära sökträdet. Om ett element hittas med samma mängd ökades värdet på value i noden. På detta sätt kan sedan programmet bygga en sorterad lista med antal element med en viss mängd bokstäver. Gruppen gjorde ett val att endast visa element som hade upp till 20 bokstäver för att sålla ut länkar med mera men också för att man lättare ska se skillnaderna i grafen.  
  
**Observera att denna graf räknar med alla ord och inte bara de unika.**

```python
lst_of_length = [str(len(x)) for x in lst_eng]
bst_map = fnc.create_bst(lst_of_length)
sorted_lst = fnc.sort_lst_of_tuples(bst_map.as_list(), "key")
```

<p align="center">
<a href="https://imgbb.com/"><img src="https://i.ibb.co/8dk7jZB/Word-count-vs-word-lenght.png" alt="Word count vs word lenght" border="0"></a>
</p>

> *Resultatet visar oss att ord med 2-4 bokstäver används som mest i text-filen.*

### Added words vs Unique words
Här användes programmet för att skapa en hash-lista. En txt-fil med cirka 2-miljoner ord matas in och hash-listan tilldelar en plats för varje unikt element. Programmet gör även två nya listor där den räknar hur många element via metoden get_size() har lagts till vid varje loop. Utöver detta skapas också en lista där programmet räknar varje ord metoden add() har försökt att lägga till.

```python
for key, x in enumerate(lst_eng):
    lst_attempts.append(key + 1)
    words.add(x)
    lst_current_size.append(words.get_size())
```

<p align="center">
<a href="https://imgbb.com/"><img src="https://i.ibb.co/Wf23ncm/Added-words-vs-unique-words.png" alt="Added words vs unique words" border="0"></a>
</p>

> *Resultatet är som väntat, för varje unikt element hash-listan la till desto svårare var det att hitta unika element och grafen började plana ut.*

# Del 5: Mäta tid

## bst_time

För att se skillnaden på söktid beroende på trädets storlek är det viktigt att trädet är i en bestämd storlek vid varje test. För att åstadkomma detta skapas en lista med unika ord innan testet genomfördes. Självaste testet görs i en iteration. Innan iterationen läggs ord till i trädet till den storleken som är intressant för testet. I varje test kommer hela listan av unika ord att användas och mängden iterationer som görs beslutar hur många av ord från listan som plockas ut. Detta betyder att om det ska ske fem iterationer kommer det tas en femtedel ord av listan vid varje iteration. Sedan när testet görs så testar man med de orden man har lagt till. Genom att göra så säkerställer vi att varje ord vi testar så kommer man söka djupare och djupare i trädet.


<p align="center">
<a href="https://ibb.co/DQMB2cr"><img src="https://i.ibb.co/jDwCX0J/BST-Time-Graphs.png" alt="BST-Time-Graphs" border="0"></a>
</p>

> *Här ser vi att desto större trädet blir desto längre tid tar det att söka efter vissa element, däremot halveras sökningen vid varje nod vilket kan göra att det kan gå lite snabbare vid större träd.*   
*Desto större trädet blir desto mindre ökar djupet.*

## hash_time

Programmet hash_time börjar med att skapa en unik lista av tuples. Därefter utförs testet i en for loop och där bestäms hur många gånger vi vill testa att lägga till element. Varje gång vi kör testet använder vi en lista med unika element. Om vi exempelvis väljer att köra testet tio gånger så delar vi listan med unika element på tio. Efter varje iteration adderas en tiondel av listans element till hashsettet vilket gör att man kan åskadligöra hur lång tid det tar att lägga till olika mängder element. Något värt att notera är att det i början kommer göras väldigt många rehashningar. Detta syns dock inte på grafen då det fortfarande går väldigt snabbt, detta då mängden element är väldigt få. Rehashningarna blir alltså tydligare desto fler element som lagts till i hashsettet.

<p align="center">
<a href="https://ibb.co/5jyZHm7"><img src="https://i.ibb.co/rpS9rYW/Sk-rmbild-2021-11-04-164105.png" alt="Sk-rmbild-2021-11-04-164105" border="0"></a>
</p>

> *Spikarna som vi ser i vänstra trädet visar som förväntat att det är själva rehashingen som tar tid.*   
*Vi ser i högra grafen att bucketsizen ökar kraftigt i början tills hashingen rehashar sig själv och skapar därav fler buckets att sortera i, till slut planar den ut.*

## Slutsats och det vi har lärt oss

### Tekniska problem och utmaningar 

Tekniska problem vi stötte på under projekt var relativt få. Det mesta flöt på bra och detta tack vare live share men också ett bra samarbete och en stark kommunikation. Uppgiften som var mest tidskrävande var uppgift fyra. Detta berodde till stor del på en otydlig uppgiftsbeskrivning men också andra diverse problem. Exempel på det här är olika buggar, okonsekventa grafer med mera.

Några saker vi kunde gjort annorlunda är att planera uppgiften som helhet först för att sedan attackera de individuella problemen och börja koda. Men också att komma överens om vad problemet faktiskt är innan vi diskuterade hur vi skulle lösa problemen. Helt enkelt en bättre planering kring hur problemen skulle lösas.
 
Om de funntis mer tid i projektet så kunde detta läggas på att göra graferna snyggare. Detta i form av bibliotek som jämnar ut linjerna och får det att se mer estetiskt tilltalande. Mer tid hade också skapat möjlighet för mer optimering av koden, både ur tidaspekt men också i längd.

### Projekt utmaningar
Gruppen talades vid varje kväll vid 18.00 för att gå igenom vad alla utfört under dagen samt om det fanns frågor eller om någon kört fast. Kommunikation ansåg vi var viktigt och på de dagliga mötena förklarade alla parter deras ändringar så alla var insatta och förstådda i koden.  

För att kommunicera användes Discord och det var även denna platform där de uppdaterade versionerna av filerna överfördes innan repositaryt på gitlab sattes upp. Då vi var klara med alla uppgifter innan repositarit lades upp på gitlab så användes inte denna platform till någon större grad.
Gruppen använde sig flitigt av visual studios plugin live share. Detta för att programmera tillsammans i realtid medans vi diskuterade via Discord eller på plats.   
