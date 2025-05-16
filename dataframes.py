import pandas as pd
import glob
import os

path = "data/"  # "C:\KU\data lab\mensa\MensaProject"
prod_files = glob.glob(f"{path}/*Produktionsplanung.xlsx")
prod_dfs = []
for file in prod_files:
    df = pd.read_excel(file)

    # leave only the necessary columns (the names are in German and in all files are the same)
    df_reduced = df[["Prod.Dat.", "Gebinde", "Bezeichnung", "Sollmenge", "Ausgabe"]]

    # remame for convenience
    df_reduced.columns = ["Datum", "Produkt", "Bezeichnung", "Sollmenge", "Ausgabe"]

    # adding it to the dataframelist
    prod_dfs.append(df_reduced)
prod_full_df = pd.concat(prod_dfs, ignore_index=True)
prod_full_df["Datum"] = pd.to_datetime(prod_full_df["Datum"], format="%d/%m/%Y")


# Путь к директории с файлами
data_dir = "data/"  # "C:\KU\data lab\mensa\MensaProject"
verkauf_files = glob.glob(os.path.join(data_dir, "*Verkaufszahlen.xlsx"))

combined_rows = []

for file in verkauf_files:
    # Чтение файла без заголовков
    df_raw = pd.read_excel(file, header=None)
    # df_raw = df_raw.iloc[5:].reset_index(drop=True)
    # Заполнение объединённых ячеек сверху вниз
    df_filled = df_raw.fillna(method="ffill", axis=0)

    # Ищем начало данных — продуктовые строки начинаются примерно с 5 строки
    df_data = df_filled.iloc[5:].copy()

    # Извлекаем название продукта (столбец 6) и даты (столбцы начиная с 8)
    produkt_col = df_data.iloc[:, 6]
    data_cols = df_data.columns[8:]

    for col in data_cols:
        datum = df_filled.iloc[3, col]  # строка 3 содержит даты в заголовках
        if pd.isna(datum):
            continue  # пропускаем пустые заголовки
        mengen = df_data[col]
        for produkt, menge in zip(produkt_col, mengen):
            if pd.notna(produkt) and pd.notna(menge):
                combined_rows.append(
                    {
                        "Datum": pd.to_datetime(datum, errors="coerce"),
                        "Produkt": str(produkt).strip(),
                        "Menge": menge,
                    }
                )

# Собираем в один DataFrame
verkauf_full_df = pd.DataFrame(combined_rows)


def is_numeric(val):
    try:
        float(val)
        return True
    except (ValueError, TypeError):
        return False


non_numeric_rows = verkauf_full_df[~verkauf_full_df["Menge"].apply(is_numeric)]
# print(len(verkauf_full_df))
# print(len(prod_full_df))
# print(prod_full_df.head(10))
# print(verkauf_full_df.head(10))

df_planung_renamed = prod_full_df.rename(
    columns={"Sollmenge": "Geplant-Sollmenge", "Ausgabe": "Geplant-Ausgabe"}
)
df_verkauf_renamed = verkauf_full_df.rename(columns={"Menge": "Verkauft"})

# Объединяем по дате и названию продукта
df_merged = pd.merge(
    df_planung_renamed,
    df_verkauf_renamed,
    how="outer",  # или "inner", если хочешь только пересекающиеся строки
    on=["Datum", "Produkt"],
)

# Убедимся, что даты в одинаковом формате
df_merged["Datum"] = pd.to_datetime(df_merged["Datum"])
print(df_merged.head(30))
