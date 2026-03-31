import pandas

DATA_DIRECTORY = './data'
DATA_FILES = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv' ]

def process_data():
    df = None
    for i, file in enumerate(DATA_FILES):
        if i == 0:
            df = read_csv(f'{DATA_DIRECTORY}/{file}')
        else:
            pandas.concat([df, read_csv(f'{DATA_DIRECTORY}/{file}')])
    parsed_data = parse_data(df)
    return parsed_data

def read_csv(data_file):
    df = pandas.read_csv(data_file, parse_dates=['date'])
    return df

def parse_data(data):
    filtered_data = data.query("product == 'pink morsel'")
    new_data = pandas.DataFrame(columns=['date', 'region', 'sales'])
    for index, row in filtered_data.iterrows():
        sales = f'{float(row["price"].replace('$','')) * int(row["quantity"]):.2f}'
        new_data.loc[len(new_data)] = { "date": row["date"],"region":  row["region"], "sales": sales}

    return new_data

def write_csv(df):
    df.to_csv('./data/daily_sales_modified_0.csv', index=False)

if __name__ == "__main__":
    process_data()