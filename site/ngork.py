from pyngrok import ngrok

def make_tunnel(port: str) -> str:
    return ngrok.connect(port=port)

print(make_tunnel('8501').public_url)