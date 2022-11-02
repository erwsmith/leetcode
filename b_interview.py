import pandas as pd

unitDf = pd.DataFrame({
    "id": range(10),
    "floor": [i // 5 + 1 for i in range(10)],
    "number": ["{}0{}".format(i // 5 + 1, i % 5 + 1) for i in range(10)],
    "beds": [1,2,1,2,3,1,2,1,2,3],
    "sqft": [700, 1100, 800, 1100, 1400, 700, 1100, 800, 1100, 1400],
    "price": [1010, 2010, 1010, 2010, 3010, 1020, 2020, 1020, 2020, 3020],
    "tenantId": [1, 2, None, 3, 4, None, 5, 6, None, None],
    "tenantRent": [1000, 1900, None, 1010, 950, None, 900, 1500, None, None]
})
unitDf.set_index('id', inplace=True)

unitDf['pricePerSqft'] = unitDf['price'] / unitDf['sqft']

# print(unitDf[['floor', 'price','tenantRent']].groupby('floor').mean())

# weight by bedcount
unitDf['Multiplier'] = unitDf['beds'] / unitDf['beds'].sum()
unitDf['WeightedPricePerSqft'] = unitDf['Multiplier'] * unitDf['pricePerSqft']

print(unitDf['WeightedPricePerSqft'].sum())

# print(unitDf['Multiplier'].sum())