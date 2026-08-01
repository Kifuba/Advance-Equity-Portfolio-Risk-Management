import pandas as pd 


def align_trading_calendar(

        prices: pd.DataFrame ,

        benchmark: pd.DataFrame


):
    
       """
  Align portfolio assets and benchmark to the same trading calendar .

       """
       common_dates = prices.index.intersection(benchmark.index)
       aligned_prices = prices.loc[common_dates]
       aligned_benchmark = benchmark.loc[common_dates]

       return aligned_prices,aligned_benchmark

def validate_calendar(

         prices: pd.DataFrame ,
        benchmark: pd.DataFrame
):

        """
  Validate that portfolio and benchmark share the same trading calendar .

        """

        if not isinstance(prices.index,pd.DatetimeIndex):
         raise TypeError("POrtfolio index must be a DatatimeIndex")
        if not isinstance(benchmark.index, pd.DatetimeIndex):
         raise TypeError("Benchmark index must be a DatatimeIndex")
        if len(prices) != len(benchmark):
         raise ValueError("Portfolio and benchmark have different numbers of observation")
        if not prices.index.equals(benchmark.index):
         raise ValueError("Portfolio and benchmark have different trading dates.")
        if not prices.index.is_monotonic_increasing:
         raise ValueError("Portfolio dates are not sorted in chronological order")
        if not benchmark.index.is_monotonic_increasing:
         raise ValueError("Benchmark dates are not sorted in chronological order")





    

