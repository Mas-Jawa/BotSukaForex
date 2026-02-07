// WebSocket Module for Real-time Updates
// NOTE: WebSocket/SocketIO is disabled for Vercel serverless deployment
// Real-time updates are not supported in serverless functions
class WebSocketManager {
    constructor() {
        this.socket = null;
        this.listeners = [];
        this.isConnected = false;
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 5;
    }

    connect() {
        // Disabled for Vercel serverless deployment
        console.log('WebSocket is disabled for Vercel serverless deployment');
        this.isConnected = true;
        this.notifyListeners({ type: 'connected' });
    }

    setupEventHandlers() {
        // Disabled for Vercel serverless deployment
    }

    subscribeToPair(pair) {
        // Disabled for Vercel serverless deployment
        console.log(`Subscribe to ${pair} - WebSocket disabled`);
    }

    onMessage(callback) {
        this.listeners.push(callback);
        return () => {
            this.listeners = this.listeners.filter(l => l !== callback);
        };
    }

    notifyListeners(message) {
        this.listeners.forEach(listener => listener(message));
    }

    disconnect() {
        this.isConnected = false;
    }

    getConnectionStatus() {
        return this.isConnected;
    }
}

// Export WebSocket instance
const websocket = new WebSocketManager();