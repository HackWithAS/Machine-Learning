import pandas as pd

data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai"]
}

df = pd.DataFrame(data)


dummy = pd.get_dummies(df["City"])

print(dummy)
