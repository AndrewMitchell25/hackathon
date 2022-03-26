from website.templates import create_app
from flask import Flask, render_template, request, redirect, session
import sqlite3,pandas

app = create_app()




if __name__ == '__main__':
    app.run(debug=True)