
import pandas

def main():
    df = pandas.concat([read_csv('./data/daily_sales_data_0.csv'), read_csv('./data/daily_sales_data_1.csv'), read_csv('./data/daily_sales_data_2.csv')])
    parsed_data = parse_data(df)
    write_csv(parsed_data)

def read_csv(data_file):
    df = pandas.read_csv(data_file, parse_dates=['date'])
    return df

def parse_data(data):
    filtered_data = data.query("product == 'pink morsel'")
    new_data = pandas.DataFrame(columns=["sales", "date", "region"])
    for index, row in filtered_data.iterrows():
        sales = f'{float(row["price"].replace('$','')) * int(row["quantity"]):.2f}'
        new_data.loc[len(new_data)] = {"sales": sales, "date": row["date"],"region":  row["region"]}

    return new_data

def write_csv(df):
    df.to_csv('./data/daily_sales_modified_0.csv', index=False)

if __name__ == "__main__":
    main()