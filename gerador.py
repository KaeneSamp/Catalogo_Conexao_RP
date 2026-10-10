"""
Wrapper de compatibilidade retroativa para gerador.py.
Agora aponta e executa o pipeline blindado de build.py.
"""
import os
import build

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if base_dir:
        os.chdir(base_dir)
        
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = build.json.load(f)
        
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(build.gerar_html(dados))
        
    with open("ids.md", "w", encoding="utf-8") as f:
        f.write(build.gerar_md(dados))
