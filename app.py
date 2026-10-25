# -*- coding: utf-8 -*-
"""Ajuda Já - protótipo funcional (Python 3, só biblioteca padrão).

Como rodar:   python app.py
Depois abra:  http://localhost:8000  (o endereço aparece no terminal)
"""
import argparse
import socket
import sys
import traceback
import webbrowser
from http import cookies
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

import rotas


class Manipulador(BaseHTTPRequestHandler):
    server_version = "AjudaJa/1.0"

    def log_message(self, formato, *args):
        pass  # terminal limpo

    def _sid(self):
        c = cookies.SimpleCookie()
        try:
            c.load(self.headers.get("Cookie", ""))
        except cookies.CookieError:
            return ""
        return c["sid"].value if "sid" in c else ""

    def do_GET(self):
        self._tratar("GET")

    def do_POST(self):
        self._tratar("POST")

    def _tratar(self, metodo):
        partes = urlsplit(self.path)
        q = parse_qs(partes.query, keep_blank_values=True)
        corpo = {}
        if metodo == "POST":
            try:
                n = min(int(self.headers.get("Content-Length") or 0), 20000)
            except ValueError:
                n = 0
            corpo = parse_qs(self.rfile.read(n).decode("utf-8", "replace"), keep_blank_values=True)
        sid, s, novo = rotas.obter_sessao(self._sid())
        try:
            status, tipo, conteudo = rotas.despachar(metodo, partes.path, q, corpo, s, self.path, sid)
        except Exception:
            traceback.print_exc()
            status, tipo, conteudo = 500, "html", "<h1>Algo deu errado no app.</h1><p><a href='/inicio'>Voltar ao início</a></p>"
        self.send_response(status)
        if novo:
            self.send_header("Set-Cookie", "sid=" + sid + "; Path=/; HttpOnly; SameSite=Lax")
        if tipo == "redir":
            self.send_header("Location", conteudo)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        dados = conteudo.encode("utf-8")
        if tipo == "html":
            self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(dados)))
        self.end_headers()
        if metodo != "HEAD" and dados:
            self.wfile.write(dados)


def ip_da_rede():
    """Descobre o IP do computador na rede (para abrir no celular)."""
    try:
        t = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        t.connect(("10.255.255.255", 1))  # não envia nada; só descobre a interface
        ip = t.getsockname()[0]
        t.close()
        return ip
    except OSError:
        return None


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description="Protótipo Ajuda Já")
    ap.add_argument("--porta", type=int, default=8000, help="porta inicial (padrão: 8000)")
    ap.add_argument("--rede", action="store_true", help="deixa abrir também no celular, na mesma rede Wi-Fi")
    ap.add_argument("--sem-navegador", action="store_true", help="não abre o navegador sozinho")
    args = ap.parse_args()

    host = "0.0.0.0" if args.rede else "127.0.0.1"
    servidor = None
    for porta in range(args.porta, args.porta + 20):
        try:
            servidor = ThreadingHTTPServer((host, porta), Manipulador)
            break
        except OSError:
            continue
    if servidor is None:
        print("Não consegui abrir nenhuma porta entre %d e %d." % (args.porta, args.porta + 19))
        sys.exit(1)

    url = "http://localhost:%d" % porta
    print("")
    print("  Ajuda Já - protótipo funcionando")
    print("  No computador, abra:  " + url)
    if args.rede:
        ip = ip_da_rede()
        if ip:
            print("  No celular (mesmo Wi-Fi):  http://%s:%d" % (ip, porta))
    else:
        print("  (Para abrir também no celular, rode:  python app.py --rede)")
    print("  Painel do facilitador:  " + url + "/teste")
    print("  Para parar: Ctrl + C")
    print("")
    if not args.sem_navegador:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\n  Até logo!")
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
