import json
from utils import fetch_real_time_data, AdvancedForexAnalyzer

def handler(event, context):
    """Analyze market and generate trading signal"""
    try:
        # Parse request body
        body = event.get('body', '{}')
        if isinstance(body, str):
            body = json.loads(body)
        
        pair = body.get('pair', 'EURUSD')
        market_data = body.get('data')
        
        # Fetch data if not provided
        if not market_data:
            market_data = fetch_real_time_data(pair)
        
        analyzer = AdvancedForexAnalyzer(market_data, pair)
        signal = analyzer.generate_signal_advanced()
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps(signal)
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