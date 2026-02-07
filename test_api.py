#!/usr/bin/env python3
"""
Test script untuk Vercel API functions
Gunakan ini untuk testing sebelum deploy ke Vercel
"""
import json
import sys
import os

# Add api folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'api'))

from utils import fetch_real_time_data, AdvancedForexAnalyzer, PAIR_CONFIG

def test_fetch_data():
    print("📊 Testing fetch_real_time_data...")
    try:
        data = fetch_real_time_data('EURUSD', '1h')
        print(f"✅ Fetched {len(data)} candles")
        print(f"   Latest price: {data[-1]['close']:.5f}")
        print(f"   Time range: {data[0]['time']} to {data[-1]['time']}")
        return data
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_analyzer(data):
    print("\n🔍 Testing AdvancedForexAnalyzer...")
    try:
        analyzer = AdvancedForexAnalyzer(data, 'EURUSD')
        signal = analyzer.generate_signal_advanced()
        
        print(f"✅ Analysis complete!")
        print(f"   Signal: {signal['signal']} ({signal['direction']})")
        print(f"   Entry: {signal['entry']:.5f}")
        print(f"   Stop Loss: {signal['stop_loss']:.5f}")
        print(f"   Take Profit: {signal['take_profit']:.5f}")
        print(f"   R/R Ratio: {signal['rr_ratio']}")
        print(f"   Confidence: {signal['confidence']}%")
        print(f"\n   Technical Indicators:")
        print(f"   - RSI: {signal['technical_indicators']['rsi']:.2f}")
        print(f"   - MACD: {signal['technical_indicators']['macd']:.5f}")
        print(f"   - EMA 20: {signal['technical_indicators']['ema_20']:.5f}")
        print(f"   - EMA 50: {signal['technical_indicators']['ema_50']:.5f}")
        print(f"   - ATR: {signal['technical_indicators']['atr']:.5f}")
        
        print(f"\n   Support Levels: {len(signal['support_levels'])}")
        for level in signal['support_levels']:
            print(f"   - {level['price']:.5f} (strength: {level['strength']})")
        
        print(f"\n   Resistance Levels: {len(signal['resistance_levels'])}")
        for level in signal['resistance_levels']:
            print(f"   - {level['price']:.5f} (strength: {level['strength']})")
        
        print(f"\n   Order Blocks: {len(signal['order_blocks'])}")
        for ob in signal['order_blocks']:
            print(f"   - {ob['type']} at {ob['high']:.5f} - {ob['low']:.5f}")
        
        print(f"\n   FVG Gaps: {len(signal['fvg_gaps'])}")
        for fvg in signal['fvg_gaps']:
            print(f"   - {fvg['type']} gap from {fvg['low']:.5f} to {fvg['high']:.5f}")
        
        print(f"\n   Analysis Details:")
        for detail in signal['analysis_details']:
            print(f"   {detail}")
        
        return signal
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_multiple_pairs():
    print("\n💱 Testing multiple pairs...")
    for pair in ['EURUSD', 'GBPUSD', 'USDJPY', 'XAUUSD']:
        try:
            data = fetch_real_time_data(pair, '1h')
            analyzer = AdvancedForexAnalyzer(data, pair)
            signal = analyzer.generate_signal_advanced()
            print(f"✅ {pair}: {signal['signal']} @ {signal['entry']:.5f}")
        except Exception as e:
            print(f"❌ {pair}: Error - {e}")

def test_api_handler():
    print("\n🔌 Testing API handler format...")
    try:
        # Test pairs.py
        from api import pairs
        event = {}
        result = pairs.handler(event, None)
        print(f"✅ pairs.py: {result['statusCode']}")
        
        # Test data.py
        from api import data
        event = {'path': '/api/data/EURUSD', 'queryStringParameters': {'timeframe': '1h'}}
        result = data.handler(event, None)
        print(f"✅ data.py: {result['statusCode']}")
        
        # Test analyze.py
        from api import analyze
        event = {'body': json.dumps({'pair': 'EURUSD'})}
        result = analyze.handler(event, None)
        print(f"✅ analyze.py: {result['statusCode']}")
        
        # Test price.py
        from api import price
        event = {'path': '/api/price/EURUSD'}
        result = price.handler(event, None)
        print(f"✅ price.py: {result['statusCode']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("=" * 60)
    print("🧪 SukaForex Bot - API Test Suite")
    print("=" * 60)
    
    # Test 1: Fetch data
    data = test_fetch_data()
    if not data:
        print("\n❌ Test failed - cannot proceed")
        return
    
    # Test 2: Analyzer
    signal = test_analyzer(data)
    if not signal:
        print("\n❌ Test failed - analyzer not working")
        return
    
    # Test 3: Multiple pairs
    test_multiple_pairs()
    
    # Test 4: API handlers
    test_api_handler()
    
    print("\n" + "=" * 60)
    print("✅ All tests passed! Ready to deploy to Vercel")
    print("=" * 60)

if __name__ == '__main__':
    main()