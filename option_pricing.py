import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

#black-scholes function
def black_scholes_call(S,K,T,r,sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    call_price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    return call_price

#data & parameter estimation
ticker = input("Enter stock ticker: ")
years = float(input("Years: "))
K = float(input("Strike price: "))
r = float(input("Risk-free rate: "))
n_sim = int(input("Number of simulations: "))

data = yf.download(ticker, period="2y")

if data.empty:
    print("Download failed")
    exit()

prices = data["Close"].dropna().values.flatten()

returns = np.diff(np.log(prices)) #log returns
if len(returns)==0:
    print("No returns computed. Check data")
    exit()

sigma = returns.std()*np.sqrt(252)

S0 = prices[-1]

#monte carlo simulation
T = years
steps = int(252*T) #approx 252 trading days in a year
dt = 1/252

paths = np.zeros((steps, n_sim))
paths[0] = S0

for t in range(1, steps):
    z = np.random.standard_normal(n_sim)
    paths[t] = paths[t-1]*np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)

final_prices = paths[-1]

#monte carlo option pricing
payoffs = np.maximum(final_prices - K, 0)
discounted_payoffs = np.exp(-r*T) * payoffs

mc_price = np.mean(discounted_payoffs)

#black-scholes price
bs_price = black_scholes_call(S0, K, T, r, sigma)

#confidence interval
std_error = np.std(discounted_payoffs, ddof = 1)/np.sqrt(n_sim)
conf_low = mc_price - 1.96*std_error
conf_high = mc_price + 1.96*std_error

#comparision output
print("\n--- Option Pricing Results ---")
print("Monte Carlo price: ", mc_price)
print("Black-Scholes price: ", bs_price)
print("Absolute difference: ", abs(mc_price - bs_price))
print("95% Confidence interval: ({}, {})".format(conf_low, conf_high))

#convergence analysis - how monte carlo price converges to black scholes
sim_list = [100, 200, 500, 1000, 2000, 5000, 10000]
prices_mc = []
errors = []

repetitions = 20

for n in sim_list:
    run_prices = []

    for _ in range(repetitions):
        paths = np.zeros((steps,n))
        paths[0] = S0

        for t in range (1, steps):
            z = np.random.standard_normal(n)
            paths[t] = paths[t-1]*np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)

        final_prices = paths[-1]
        payoffs = np.maximum(final_prices - K, 0)
        discounted_payoffs = np.exp(-r*T) * payoffs    
        price = np.mean(discounted_payoffs)
        run_prices.append(price)

    prices_mc.append(np.mean(run_prices))
    errors.append(1.96 * np.std(run_prices, ddof = 1))

plt.figure(figsize = (10, 6))
plt.errorbar(sim_list, prices_mc, yerr = errors, fmt = 'o-', capsize = 5, label = 'Monte Carlo Estimate (95% CI)')
plt.axhline(bs_price, color = "red", linestyle = "--", label = f"Black-Scholes ({bs_price:.2f})")
plt.xscale('log')
plt.xlabel("Number of simulations")
plt.ylabel("Option price ($)")
plt.legend()
plt.grid(True)
plt.title(f"Monte Carlo Convergence for {ticker} European Call Option")
plt.savefig("convergence_plot.png", dpi = 300, bbox_inches = 'tight')
plt.show()
