import json
from utils import fetch_real_time_data

def handler(event, context):
    """Get market data for a specific pair"""
    try:
        # Parse query parameters
        path = event.get('path', '')
        pair = path.split('/')[-1] if '/' in path else 'EURUSD'
        
        # Parse query string for timeframe
        query_string = event.get('queryStringParameters', {}) or {}
        timeframe = query_string.get('timeframe', '1h')
        
        data = fetch_real_time_data(pair, timeframe)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps(data)
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