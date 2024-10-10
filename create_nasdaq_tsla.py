import pandas as pd

# Загрузка данных
df1 = pd.read_csv('TESLA INC (06-29-2010 _ 09-12-2022).csv')
df2 = pd.read_csv('TESLA INC (09-13-2022 _ 10-07-2024).csv')

# Объединение DataFrame-ов
combined_df = pd.concat([df1, df2], ignore_index=True)

# Преобразование столбца 'Date' в формат datetime
combined_df['Date'] = pd.to_datetime(combined_df['Date'])

# Сортировка объединенного DataFrame по столбцу 'Date'
combined_df = combined_df.sort_values(by='Date')

# Обработка столбца 'Volume'
def remove_separators(volume_str):
    return int(volume_str.replace(',', ''))

combined_df['Volume'] = combined_df['Volume'].apply(remove_separators)

# Сохранение данных в файл nasdaq_tsla.csv с исходными шапками и двойными кавычками
with open('nasdaq_tsla.csv', 'w', newline='') as file:
    file.write('"Date","Open","High","Low","Close","Volume"' + '\n')
    for index, row in combined_df.iterrows():
        date_str = f'"{row["Date"].strftime("%Y-%m-%d")}"'
        open_val = f'"{row["Open"]:.4f}"'
        high_val = f'"{row["High"]:.4f}"'
        low_val = f'"{row["Low"]:.4f}"'
        close_val = f'"{row["Close"]:.4f}"'
        volume_val = f'"{int(row["Volume"])}"'
        file.write(f"{date_str},{open_val},{high_val},{low_val},{close_val},{volume_val}\n")

# Создание нового DataFrame с нужной шапкой и формате даты 'YYYYMMDDТ'
new_df = pd.DataFrame({
    'series': combined_df['Date'].dt.strftime('%Y%m%dT'),
    'o': combined_df['Open'].round(4),
    'h': combined_df['High'].round(4),
    'l': combined_df['Low'].round(4),
    'c': combined_df['Close'].round(4),
    'v': combined_df['Volume'].astype(int)
})

# Сохранение нового DataFrame в файл SIMULATED_TSLA.csv с шапкой и двойными кавычками
with open('SIMULATED_TSLA.csv', 'w', newline='') as file:
    file.write('series,o,h,l,c,v\n')
    for i, row in new_df.iterrows():
        file.write(f'"{row["series"]}","{row["o"]}","{row["h"]}","{row["l"]}","{row["c"]}","{row["v"]}"\n')
