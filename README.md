Computational Finance Projects

A collection of computational finance projects implemented in Python, focusing on simulation-based methods and derivative pricing.

Projects

1. Monte Carlo Stock Price Simulator with Risk Analytics
   This project implements a Monte Carlo simulation framework to model possible future price paths of a stock using the Geometric Brownian Motion     (GBM) assumption.
  It demonstrates practical application of probability modeling, stochastic processes, and numerical simulation in financial analysis.

  Features: 
  1. Historic price retrieval using Yahoo Finance API
  2. Simulation of multiple stochastic price paths
  3. User defined inputs
  4. Risk analytics include: probability of loss, value at risk (VaR), expected shortfall (ES), probability of outperforming a benchmark return
  5. Visualizations: simulated price trajectory plots, histogram of final price distribution with risk thresholds

  <img width="1282" height="1095" alt="image" src="https://github.com/user-attachments/assets/ed813da3-feb3-4f1c-ace1-97fd0256d33b" />
  <img width="1599" height="1124" alt="image" src="https://github.com/user-attachments/assets/37f82953-4bbf-428f-becf-f1dc53cb8a20" />
  (Images represent graphs plotted for stock ticker AAPL, duration 4 years, 500 simulated paths)

  Technologies:
  1. Python
  2. Numpy
  3. Matplotlib
  4. yfinance

2. European Call Option Pricing
   This project implements Monte Carlo simulation techniques to price European call options and compares the numerical estimate with the analytical  Black-Scholes solution.

  It demonstrates practical application of stochastic processes, risk-neutral valuation, and numerical methods in computational finance.

  Features:
  1. Historical stock price retrieval using Yahoo Finance API
  2. Estimation of annualized volatility from historical log returns
  3. Monte Carlo simulation of future stock price paths under the Geometric Brownian Motion (GBM) assumption
  4. Pricing of European call options using discounted expected payoffs
  5. Black-Scholes analytical pricing for validation and comparison
  6. Confidence interval estimation for Monte Carlo prices
  7. Convergence analysis showing how Monte Carlo estimates approach the Black-Scholes price as the number of simulations increases

  Technologies: 
  1. Python
  2. Numpy
  3. SciPy
  4. Matplotlib
  5. yfinance
   
Author:
Aradhya Kashyap,
UG Mathematics & Computing
