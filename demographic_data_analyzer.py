import pandas as pd

def calculate_demographic_data(print_data=True):
    # 1. Carga del conjunto de datos censales
    df = pd.read_csv('adult.data.csv')

    # 2. Distribución de observaciones por categoría racial
    race_count = df['race'].value_counts()

    # 3. Estimación de la media muestral de edad en la población masculina
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 4. Proporción de individuos con grado académico (Bachelors)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 5. Segmentación por nivel de instrucción formal
    advanced_degrees = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df['education'].isin(advanced_degrees)
    lower_education = ~higher_education

    # Tasas relativas de ingresos superiores al umbral (>50K)
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Límite inferior de carga horaria semanal
    min_work_hours = df['hours-per-week'].min()

    # 7. Proporción de ingresos elevados en el estrato de carga horaria mínima
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Tasa relativa de ingresos superiores normalizada por país de origen
    total_by_country = df['native-country'].value_counts()
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    rate_rich_by_country = (rich_by_country / total_by_country) * 100

    highest_earning_country = rate_rich_by_country.idxmax()
    highest_earning_country_percentage = round(rate_rich_by_country.max(), 1)

    # 9. Moda ocupacional en el segmento de altos ingresos para India
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_income['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }