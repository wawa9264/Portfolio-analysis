# Portfolio Optimization Tool

## Overview

This repository offers a portfolio optimization tool grounded in the principles of Modern Portfolio Theory (MPT) to assist investors in locating the optimal allocation of assets based on the desired risk-adjusted returns. The tool uses the Sharpe ratio as the objective in portfolio selection to locate portfolios with minimum risk and maximum return.

## Key Features

- **Mean-Variance Optimization**: Implements Markowitz's Modern Portfolio Theory
- **Sharpe Ratio Maximization**: Optimizes risk-adjusted returns
- **Custom Constraints**: Supports allocation bounds and restrictions
- **Visualization**: Plots efficient frontier and optimal portfolio

## Usage

1. Prepare historical return data (can fetch from Yahoo Finance or use custom datasets)
2. Configure optimization parameters (risk-free rate, constraints, etc.)
3. Run optimization algorithm
4. View optimal portfolio allocation
5. Visualize efficient frontier and optimal portfolio

## Output Description

The optimizer returns:
- Optimal asset weights 
- Annualized portfolio return
- Annualized portfolio volatility (risk)
- Portfolio Sharpe ratio

## Theoretical Background

### Sharpe Ratio
Measures excess return per unit of risk:
\[
\text{Sharpe Ratio} = \frac{E[R_p] - R_f}{\sigma_p}
\]
Where:
- \(E[R_p]\) is expected portfolio return
- \(R_f\) is risk-free rate
- \(\sigma_p\) is portfolio return standard deviation (risk)

### Optimization Problem
Maximizing Sharpe ratio solves:
\[
\max_w \frac{w^T \mu - R_f}{\sqrt{w^T \Sigma w}}
\]
Subject to:
\[
\sum_{i=1}^n w_i = 1
\]
\[
w_i \geq 0 \quad \text{(no short selling)}
\]


## Contribution Guidelines

Contributions via Pull Requests or Issues are welcome. Key development areas include:
- Additional constraints (sector limits, ESG scores, etc.)
- Black-Litterman model implementation
- Numerical stability improvements
- Enhanced visualization capabilities

## Disclaimer

This code is for educational/research purposes only and does not constitute investment advice. Actual investment decisions should consider additional factors and professional financial advice. The author bears no responsibility for any investment losses resulting from using this code.
