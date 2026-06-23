import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("daily_sales.csv")

# Prepare data
df.columns = ["ds", "y"]
df["ds"] = pd.to_datetime(df["ds"])

# Train Prophet model
model = Prophet()
model.fit(df)

# Forecast next 30 days
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Save forecast.csv
forecast_output = forecast[
    ["ds", "yhat", "yhat_lower", "yhat_upper"]
]

forecast_output.columns = [
    "Date",
    "PredictedSales",
    "LowerBound",
    "UpperBound"
]

forecast_output.to_csv(
    "forecast.csv",
    index=False
)

# Forecast graph
fig = model.plot(forecast)
fig.savefig("forecast_graph.png")

# Components graph
fig2 = model.plot_components(forecast)
fig2.savefig("components_graph.png")