from flask import Flask, request, render_template, jsonify
import yfinance as yf
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

app = Flask(__name__)

class Bourse(BoxLayout):
    def __init__(self, **kwargs):
        super(Bourse, self).__init__(**kwargs)

    @app.route("/quote")

    def display_quote():
        symbol = request.args.get('symbol', default="AAPL")
        quote = yf.Ticker(symbol)
        return jsonify(quote.info)

    @app.route("/history")
    def display_history():
        symbol = request.args.get('symbol', default="AAPL")
        period = request.args.get('period', default="1y")
        interval = request.args.get('interval', default="1mo")
        quote = yf.Ticker(symbol)   
        hist = quote.history(period=period, interval=interval)
        data = hist.to_json()
        return data

    @app.route("/")
    def home():
        return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)