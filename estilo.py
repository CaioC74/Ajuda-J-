# -*- coding: utf-8 -*-
"""Visual do app: CSS, ícones (SVG embutido) e o pouco de JavaScript que o
navegador exige para voz (falar e ouvir). Nada é baixado da internet."""

_ICONES = {
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "gift": '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 0 1 0 5"/>',
    "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "home": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    "help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    "sliders": '<line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/>',
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "mic": '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/>',
    "volume": '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "bookmark": '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>',
    "alert": '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    "right": '<polyline points="9 18 15 12 9 6"/>',
    "chevron-left": '<polyline points="15 18 9 12 15 6"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "search": '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "check": '<polyline points="20 6 9 17 4 12"/>',
    "check-circle": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    "type": '<polyline points="4 7 4 4 20 4 20 7"/><line x1="9" y1="20" x2="15" y2="20"/><line x1="12" y1="4" x2="12" y2="20"/>',
    "contrast": '<circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 0 20z" fill="currentColor"/>',
    "layout": '<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="9" x2="9" y2="21"/>',
    "refresh": '<polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/>',
    "x-circle": '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>',
    "landmark": '<line x1="3" y1="22" x2="21" y2="22"/><line x1="6" y1="18" x2="6" y2="11"/><line x1="10" y1="18" x2="10" y2="11"/><line x1="14" y1="18" x2="14" y2="11"/><line x1="18" y1="18" x2="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    "clipboard": '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "send": '<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>',
    "edit": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
}


def ic(nome, classe=""):
    """Devolve um ícone SVG (usa a cor do texto)."""
    return ('<svg class="ic ' + classe + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            + _ICONES[nome] + '</svg>')


CSS = """
*{box-sizing:border-box}
:root{--bg:#f4f4f4;--card:#fff;--txt:#1a1a1a;--mut:#525252;--pri:#1d4ed8;--pri-t:#fff;--bd:#b5b5b5;--grey:#d9d9d9;--grey-t:#111;--head:#fff;--sel:#eff6ff;--lin:#dcdcdc;
--ok-bg:#d1fae5;--ok-t:#065f46;--ok-bd:#34d399;--info-bg:#eff6ff;--info-bd:#93c5fd;--info-t:#1e40af;--bad-bg:#fee2e2;--bad-bd:#f87171;--bad-t:#991b1b;--warn-bg:#fef3c7;--warn-bd:#f59e0b;--warn-t:#92400e}
body.contraste{--bg:#000;--card:#000;--txt:#fff;--mut:#fff;--pri:#ffe600;--pri-t:#000;--bd:#fff;--grey:#1f1f1f;--grey-t:#fff;--head:#000;--sel:#1a1a00;--lin:#fff;
--ok-bg:#000;--ok-t:#7dffb0;--ok-bd:#7dffb0;--info-bg:#000;--info-bd:#fff;--info-t:#fff;--bad-bg:#000;--bad-bd:#ff8a8a;--bad-t:#ff8a8a;--warn-bg:#000;--warn-bd:#ffe600;--warn-t:#ffe600}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:"Inter","Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif;background:#101827;color:var(--txt);line-height:1.35}
a{color:inherit}
.celular{width:100%;max-width:430px;margin:0 auto;height:100vh;height:100dvh;display:flex;flex-direction:column;background:var(--bg);overflow:hidden;position:relative}
@media (min-width:520px){body{padding:20px 0}.celular{height:min(880px,calc(100vh - 40px));border-radius:34px;border:8px solid #000;box-shadow:0 20px 60px rgba(0,0,0,.55)}}
.topo{display:flex;align-items:center;gap:.6rem;padding:.55rem 1rem;background:var(--head);border-bottom:1px solid var(--lin);flex:0 0 auto;min-height:3.4rem}
.topo .titulo{font-size:1.1rem;font-weight:700}
.topo .pg{font-size:1.1rem}
.voltar{display:inline-flex;width:2.8rem;height:2.8rem;align-items:center;justify-content:center;border-radius:.8rem;color:var(--txt);text-decoration:none;margin-left:-.6rem}
.logo{width:2rem;height:2rem;border-radius:.55rem;background:var(--pri);color:var(--pri-t);display:inline-flex;align-items:center;justify-content:center;font-weight:800;flex:0 0 auto}
.marca{color:var(--pri);font-weight:800;font-size:1.15rem}
.marca small{font-size:.62rem;color:var(--mut);font-weight:500;margin-left:.3rem}
.prog{background:var(--head);padding:.6rem 1rem .8rem;border-bottom:1px solid var(--lin);flex:0 0 auto}
.prog-t{display:flex;justify-content:space-between;font-size:.85rem;color:var(--mut);margin-bottom:.35rem}
.prog-t b{color:var(--pri)}
.prog-b{height:.6rem;background:#d4d4d4;border-radius:1rem;overflow:hidden}
.prog-b i{display:block;height:100%;background:var(--pri)}
.tela{flex:1 1 auto;overflow-y:auto;padding:1rem;-webkit-overflow-scrolling:touch}
.nav{flex:0 0 auto;display:flex;background:var(--head);border-top:1px solid var(--lin)}
.nav a{flex:1;display:flex;flex-direction:column;align-items:center;gap:.15rem;padding:.5rem .2rem .45rem;color:var(--mut);text-decoration:none;font-size:.75rem;font-weight:600;position:relative;border-top:3px solid transparent}
.nav a.ativo{color:var(--pri);border-top-color:var(--pri)}
.nav .ic{width:1.5rem;height:1.5rem}
.nav .n{position:absolute;top:.25rem;left:calc(50% + .5rem);background:#dc2626;color:#fff;border-radius:1rem;min-width:1.15rem;height:1.15rem;padding:0 .25rem;font-size:.68rem;display:flex;align-items:center;justify-content:center}
h1.t{font-size:1.5rem;margin:.2rem 0 .4rem;line-height:1.2}
h2.t{font-size:1.1rem;margin:1.2rem 0 .6rem}
p.sub{color:var(--mut);margin:0 0 1rem}
.ic{width:1.35rem;height:1.35rem;flex:0 0 auto}
.card{background:var(--card);border:1.5px solid var(--bd);border-radius:1rem;padding:1rem;margin-bottom:.75rem}
a.card{display:block;text-decoration:none}
.menu-card{display:flex;align-items:center;gap:.9rem;background:var(--card);border:1.5px solid var(--bd);border-radius:1rem;padding:.85rem 1rem;margin-bottom:.7rem;text-decoration:none;min-height:4.6rem}
.menu-card .tx{flex:1;min-width:0}
.menu-card strong{display:block;font-size:1.2rem}
.menu-card span.s{color:var(--mut);font-size:.88rem;line-height:1.25;display:block}
.caixa-ico{width:3.3rem;height:3.3rem;border-radius:.9rem;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.caixa-ico .ic{width:1.7rem;height:1.7rem}
.azul{background:#dbeafe;color:#1d4ed8}.verde{background:#d1fae5;color:#047857}.roxo{background:#ede9fe;color:#6d28d9}.cinza{background:#e5e7eb;color:#374151}
body.contraste .caixa-ico{background:#000;border:2px solid #fff;color:#fff}
.btn{display:flex;align-items:center;justify-content:center;gap:.5rem;min-height:3.3rem;padding:.6rem 1rem;border-radius:.9rem;font:inherit;font-weight:700;font-size:1.05rem;border:2px solid var(--bd);background:var(--grey);color:var(--grey-t);text-decoration:none;width:100%;cursor:pointer;text-align:center;margin-bottom:.65rem}
.btn.pri{background:var(--pri);border-color:var(--pri);color:var(--pri-t)}
.btn.claro{background:var(--card);color:var(--txt)}
.btn.sel{background:var(--pri);border-color:var(--pri);color:var(--pri-t)}
.linha-btn{display:flex;gap:.65rem}.linha-btn>*{flex:1}
.linha-btn .btn{font-size:.95rem;padding:.5rem .4rem}
.btn-mini{display:inline-flex;align-items:center;gap:.4rem;min-height:2.6rem;padding:.35rem .8rem;border-radius:.8rem;border:1.5px solid var(--bd);background:var(--card);color:var(--txt);font:inherit;font-weight:700;font-size:.9rem;text-decoration:none;cursor:pointer}
.btn-mini .ic{width:1.15rem;height:1.15rem}
.ferr{display:flex;gap:.5rem;justify-content:flex-end;margin-bottom:.8rem}
.link{background:none;border:0;color:var(--txt);text-decoration:underline;font:inherit;font-size:.9rem;cursor:pointer;padding:.5rem 0}
.centro{text-align:center}
.caixa{display:flex;gap:.65rem;align-items:flex-start;border-radius:.9rem;padding:.8rem 1rem;border:1.5px solid;margin-bottom:.75rem}
.caixa .ic{margin-top:.1rem}
.caixa.info{background:var(--info-bg);border-color:var(--info-bd);color:var(--info-t)}
.caixa.ok{background:var(--ok-bg);border-color:var(--ok-bd);color:var(--ok-t)}
.caixa.ruim{background:var(--bad-bg);border-color:var(--bad-bd);color:var(--bad-t)}
.caixa.atencao{background:var(--warn-bg);border-color:var(--warn-bd);color:var(--warn-t)}
.caixa strong{display:block}
.opt{display:flex;align-items:center;gap:.6rem;padding:.7rem .75rem;border:2px solid var(--bd);border-radius:.85rem;background:var(--card);min-height:3.3rem;font-weight:600;cursor:pointer}
.opt input{width:1.4rem;height:1.4rem;flex:0 0 auto;accent-color:var(--pri)}
.opt:has(input:checked){border-color:var(--pri);background:var(--sel)}
.opt.grande{padding:.9rem 1rem;margin-bottom:.65rem;font-size:1.05rem}
.opt.grande small{display:block;color:var(--mut);font-weight:500}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.6rem;margin-bottom:1rem}
.grid2 .opt{font-size:.86rem;padding:.55rem .4rem;gap:.35rem;overflow-wrap:break-word;line-height:1.2}
.grid2 .opt input{width:1.15rem;height:1.15rem}
.chip{white-space:nowrap;display:inline-block;font-size:.75rem;font-weight:700;padding:.12rem .5rem;border-radius:.4rem;background:var(--grey);color:var(--grey-t);margin-right:.3rem}
.chip.ok{background:var(--ok-bg);color:var(--ok-t);border:1px solid var(--ok-bd)}
.chip.tag{background:#dbeafe;color:#1e40af}
.chip.aviso{background:var(--warn-bg);color:var(--warn-t);border:1px solid var(--warn-bd)}
body.contraste .chip.tag{background:#000;color:#fff;border:1px solid #fff}
.vaga h3{margin:0 0 .15rem;font-size:1.15rem}
.vaga .emp{color:var(--mut);margin-bottom:.45rem}
.vaga .linha{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap;font-size:.95rem}
.vaga .topo-v h3{flex:1;min-width:0}
.vaga .topo-v{display:flex;justify-content:space-between;gap:.5rem;align-items:flex-start}
.info-l{display:flex;gap:.7rem;margin:.75rem 0}
.info-l .ic{color:var(--pri);margin-top:.15rem}
.info-l small{display:block;color:var(--mut);font-size:.82rem}
.info-l b{font-size:1.02rem}
.busca{display:flex;gap:.5rem;margin-bottom:.8rem}
.busca{flex-wrap:wrap}
.busca input{flex:1 1 9rem;min-width:0}
input[type=text],input[type=search],textarea{font:inherit;padding:.75rem .9rem;border:2px solid var(--bd);border-radius:.85rem;background:var(--card);color:var(--txt);width:100%;min-height:3.1rem}
textarea{min-height:6rem;resize:vertical}
label.rot{display:block;font-weight:700;margin:.9rem 0 .35rem}
.contagem{color:var(--mut);margin:.2rem 0 .7rem}
.chat{display:flex;gap:.6rem;align-items:flex-start;margin-bottom:.9rem}
.avatar{width:2.5rem;height:2.5rem;border-radius:50%;background:var(--pri);color:var(--pri-t);display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.balao{background:var(--card);border:1.5px solid var(--bd);border-radius:1rem;padding:.8rem 1rem;font-size:1.05rem}
.balao.eu{background:var(--sel);border-color:var(--pri);margin-left:auto}
.resp{display:flex;justify-content:space-between;align-items:center;gap:.5rem;padding:1rem;border:2px solid var(--bd);border-radius:.9rem;background:var(--card);margin-bottom:.65rem;text-decoration:none;font-weight:600;font-size:1.05rem;min-height:3.5rem}
.sw{width:3.3rem;height:1.95rem;border-radius:2rem;background:#cfcfcf;position:relative;flex:0 0 auto;display:inline-block;border:2px solid #8f8f8f}
.sw::after{content:"";position:absolute;top:.17rem;left:.17rem;width:1.35rem;height:1.35rem;border-radius:50%;background:#fff;transition:left .15s}
.sw.on{background:var(--pri);border-color:var(--pri)}
.sw.on::after{left:1.5rem}
body.contraste .sw{background:#333;border-color:#fff}
body.contraste .sw.on{background:#ffe600;border-color:#ffe600}
body.contraste .sw::after{background:#fff}
body.contraste .sw.on::after{background:#000}
a.card.linha-sw{display:flex;align-items:center;gap:.8rem;text-decoration:none}
.linha-sw .ic{color:var(--pri)}
.linha-sw .tx{flex:1;min-width:0}
.linha-sw strong{display:block;font-size:1.05rem}
.linha-sw small{color:var(--mut);font-size:.88rem}
.linha-sw .est{display:flex;flex-direction:column;align-items:center;gap:.15rem;font-size:.7rem;font-weight:700;color:var(--mut)}
.tamanhos{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem;margin-top:.7rem}
.tamanhos a{display:flex;flex-direction:column;align-items:center;gap:.3rem;text-decoration:none;font-weight:600;font-size:.88rem}
.tamanhos a b{display:flex;width:100%;align-items:center;justify-content:center;min-height:3.6rem;border-radius:.9rem;background:var(--grey);color:var(--grey-t);border:2px solid var(--bd)}
.tamanhos a.sel b{background:var(--pri);border-color:var(--pri);color:var(--pri-t)}
.exemplo{margin-top:.8rem;padding:.7rem .9rem;border-radius:.8rem;background:var(--sel);border:1.5px dashed var(--pri);font-weight:600}
a.card.aviso-card{display:flex;gap:.8rem;align-items:flex-start;text-decoration:none}
.aviso-card.novo{background:var(--info-bg);border-color:var(--info-bd)}
.aviso-card .tx{flex:1;min-width:0}
.aviso-card strong{display:block;font-size:1.05rem}
.aviso-card .q{color:var(--mut);font-size:.8rem;margin-top:.2rem}
.ponto{width:.7rem;height:.7rem;border-radius:50%;background:var(--pri);flex:0 0 auto;margin-top:.5rem}
.aviso-ic{color:#7c4a2d}
body.contraste .aviso-ic{color:#fff}
.mapa{position:relative;height:8.5rem;border:1.5px solid var(--bd);border-radius:.9rem;background:#d9d9d9;overflow:hidden;display:flex;align-items:center;justify-content:center;margin-bottom:.75rem;color:var(--pri)}
body.contraste .mapa{background:#1f1f1f}
.mapa .x{position:absolute;inset:0;width:100%;height:100%;stroke:#b3b3b3;stroke-width:1;fill:none}
.mapa .x line{vector-effect:non-scaling-stroke}
.mapa .ic{width:2.4rem;height:2.4rem;position:relative}
.mapa .rotulo{position:absolute;bottom:.55rem;left:50%;transform:translateX(-50%);background:#fff;border:1px solid #bbb;border-radius:.6rem;padding:.25rem .7rem;font-size:.82rem;white-space:nowrap;color:#222}
.passos3{display:grid;grid-template-columns:repeat(3,1fr);gap:.55rem;margin:1.2rem 0 1.5rem;text-align:center;font-size:.8rem}
.passos3 .ph{position:relative;height:4.3rem;background:#d9d9d9;border:1.5px solid #bbb;border-radius:.5rem;display:flex;align-items:center;justify-content:center;color:#555;overflow:hidden;margin-bottom:.5rem}
.passos3 .ph .x{position:absolute;inset:0;width:100%;height:100%;stroke:#bbb;fill:none}
.passos3 .ph .x line{vector-effect:non-scaling-stroke}
.passos3 .ph .ic{position:relative;width:1.8rem;height:1.8rem}
.passos3 .num{display:inline-flex;width:1.8rem;height:1.8rem;border-radius:50%;background:var(--pri);color:var(--pri-t);font-weight:700;align-items:center;justify-content:center;margin-bottom:.3rem}
.logo-g{width:5rem;height:5rem;border-radius:1.2rem;background:var(--pri);color:var(--pri-t);display:flex;align-items:center;justify-content:center;font-size:2.8rem;font-weight:800;margin:1rem auto .8rem;box-shadow:0 0 30px rgba(29,78,216,.35)}
.spin{width:4rem;height:4rem;border:.4rem solid #d4d4d4;border-top-color:var(--pri);border-radius:50%;animation:g 1s linear infinite;margin:0 auto 1.2rem}
@keyframes g{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.spin{animation:none}}
details.acc{background:var(--card);border:1.5px solid var(--bd);border-radius:.9rem;margin-bottom:.6rem}
details.acc[open]{border-color:var(--pri)}
details.acc summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;padding:.9rem 1rem;font-weight:700;font-size:1.05rem;min-height:3.3rem}
details.acc summary::-webkit-details-marker{display:none}
details.acc[open] summary{color:var(--pri)}
details.acc[open] summary .ic{transform:rotate(90deg)}
details.acc .corpo{padding:.8rem 1rem 1rem;border-top:1px solid var(--lin)}
ul.ok{list-style:none;margin:0;padding:0}
ul.ok li{display:flex;gap:.5rem;margin:.45rem 0}
ul.ok .ic{color:var(--pri);width:1.15rem;height:1.15rem;margin-top:.15rem}
ul.pontos{margin:.3rem 0 0;padding-left:1.2rem}
ul.pontos li{margin:.35rem 0}
.rodape-nota{font-size:.82rem;color:var(--mut);text-align:center;margin:1rem 0 .3rem}
.aviso-js{position:absolute;left:1rem;right:1rem;bottom:5rem;background:#111;color:#fff;border-radius:.8rem;padding:.7rem 1rem;z-index:20;font-size:.95rem;border:2px solid #fff}
.aviso-js[hidden]{display:none}
.gravando{outline:3px solid #dc2626;outline-offset:2px}
.simples .nao-simples{display:none!important}
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid #f59e0b;outline-offset:2px}
.dash{font-size:.9rem}
.dash code{background:#e5e7eb;padding:.1rem .3rem;border-radius:.3rem;color:#111}
"""

JS = """
(function(){
  function norm(t){return (t||'').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');}
  var aviso=document.getElementById('aviso-js');
  function mostrarAviso(msg){
    if(!aviso){return;}
    aviso.textContent=msg;aviso.hidden=false;
    clearTimeout(mostrarAviso.t);
    mostrarAviso.t=setTimeout(function(){aviso.hidden=true;},5000);
  }
  function falar(texto){
    if(!('speechSynthesis' in window)){mostrarAviso('Este aparelho não consegue ler em voz alta.');return false;}
    window.speechSynthesis.cancel();
    var u=new SpeechSynthesisUtterance(texto);
    u.lang='pt-BR';u.rate=0.9;
    window.speechSynthesis.speak(u);
    return true;
  }
  var SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  function ouvir(botao,aoTerminar){
    if(!SR){mostrarAviso('Este navegador não entende voz. Use a opção Escrever.');return;}
    var r=new SR();
    r.lang='pt-BR';r.interimResults=false;r.maxAlternatives=1;
    botao.classList.add('gravando');
    mostrarAviso('Pode falar, estou ouvindo...');
    r.onresult=function(ev){aoTerminar(ev.results[0][0].transcript);};
    r.onerror=function(){mostrarAviso('Não consegui ouvir. Tente de novo ou escreva.');};
    r.onend=function(){botao.classList.remove('gravando');};
    try{r.start();}catch(e){mostrarAviso('Não consegui ligar o microfone.');}
  }
  document.addEventListener('click',function(e){
    var o=e.target.closest('[data-ouvir]');
    if(o){
      e.preventDefault();
      var alvo=o.getAttribute('data-ouvir');
      var texto=alvo==='tela'?document.getElementById('conteudo').innerText:alvo;
      falar(texto);
      return;
    }
    var f=e.target.closest('[data-falar]');
    if(f){
      e.preventDefault();
      var modo=f.getAttribute('data-falar');
      ouvir(f,function(fala){
        if(modo==='pergunta'){
          window.location.href='/ajuda/pergunta?q='+encodeURIComponent(fala);
        }else if(modo==='campo'){
          var c=document.getElementById(f.getAttribute('data-campo'));
          if(c){c.value=(c.value?c.value+' ':'')+fala;}
          mostrarAviso('Entendi: '+fala);
        }else if(modo==='vagas'){
          var t=norm(fala),achou=0;
          document.querySelectorAll('input[data-chaves]').forEach(function(i){
            var ps=i.getAttribute('data-chaves').split(' ');
            for(var k=0;k<ps.length;k++){
              if(ps[k]&&t.indexOf(ps[k])>=0){i.checked=true;achou++;break;}
            }
          });
          mostrarAviso(achou?('Entendi: '+fala):'Não entendi o trabalho. Toque nas opções ou tente de novo.');
        }
      });
    }
  });
  var corpo=document.body;
  if(corpo.getAttribute('data-autoler')==='1'){
    window.addEventListener('load',function(){
      var h=document.querySelector('#conteudo h1');
      if(h){try{falar(h.innerText);}catch(e){}}
    });
  }
})();
"""
