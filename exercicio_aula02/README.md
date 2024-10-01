# Como executar
Para executar esse código é necessário ter o Python instalado e criar a venv usando o comando:

```
python -m venv venv
```

Depois, basta ativar a venv usando o comando:

- Windows: `source venv/Scripts/activate`
- Linux/macOS: `source venv/bin/activate`

Com a venv ativada, podemos instalar o FastAPI e Uvicorn usando o comando:

```
pip install fastapi uvicorn
```

Para rodar a aplicação, use o comando:

```
uvicorn main:app --reload
```