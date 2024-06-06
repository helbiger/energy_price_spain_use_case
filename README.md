# Electricity prices analyses and forecasting
Analyse energy prices in Spain based on consumption, weather and generation data and create a forecast of the electricity price

## Full presentation:
[Results Presentation](Analyse_Energy_prices_Spain_results.pdf)

##### Timeseries forecasting and managementsummary

## 1. Workflow – CRISP-DM:

- Forecasts for the Spanish energy transition
    - **Data Preparationand Feature Engineering:**
       - Checking and removingduplicates
       - Checking and removingoutliers
       - Check formissing values
       - Fill in missing valueswith last know data(interpolation)
       - Cretedatasetper cityfrom weather
       - Restrictdatasetto highlycorrelatedfeatures(basedon target)
       - Create simple time features, e.g. dayoftheweek, month, etc.

###### CRISP-DM:

```
[1] -https://datasolut.com/crisp-dm-standard/
```
```
CRISP-DM:
```

## 2. Factors influencing the electricity price

- Trends andSeasonality
    Electricity price (€/MWh)
    across weekdays & months

```
Electricity price (€/MWh)
across weekdays & hours
```
```
Trends & Seasonalityofelectricityprices
⚫ Seasonality : Montly, dailyand hourly
⚫ Monthly :
⚫ Electricity prices tend to be lower in winter
⚫ Highest electricity prices in late summer (September maximum)
⚫ Possible reason: high demand (ac) and lower production (water)
⚫ Does not correlate 1:1 with electricity demand (highest in winter and
summer)
⚫ Daily :
⚫ Working days higher than weekends (possible reason: industry)
⚫ Hourly :
⚫ Cheapest at night, most expensive in the evening (5-9 pm)
⚫ Striking: 13-16 h the electricity price is lower (possibly siesta time in Spain)
```

## 2. Factors influencing the electricity price

- Resultsofcorrelationanalysis

```
Figure: Highest linear correlation to the target variable electricity price
```
```
⚫ Positivelycorrelated::
⚫ Day-Ahead-Preis (0.67)
⚫ Generation bynaturalgas(0.48)
⚫ Erzeugung durch Kohle (0.46)
⚫ Negativelycorrelated:
⚫ Generation byhydropump (-0.48)
⚫ Generation wind power (-0.33)
⚫ Wind speedMadrid (-0.33)
⚫ Strong correlation of temperature data between the cities
```

## 2. Factors influencing the electricity price

- Resultsofcorrelationanalysis

```
Analysis of the high electricity prices in September compared to the year as a whole revealed
⚫ Higher influencing factor due to consumption (possibly air conditioning systems with high consumption)
⚫ Higher influencing factor Hydropower reservoir (water shortage due to drought → Generation more expensive
```
```
Rank September
Merkmal
```
```
September
Korrelation
```
```
Gesamtjahr
Merkmal
```
```
Gesamtjahr
Korrelation
```
1. Electricityprice 1.0 Electricityprice 1.
2. Gaserzeugung 0.55 Day-Ahead-Price 0.
3. Generation by
    waterreservoir

```
0.52 Generation bygas 0.
```
4. Electricitydemand **0.51** Generation bycoal 0.
5. Day-Ahead-Price 0.48 Temp_max_Sevilla 0.


### 3. Time seriesforecast

- Comparison of different ML models with cross-validation and AutoML (criteria: **MAPE** )
- ChooseEBM (ML-Model) –Explainable BoostingMachine (Regressor)

```
Time Prei
s
```
```
Preis Prognose Abs(Preis –
Prog.)
```
```
Abs / Preis
```
```
23:00:00 67 65 2 2 / 67 =
0,
00:00:00 58 60 2 2 / 58 =
0,
```
```
MAPE = (0,029 +0,035) /
= 0,032 → 3,2 %
```
```
[2] -https://interpret.ml/docs/ebm.html
```
```
Mean absolute percentage error
```

### 4. Evaluation & Explainability

- Evaluation with TSO:
- Interpret Model:
    - **Global** : [http://127.0.0.1:7777/140231638982464/](http://127.0.0.1:7777/140231638982464/)
    - **Lokal** : [http://127.0.0.1:7777/140231638978864/](http://127.0.0.1:7777/140231638978864/)


## 4. Global Explainability

- Feature Importancefrom theEBM model


## 5. Conclusion and outlook

- **Conclusion** :
    - Influencing factors identified and explained (see chapter 2)
    - Forecast created with very low error (3.5%) for the next 24 hours
    - Recommendation for transmission system operators → Own forecast is significantly more accurate
- **Next steps** :
    - Forecast various weather data and producers for more accurate forecasts and out-of-sample forecasts
    - Detailed analysis of additional features in order to identify further trends and derive new features from
       them
    - Data set sufficiently large for an approach with artificial neural networks
       - But training computationally and time consuming


## 6. Additional Slides


#### Additional slide: Explainable Boosting Machines

- Explainable Boosting Machine (EBM) is a tree-based, cyclic gradient boosting Generalized Additive Model with automatic
    interaction detection. EBMs are often as accurate as state-of-the-art blackbox models while remaining completely interpretable.
    Although EBMs are often slower to train than other modern algorithms, EBMs are extremely compact and fast at prediction
    time.
- Explainable Boosting Machine (interpret.ml)
- Exploringexplainableboostingmachines


## Additional slide: Explain calculation MAPE

**Time Price Price_Predictio
n**

```
Abs(price–pred) (M)APE
```
###### 23:00:00 67 65 2 2 / 67 = 0,

###### 00:00:00 58 60 2 2 / 58 = 0,

###### (0,029 + 0,035)

###### /

###### = 0,032 → 3,2 %


