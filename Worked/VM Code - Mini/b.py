import pandas as pd
import glob

csv1 = glob.glob('pfp/multiTimeline *.{}'.format('csv'))
print(csv1)

df2 = pd.DataFrame(
    columns=['Month', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12', '2024-01', '2024-02', '2024-03',
             '2024-04', '2024-05', '2024-06', '2024-07','2024-08'])
count = 0
# print(csv1)

for i in csv1:
    # print(i)
    csv_data = pd.read_csv(i, names=['Week', 'Value'])

    Keyword = csv_data.Value[1]

    #For India
    # Keyword = Keyword[:len(Keyword)-9]

    #For (United States)
    Keyword = Keyword[:len(Keyword)-17]
    # print(Keyword)

    csv_data = pd.read_csv(i, names=['Week', Keyword])

    data = csv_data[2:]


    df = pd.DataFrame(data, columns=['Week', Keyword])

    df[Keyword] = df[Keyword].replace('<1', 0)

    df['Week'] = pd.to_datetime(df['Week'])

    df['Month'] = df['Week'].dt.to_period('M')

    df[Keyword] = pd.to_numeric(df[Keyword])
    # print(f"{Keyword}")

    monthly_mean = df.groupby('Month')[Keyword].mean()
    # print(monthly_mean)
    val = []
    for row in monthly_mean:
        val.append(row)

    try:
        df2.loc[count] = [Keyword] + val
    except:
        print(i)
        print(Keyword)
    # print(df2)
    count = count + 1
# print(df2)
df2.drop_duplicates(subset=['Month'], keep='first', inplace=True)
df2 = df2.reset_index()
df2.pop('index')

print(df2)
df2.to_csv('pfp.csv')

# Read the data into a DataFrame