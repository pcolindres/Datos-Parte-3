import pandas as pd

# Parte 3: Calculando analíticas simples

#Continuando con el DataFrame con todos los datos de la anterior subsección, ahora debes:

#Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas
#numéricas en formato de cadena).

#Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).

data = Dataset({
    'features': [
        'age',
        'has_anaemia',
        'creatinine_phosphokinase_concentration_in_blood',
        'has_diabetes',
        'heart_ejection_fraction',
        'has_high_blood_pressure',
        'platelets_concentration_in_blood',
        'serum_creatinine_concentration_in_blood', 
        'serum_sodium_concentration_in_blood',
        'is_male', 'is_smoker',
        'days_in_study',
        'is_dead'
    ],
    'num_rows': 299
})

# Convertir el objeto Dataset a un DataFrame de Pandas
df = pd.DataFrame(data)

# Verificar tipos de datos en cada columna
tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

# Calcular la cantidad de hombres fumadores y mujeres fumadoras
cantidad_hombres_fumadores = df[df['is_male'] == 1]['is_smoker'].sum()
cantidad_mujeres_fumadoras = df[df['is_male'] == 0]['is_smoker'].sum()

# Imprimir los resultados
print("Cantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)