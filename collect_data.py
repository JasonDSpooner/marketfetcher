import yfinance as yf
import pandas as pd
from datetime import datetime

def collect_market_data():
    # List of stocks/indices to track
    symbols = [
        '^GSPC',  # S&P 500
        '^DJI',   # Dow Jones
        '^IXIC',  # NASDAQ
    ]
    
    data = []
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period='1d')
        
        if not hist.empty:
            data.append({
                'Symbol': symbol,
                'Date': datetime.now().strftime('%Y-%m-%d'),
                'Open': hist['Open'].iloc[-1],
                'High': hist['High'].iloc[-1],
                'Low': hist['Low'].iloc[-1],
                'Close': hist['Close'].iloc[-1],
                'Volume': hist['Volume'].iloc[-1],
                'Daily_Change': hist['Close'].iloc[-1] - hist['Open'].iloc[-1],
                'Daily_Change_Pct': ((hist['Close'].iloc[-1] - hist['Open'].iloc[-1]) / hist['Open'].iloc[-1]) * 100
            })
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(data)
    filename = f'market_data_{datetime.now().strftime("%Y%m%d")}.csv'
    df.to_csv(filename, index=False)
    
    # Create a plot-friendly CSV for Jenkins Plot plugin
    plot_df = df[['Symbol', 'Daily_Change_Pct']]
    plot_df.to_csv('plot_data.csv', index=False)

if __name__ == '__main__':
    collect_market_data()