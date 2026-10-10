import os
import time
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))
if base_dir:
    os.chdir(base_dir)

arquivos_monitorados = ['dados.json', 'template.html', 'build.py']

def obter_ultima_modificacao():
    return max(os.path.getmtime(f) for f in arquivos_monitorados if os.path.exists(f))

def main():
    print("👀 Assistindo alterações... (dados.json, template.html, build.py)")
    print("Sempre que você der Ctrl+S, o index.html será atualizado automaticamente!")
    print("Pressione Ctrl+C para parar.\n")
    
    ultima_modificacao = obter_ultima_modificacao()
    
    try:
        while True:
            time.sleep(1)
            atual_modificacao = obter_ultima_modificacao()
            
            if atual_modificacao != ultima_modificacao:
                print("🔄 Alteração detectada! Reconstruindo index.html...")
                subprocess.run(['python3', 'build.py'])
                print("✅ index.html atualizado!\n")
                ultima_modificacao = atual_modificacao
    except KeyboardInterrupt:
        print("\n🛑 Monitoramento encerrado.")

if __name__ == "__main__":
    main()
