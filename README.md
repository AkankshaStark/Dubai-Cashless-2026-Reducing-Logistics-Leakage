# Dubai-Cashless-2026-Reducing-Logistics-Leakage

Current logistics operations in Dubai are hindered by a high volume of Cash on Delivery (COD) orders, which drive significant financial inefficiency. By leveraging a predictive "Aani Nudge" model, this project identifies high-risk transactions in real-time and encourages a transition to digital payments. Implementing this strategy across key districts like JVC and Al Barsha projects a substantial reduction in failed deliveries and a direct boost to the bottom line.

The Executive Dashboard


Technical Stack

VS Code: Primary IDE for data engineering and model development.
Python: Used for data cleaning, exploratory data analysis (EDA), and building the predictive "Nudge" model (stored as .pkl).
SQL/SQLite: Data storage and management (stored as .db).
Power BI: Advanced visualization and executive reporting.

Project Structure

/dashboard: Contains the screen recording for the interactive Power BI report.
/models: Contains the trained .pkl predictive model for the Aani Nudge.
/database: Contains the .db file (SQLite) housing the logistics transaction data.
/notebooks: Jupyter notebooks covering the data science workflow.
/output: High-resolution screenshots for documentation.

Conclusion

The COD Risk: Cash on Delivery (COD) consistently exhibits a ~17.43% Return-to-Origin (RTO) rate, nearly double the rate of digital alternatives like Aani or ApplePay.
Financial Leakage: Identified a total of AED 251.35K in annual logistics leakage directly tied to failed payment-on-delivery attempts.
Geographic Hotspots: High-density residential areas (JVC, International City) show the highest concentration of waste, making them prime targets for the digital payment rollout.
The Aani Solution: By converting just 20% of high-risk COD orders to Aani Instant payments, the model projects thousands in immediate recoverable savings per district.

How to Use

Explore the Model: Navigate to /notebooks to see the logic behind the predictive nudge.
View the Data: Check /database for the structured transaction logs.
Interact with the Report: Open the file in /dashboard to filter by district and view the financial waterfall bridge.
