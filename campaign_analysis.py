import pandas as pd

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv("Campaign-Data.csv")

print("Data loaded")
print(df.head())
print("\nColumns:")
print(df.columns)

# ----------------------------
# Campaign columns
# ----------------------------
campaign_columns = [
    "Campaign (Email)",
    "Campaign (Flyer)",
    "Campaign (Phone)"
]

results = []

# ----------------------------
# Loop through campaigns
# ----------------------------
for campaign in campaign_columns:

    # campaign is considered active if value > 0
    campaign_data = df[df[campaign] > 0]

    if len(campaign_data) == 0:
        continue

    total_units = campaign_data["Unit Sold"].sum()
    total_revenue = campaign_data["Amount Collected"].sum()
    customers = campaign_data["Client ID"].nunique()

    revenue_per_customer = total_revenue / customers
    units_per_customer = total_units / customers

    results.append({
        "Campaign": campaign.replace("Campaign (", "").replace(")", ""),
        "Total Units Sold": total_units,
        "Total Revenue": total_revenue,
        "Customers Reached": customers,
        "Revenue per Customer": round(revenue_per_customer, 2),
        "Units per Customer": round(units_per_customer, 2)
    })

# ----------------------------
# Final results table
# ----------------------------
campaign_summary = pd.DataFrame(results)

print("\nCampaign Summary:")
print(campaign_summary)

# ----------------------------
# Simple benchmarking
# ----------------------------
avg_revenue = campaign_summary["Revenue per Customer"].mean()

campaign_summary["Performance"] = campaign_summary[
    "Revenue per Customer"
].apply(
    lambda x: "Above Average" if x >= avg_revenue else "Below Average"
)

print("\nCampaign Performance:")
print(campaign_summary[["Campaign", "Performance"]])

# ----------------------------
# Business insights
# ----------------------------
print("\nInsights:")
for _, row in campaign_summary.iterrows():
    print(
        f"{row['Campaign']} campaign is "
        f"{row['Performance']} in terms of revenue per customer."
    )


