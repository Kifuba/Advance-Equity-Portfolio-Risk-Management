"""
Data Loader

Loads all datasets generated during Phase 1 (Data Collection).
These datasets are the inputs for the Data Cleaning pipeline.
"""

from pathlib import Path 
import pandas as pd 

PHASE1_DATA_DIR = Path('data/raw')
def load_adjusted_price() -> pd.DataFrame: #load adjusted closing prices
    file_path = PHASE1_DATA_DIR / "adjusted_close_price.parquet"
    if not file_path.exists():
        raise FileNotFoundError(f"Required PHASE 1 output not found : {file_path}")
    prices = pd.read_parquet(file_path)
    return prices 

def load_simple_returns() -> pd.DataFrame: #Load simple returns generated during Phase 1.
    file_path = PHASE1_DATA_DIR / "simple_returns.parquet"
    if not file_path.exists():
        raise FileNotFoundError(f"Required PHASE1 output not found : {file_path}")
    simple_returns = pd.read_parquet(file_path)
    return simple_returns

def load_log_returns() -> pd.DataFrame:
    file_path = PHASE1_DATA_DIR / "log_returns.parquet"
    if not file_path.exists():
        raise FileNotFoundError(f" Required PHASE 1 output not found : {file_path}")
    log_returns = pd.read_parquet(file_path)
    return log_returns

def load_portfolio_weights() -> pd.DataFrame:
    file_path = PHASE1_DATA_DIR / "portfolio_weights.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Required PHASE 1 output not found : {file_path}")
    portfolio_weights = pd.read_csv(file_path)
    return portfolio_weights


def load_benchmark_prices() -> pd.DataFrame:
    file_path = PHASE1_DATA_DIR / "benchmark_prices.parquet"
    if not file_path.exists():
        raise FileNotFoundError(f"Required PHASE 1 output not found : {file_path}")
    benchmark_prices = pd.read_parquet(file_path)
    return benchmark_prices

def load_benchmark_returns() -> pd.DataFrame:
  file_path = PHASE1_DATA_DIR / "benchmark_returns.parquet"
  if not file_path.exists():
    raise FileNotFoundError(f"Required PHASE 1 output not found : {file_path}")
  benchmark_returns = pd.read_parquet(file_path)
  return benchmark_returns

def load_sector_information() -> pd.DataFrame:
    file_path = PHASE1_DATA_DIR / "sector_information.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Required PHASE 1 output not found : {file_path}")
    sector_information = pd.read_csv(file_path)
    return sector_information

def load_risk_free_rates() -> pd.DataFrame:
    file_path = PHASE1_DATA_DIR / "risk_free_rate.parquet"
    if not file_path.exists():
        raise FileNotFoundError(f"Required PHASE 1 output not found : {file_path}")
    risk_free_rate  = pd.read_parquet(file_path)
    return risk_free_rate
