# Advance-Equity-Portfolio-Risk-Management
**Python-based risk analytics platform for calculating, scaling, backtesting, and visualizing Value at Risk (VaR) for equity portfolios using Historical Simulation, EWMA, GARCH, GJR-GARCH, and VaR backtesting**

---


## Overview

**Advance Equity POrtfolio Risk Management** is a modular Python project developed to build a complete market risk analytics platform for equity portfolios.

The project follows professional software engineering principles and quantitative finance methodologies to reproduce the market risk workflow commonly used in investment banks, asset management firms, consulting companies, and quantitative research teams.

Starting from raw financial market data, the platform progressively performs data collection, data validation, portfolio construction, market risk estimation, volatility modeling, model validation, stress testing, and interactive visualization.

The project is implemented using a modular architecture, where each component is responsible for one specific task, making the code easier to understand, maintain, test, and extend.

---

## What This Project Does
The project includes:

- Historical Simulation VaR
- Expected Shortfall (ES)
- EWMA Volatility Scaling
- GARCH(1,1)
- GJR-GARCH
- VaR Backtesting
- Model Comparison
- Stress Testing
- Interactive Dashboard


---

## Project Progress

| Phase | Status | Description |
|--------|--------|-------------|
| Phase 1 | ✅ Completed | Data Collection |
| Phase 2 | 🚧 In Progress | Data Cleaning |
| Phase 3 | ⏳ Planned | Portfolio Construction |
| Phase 4 | ⏳ Planned | Historical Simulation VaR |
| Phase 5 | ⏳ Planned | EWMA Volatility Scaling |
| Phase 6 | ⏳ Planned | GARCH Volatility Scaling |
| Phase 7 | ⏳ Planned | GJR-GARCH Volatility Scaling |
| Phase 8 | ⏳ Planned | VaR Backtesting |
| Phase 9 | ⏳ Planned | Model Comparison |
| Phase 10 | ⏳ Planned | Stress Testing |
| Dashboard | ⏳ Planned | Interactive Streamlit Dashboard |

---

## Project Scope

The **Market Risk Track** project aims to develop a comprehensive and modular market risk analytics platform for equity portfolios. It reproduces the complete workflow commonly adopted by financial institutions to measure, analyze, validate, and communicate portfolio market risk.

The platform is designed to support the entire risk management lifecycle, from financial data acquisition to portfolio construction, Value at Risk estimation, volatility modeling, statistical backtesting, stress testing, and interactive visualization.

The project emphasizes modular software development, quantitative finance methodologies, reproducibility, and scalability, allowing each component to be developed, tested, and maintained independently.

---

### Portfolio Types

The platform supports multiple portfolio configurations:

- Long-only portfolios
- Equal-weighted portfolios
- User-defined weighted portfolios
- Market capitalization weighted portfolios
- Multi-asset equity portfolios
- Long-short portfolios (optional)

---

### Asset Universe

The initial implementation focuses on publicly traded U.S. equities downloaded from Yahoo Finance.

The default portfolio consists of the following assets:

| Ticker | Company |
|---------|---------|
| AAPL | Apple Inc. |
| MSFT | Microsoft Corporation |
| NVDA | NVIDIA Corporation |
| JPM | JPMorgan Chase & Co. |
| XOM | Exxon Mobil Corporation |
| AMZN | Amazon.com Inc. |
| META | Meta Platforms Inc. |
| GOOGL | Alphabet Inc. |
| TSLA | Tesla Inc. |
| UNH | UnitedHealth Group Inc. |

The portfolio benchmark is the **S&P 500 Index (^GSPC)**.

An optional risk-free rate is obtained from the **13-Week U.S. Treasury Bill (^IRX)**.

---

### Risk Measures

The platform estimates and analyzes a wide range of portfolio risk metrics, including:

- Daily Simple Returns
- Daily Logarithmic Returns
- Portfolio Returns
- Portfolio Profit and Loss (P&L)
- Portfolio Volatility
- Historical Simulation Value at Risk (VaR)
- Expected Shortfall (ES)
- Rolling Value at Risk
- Drawdown
- Backtesting Exceptions

---

### Data Sources

The project currently uses **Yahoo Finance** through the **yfinance** Python package as its primary market data provider.

Additional data providers may be integrated in future versions:

- Yahoo Finance
- Stooq
- Alpha Vantage
- Polygon.io
- WRDS (Wharton Research Data Services)

---

### Development Philosophy

The project follows a modular software architecture where each component is responsible for a single well-defined task.

Examples include:

- Data Collection
- Data Cleaning
- Portfolio Construction
- Risk Engine
- Volatility Models
- Backtesting
- Stress Testing
- Visualization

This design improves code readability, maintainability, testability, and scalability while facilitating future extensions and collaboration among multiple developers.

---

### Intended Applications

The methodologies implemented in this project are representative of workflows commonly found in:

- Investment Banks
- Commercial Banks
- Asset Management Firms
- Hedge Funds
- Insurance Companies
- Financial Consulting Firms
- Quantitative Research Teams
- Academic Research Projects

Although developed for educational and research purposes, the platform is designed following professional software engineering practices and quantitative finance standards.


## Project Workflow

The **Advance Equity Portfolio Risk Management** platform follows a modular end-to-end risk management workflow. Each phase uses the outputs generated by the previous stage, creating a reproducible and scalable quantitative risk analytics pipeline.

| Phase | Module | Main Objective |
|------:|--------|----------------|
| 1 | **Data Collection** | Download, validate, and store market and benchmark data |
| 2 | **Data Cleaning** | Clean, align, and transform raw financial data |
| 3 | **Portfolio Construction** | Build the investment portfolio and calculate returns and P&L |
| 4 | **Historical Simulation VaR** | Estimate portfolio Value at Risk and Expected Shortfall |
| 5 | **EWMA Volatility Scaling** | Apply EWMA conditional volatility scaling |
| 6 | **GARCH Volatility Scaling** | Estimate conditional volatility using a GARCH(1,1) model |
| 7 | **GJR-GARCH Volatility Scaling** | Capture asymmetric volatility using the GJR-GARCH model |
| 8 | **VaR Backtesting** | Validate VaR forecasts using statistical backtesting tests |
| 9 | **Model Comparison** | Compare the performance of all implemented VaR models |
| 10 | **Stress Testing** | Evaluate portfolio performance under extreme market scenarios |
| 11 | **Interactive Dashboard** | Present risk analytics through an interactive Streamlit dashboard |

---

### Phase 1 – Data Collection

Collects market data required for portfolio risk analysis, including equity prices, benchmark data, portfolio weights, and optional market information.

**Main outputs**

- Adjusted Close Prices
- Daily Returns
- Portfolio Weights
- Benchmark Prices
- Risk-Free Rate (optional)
- Sector Information (optional)

---

### Phase 2 – Data Cleaning

Validates and prepares the raw financial data before any quantitative analysis.

**Main tasks**

- Align trading calendars
- Handle missing values
- Remove stale prices
- Winsorize extreme observations
- Calculate log returns
- Generate clean return matrices

---

### Phase 3 – Portfolio Construction

Builds the investment portfolio using user-defined or predefined allocation strategies.

**Main outputs**

- Portfolio Value
- Portfolio Returns
- Portfolio Profit & Loss (P&L)

---

### Phase 4 – Historical Simulation VaR

Estimates portfolio risk using non-parametric Historical Simulation.

**Risk measures**

- Historical Value at Risk
- Expected Shortfall
- Rolling VaR

---

### Phase 5 – EWMA Volatility Scaling

Applies exponentially weighted volatility estimates to improve Historical VaR under changing market conditions.

---

### Phase 6 – GARCH Volatility Scaling

Models conditional volatility using a GARCH(1,1) process and computes volatility-scaled Historical VaR.

---

### Phase 7 – GJR-GARCH Volatility Scaling

Extends the GARCH model by incorporating asymmetric volatility responses to negative market shocks.

---

### Phase 8 – VaR Backtesting

Evaluates the statistical performance of each VaR model using internationally recognized backtesting procedures.

**Implemented tests**

- Kupiec Proportion of Failures Test
- Christoffersen Independence Test
- Christoffersen Conditional Coverage Test
- Basel Traffic Light Framework

---

### Phase 9 – Model Comparison

Compares all implemented VaR methodologies using common performance metrics, statistical tests, and visualization tools.

---

### Phase 10 – Stress Testing

Evaluates portfolio resilience under historical crises and hypothetical adverse market scenarios.

**Scenario categories**

- Historical market crises
- Market shocks
- Volatility shocks
- Correlation shocks
- Sector-specific shocks

---

### Interactive Dashboard

The final stage integrates all analytical components into an interactive dashboard developed with **Streamlit** and **Plotly**.

Users can:

- Build portfolios
- Visualize portfolio performance
- Estimate Value at Risk
- Compare volatility models
- Perform statistical backtesting
- Run stress-testing scenarios
- Explore interactive charts and risk metrics

## Project Architecture

The **Market Risk Track** project follows a modular architecture inspired by professional quantitative risk management systems used in investment banks, asset management firms, and financial consulting companies.

Each module is responsible for a single well-defined task, following the **Single Responsibility Principle (SRP)**. This approach improves readability, maintainability, testability, scalability, and code reuse.

The architecture separates the project into independent components that communicate through clearly defined inputs and outputs, allowing each module to evolve without affecting the rest of the system.

---

### Directory Structure

```text
market-risk-track/
│
├── app/
│   └── dashboard.py                 # Streamlit application
│
├── data/
│   ├── raw/                         # Raw downloaded market data
│   ├── clean/                       # Cleaned and validated datasets
│   ├── portfolio/                   # Portfolio valuation and returns
│   ├── risk/                        # Historical VaR and Expected Shortfall
│   ├── ewma/                        # EWMA volatility outputs
│   ├── garch/                       # GARCH model outputs
│   ├── gjr_garch/                   # GJR-GARCH outputs
│   ├── backtesting/                 # VaR validation results
│   ├── model_comparison/            # Model comparison metrics
│   └── stress_testing/              # Stress testing scenarios
│
├── docs/                            # Technical documentation
│
├── notebooks/                       # Jupyter notebooks
│
├── src/
│   ├── data_collection/
│   ├── data_cleaning/
│   ├── portfolio/
│   ├── var/
│   ├── volatility/
│   ├── backtesting/
│   ├── stress_testing/
│   └── visualization/
│
├── tests/                           # Unit tests
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Module Responsibilities

Each package has a specific responsibility within the system.

| Module | Responsibility |
|---------|----------------|
| **data_collection** | Downloads market data, benchmark data, company metadata, and risk-free rates from external providers. |
| **data_cleaning** | Cleans, validates, aligns, and preprocesses financial time series before analysis. |
| **portfolio** | Builds portfolios, applies portfolio weights, calculates portfolio value, returns, and profit & loss (P&L). |
| **var** | Implements Historical Simulation Value at Risk (VaR), Expected Shortfall (ES), and rolling risk measures. |
| **volatility** | Implements EWMA, GARCH(1,1), and GJR-GARCH volatility models for volatility scaling. |
| **backtesting** | Validates VaR models using Kupiec, Christoffersen, and Basel Traffic Light tests. |
| **stress_testing** | Simulates historical and hypothetical stress scenarios to evaluate portfolio resilience. |
| **visualization** | Generates interactive charts and figures used throughout the project and dashboard. |

---

## Data Flow

The platform processes information through a sequential pipeline where each module receives the output produced by the previous stage.

| Step | Module |
|------|--------|
| 1 | Data Collection |
| 2 | Data Cleaning |
| 3 | Portfolio Construction |
| 4 | Historical Simulation VaR |
| 5 | EWMA Volatility Scaling |
| 6 | GARCH Volatility Scaling |
| 7 | GJR-GARCH Volatility Scaling |
| 8 | VaR Backtesting |
| 9 | Model Comparison |
| 10 | Stress Testing |
| 11 | Streamlit Dashboard |

---

## Software Engineering Principles

The project architecture follows widely accepted software engineering principles.

### Modularity

Each module performs one specific task and can be developed independently.

### Separation of Concerns

Data collection, portfolio construction, risk estimation, visualization, and validation are implemented in separate packages.

### Reusability

Core functions are implemented once and reused throughout multiple phases of the project.

### Scalability

New risk models, financial instruments, data providers, or visualization components can be integrated with # Data Flow

The platform processes information through a sequential pipeline where each module receives the output produced by the previous stage.

| Step | Module | Purpose |
|------|--------|---------|
| 1 | External Market Data | Retrieve market and benchmark data from financial data providers |
| 2 | Data Collection | Download, validate, and store raw market data |
| 3 | Data Cleaning | Align trading dates, clean prices, and calculate returns |
| 4 | Portfolio Construction | Build portfolio weights, returns, and P&L |
| 5 | Risk Engine | Calculate Historical VaR and Expected Shortfall |
| 6 | Volatility Models | Apply EWMA, GARCH, and GJR-GARCH volatility scaling |
| 7 | Backtesting | Evaluate VaR models using statistical tests |
| 8 | Stress Testing | Assess portfolio performance under historical and hypothetical scenarios |
| 9 | Visualization & Dashboard | Present results through interactive charts and dashboards |


---

## Software Engineering Principles

The project architecture follows widely accepted software engineering principles.

### Modularity

Each module performs one specific task and can be developed independently.

### Separation of Concerns

Data collection, portfolio construction, risk estimation, visualization, and validation are implemented in separate packages.

### Reusability

Core functions are implemented once and reused throughout multiple phases of the project.

### Scalability

New risk models, financial instruments, data providers, or visualization components can be integrated with minimal changes to the existing codebase.

The platform is designed using a modular architecture, making it easy to extend and maintain.

| Component | Extensibility |
|-----------|---------------|
| Risk Models | Add new VaR methodologies or volatility models |
| Financial Instruments | Extend from equities to fixed income, ETFs, commodities, FX, or derivatives |
| Data Providers | Integrate Bloomberg, Refinitiv, WRDS, Alpha Vantage, Polygon, or other APIs |
| Portfolio Models | Support equal-weight, market-cap, factor-based, and optimization strategies |
| Backtesting | Include additional statistical validation methods |
| Stress Testing | Add custom market scenarios and macroeconomic stress events |
| Visualization | Extend dashboards with new charts, reports, and performance metrics |

---

### Testability

Each module can be independently validated through automated unit tests, ensuring correctness and reliability.

### Maintainability

A clear separation of responsibilities simplifies debugging, code reviews, collaboration, and future enhancements.

---

## Why This Architecture?

A market risk platform consists of multiple independent analytical components, including data acquisition, portfolio analytics, volatility estimation, risk measurement, statistical validation, stress testing, and visualization.

Organizing these components into separate modules improves code quality, enables collaborative development, and facilitates future extensions. This modular architecture closely resembles the design principles adopted by professional quantitative risk management systems used in financial institutions.

# Installation & Quick Start

This section explains how to install, configure, and run the **Market Risk Track** platform.

The project is written in **Python** and has been designed to run on Windows, Linux, and macOS.

---

## Prerequisites

Before installing the project, make sure the following software is available on your system:

- Python 3.11 or newer
- Git
- pip
- Virtual Environment (recommended)

Verify your installation:

```bash
python --version
git --version
pip --version
```

---

## Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/Kifuba/Advance-Equity-Portfolio-Risk-Management.git
```

Move into the project directory:

```bash
cd market-risk-track
```

---

## Create a Virtual Environment

Creating a virtual environment is strongly recommended to isolate project dependencies.

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

## Verify the Installation

Check that the main dependencies are installed correctly:

```bash
python -c "import pandas, numpy, matplotlib, plotly, yfinance; print('Installation successful!')"
```

If no errors appear, the project is ready to use.

---

# Quick Start

The project is organized into ten independent phases.

The complete pipeline can be executed using a single command:

```bash
python main.py
```

Alternatively, each phase can be executed independently.

---

## Phase 1 — Data Collection

Downloads market data and creates the initial datasets.

```bash
python main.py phase1
```

---

## Phase 2 — Data Cleaning

Cleans and validates the downloaded financial data.

```bash
python main.py phase2
```

---

## Phase 3 — Portfolio Construction

Builds the investment portfolio and calculates portfolio returns.

```bash
python main.py phase3
```

---

## Phase 4 — Historical Simulation VaR

Calculates Historical Value at Risk and Expected Shortfall.

```bash
python main.py phase4
```

---

## Phase 5 — EWMA Volatility Scaling

Calculates volatility-scaled Historical VaR using the EWMA model.

```bash
python main.py phase5
```

---

## Phase 6 — GARCH Volatility Scaling

Fits a GARCH(1,1) model and calculates GARCH-scaled VaR.

```bash
python main.py phase6
```

---

## Phase 7 — GJR-GARCH Volatility Scaling

Fits a GJR-GARCH model and estimates asymmetric volatility.

```bash
python main.py phase7
```

---

## Phase 8 — VaR Backtesting

Evaluates the performance of the implemented VaR models.

```bash
python main.py phase8
```

---

## Phase 9 — Model Comparison

Compares all implemented risk models.

```bash
python main.py phase9
```

---

## Phase 10 — Stress Testing

Runs historical and hypothetical stress scenarios.

```bash
python main.py phase10
```

---

# Running the Dashboard

After executing the pipeline, launch the interactive dashboard using Streamlit:

```bash
streamlit run dashboard.py
```

If Streamlit is not available in your environment, use:

```bash
python -m streamlit run dashboard.py
```

---

# Running Unit Tests

Execute all automated tests:

```bash
pytest
```

or

```bash
python -m pytest
```

---

# Expected Project Workflow

The platform is developed using widely adopted tools and libraries in quantitative finance, data science, and risk management.

| Category | Technologies |
|----------|--------------|
| Programming Language | Python 3 |
| Data Manipulation | Pandas, NumPy |
| Scientific Computing | SciPy |
| Financial Data | yfinance |
| Statistical Models | statsmodels, arch |
| Data Visualization | Matplotlib, Plotly |
| Interactive Dashboard | Streamlit |
| Testing | pytest |
| Development Environment | Jupyter Notebook, Visual Studio Code |
| Version Control | Git, GitHub |

---

## Project Outputs

After successfully completing the workflow, the platform generates the following outputs.

| Category | Outputs |
|----------|---------|
| Market Data | Clean price matrix, clean return matrix |
| Portfolio Analytics | Portfolio return series, portfolio P&L, portfolio volatility |
| Risk Measures | Historical VaR, EWMA VaR, GARCH VaR, GJR-GARCH VaR, Expected Shortfall |
| Volatility Models | EWMA volatility, GARCH conditional volatility, GJR-GARCH conditional volatility |
| Backtesting | Kupiec Test, Christoffersen Tests, Basel Traffic Light results |
| Stress Testing | Historical and hypothetical stress scenario reports |
| Visualization | Interactive Streamlit dashboard and risk charts |

## Output

After the pipeline finishes successfully, the project generates:

- Clean financial datasets
- Portfolio return series
- Portfolio profit & loss (P&L)
- Historical Value at Risk
- Expected Shortfall
- EWMA volatility estimates
- GARCH volatility estimates
- GJR-GARCH volatility estimates
- Backtesting reports
- Stress testing reports
- Interactive dashboard visualizations