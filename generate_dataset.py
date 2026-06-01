import pandas as pd
import numpy as np

np.random.seed(42)

rows = 5000

data = pd.DataFrame({
    "amount": np.random.randint(100,100000,rows),
    "hour": np.random.randint(0,24,rows),
    "online": np.random.randint(0,2,rows),
    "card_present": np.random.randint(0,2,rows),
    "new_device": np.random.randint(0,2,rows),
    "high_risk_country": np.random.randint(0,2,rows)
})

data["fraud"] = (
    (data["amount"] > 50000) &
    (data["online"] == 1) &
    (data["new_device"] == 1)
).astype(int)

data.to_csv("fraud_dataset.csv", index=False)

print(data.head())