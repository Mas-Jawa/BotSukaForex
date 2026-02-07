import json
from datetime import datetime
from utils import PAIR_CONFIG, fetch_real_time_data
import yfinance as yf

def handler(event, context):
    """Get current price for a pair"""
    try:
        # Parse query parameters
        path = event.get('path', '')
        pair = path.split('/')[-1] if '/' in path else 'EURUSD'
        
        # Try to get real-time price
        try:
            symbol = PAIR_CONFIG[pair]['symbol']
            ticker = yf.Ticker(symbol)
            info = ticker.history(period='1d', interval='1m')
            
            if not info.empty:
                current_price = float(info['Close'].iloc[-1])
                return {
                    'statusCode': 200,
                    'headers': {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                        'Access-Control-Allow-Headers': 'Content-Type'
                    },
                    'body': json.dumps({
                        'pair': pair,
                        'price': current_price,
                        'timestamp': datetime.now().isoformat()
                    })
                }
        except:
            pass
        
        # Fallback to cached or mock data
        data = fetch_real_time_data(pair)
        current_price = data[-1]['close']
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'pair': pair,
                'price': current_price,
                'timestamp': datetime.now().isoformat()
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }