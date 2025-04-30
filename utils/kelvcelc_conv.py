

def kelvcelcconv(kelv):
    celc = kelv - 273.15

    return round(celc,2)

#mozna zrobic jako lambde, np:
# kelvcelcconv: lambda x: round(x - 273.15, 2)
