from app import create_app

app = create_app()

if __name__ == "__main__":
    print("🚀 Tentando rodar o Flask...")
    app.run(debug=False)