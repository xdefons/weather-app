import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Miesiąc":["Styczeń","Luty","Marczec","Kwiecień"],
    "Sprzedaż":[120,400,200,100]
}

dataframe = pd.DataFrame(data)

print(dataframe.values)
print(dataframe.head(1))

dataframe.plot(
    x="Miesiąc",
    y="Sprzedaż",
    kind="barh", #bar h - wykres slupkowy(bar) horyzontalny (h)
    color="blue"
)




data2 = {
    "x":[1,5,4,3,62,34,42,2,3,4],
    "y":[56,34,21,23,42,634,123,4,3,23]
}

df2 = pd.DataFrame(data2)
df2.plot(
    x="x",
    y="y",
    kind="scatter",
    color="green"
)

plt.title("zależność miedzy X a Y")
plt.xlabel("Mesiące")
plt.ylabel("Ilość")

plt.ylim(0, max(data["Sprzedaż"])+25)  #oś Y bedzie miec zakres od 0 do maxymalnej wartosci sprzedazy + bufor 25

plt.show()

dataframe = pd.DataFrame(data)
dataframe.to_json("test.json",force_ascii=False)
dataframe.to_html("test.html")
