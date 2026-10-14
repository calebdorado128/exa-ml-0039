# Reporte de Análisis de Datos - Pandas

`Caleb Dorado Machine Learning pandas, NC = 0039`

## 1. DataFrame Convertido
```text
      Deporte  Jugadores  Duracion_min
0      Fútbol         11            90
1  Básquetbol          5            48
2       Tenis          2           120
3    Natación          1            60
4    Voleibol          6            90
5     Béisbol          9           108
```

## 2.1 Primeras Filas (head)
```text
      Deporte  Jugadores  Duracion_min
0      Fútbol         11            90
1  Básquetbol          5            48
```

## 2.2 Últimas Filas (tail)
```text
    Deporte  Jugadores  Duracion_min
4  Voleibol          6            90
5   Béisbol          9           108
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Deporte           str
Jugadores       int64
Duracion_min    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   Deporte       6 non-null      str  
 1   Jugadores     6 non-null      int64
 2   Duracion_min  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Duracion_min'
```text
count      6.000000
mean      86.000000
std       27.539063
min       48.000000
25%       67.500000
50%       90.000000
75%      103.500000
max      120.000000
Name: Duracion_min, dtype: float64
```

## 4. Ordenar Ascendente por Precio
```text
      Deporte  Jugadores  Duracion_min
1  Básquetbol          5            48
3    Natación          1            60
0      Fútbol         11            90
4    Voleibol          6            90
5     Béisbol          9           108
2       Tenis          2           120
```

## 5. Ordenar Descendente por Jugadores
```text
      Deporte  Jugadores  Duracion_min
0      Fútbol         11            90
5     Béisbol          9           108
4    Voleibol          6            90
1  Básquetbol          5            48
2       Tenis          2           120
3    Natación          1            60
```

`Caleb Dorado Machine Learning pandas, NC = 0039`