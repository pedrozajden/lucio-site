"""Guarda os campos clínicos originais (ID027–ID030) de uma página de condição do site antigo, sem alterar referências.

Uso: python scripts/guardar-originais-condicao.py transtorno-de-ansiedade-generalizada-tag tag
"""
from pathlib import Path
import json, sys
from lxml import html

slug, name = sys.argv[1], sys.argv[2]
site = Path(__file__).resolve().parent.parent
records = json.loads((site.parent/'planejamento/evidencias/html-estruturado.json').read_text('utf-8'))
record = next(r for r in records if r['arquivo'].endswith(f'/enfermidades/{slug}.html'))

def blocks(fragment):
    root = html.fragment_fromstring(fragment, create_parent='div')
    return [html.tostring(child, encoding='unicode', method='html').strip() for child in root]

fields = {'oQueE':'ID027','sintomasDiagnostico':'ID028','tratamento':'ID029','atendimento':'ID030'}
data = {'origem':record['arquivo'],'versao':'Dados dinâmicos ID027–ID030; palavras e espaços internos originais.'}
data.update({key:blocks(record['dynamic'][field]) for key, field in fields.items()})
data['campos'] = {field:record['dynamic'][field] for field in fields.values()}
target = site/f'src/content/originais/{name}.json'
target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')
print(target.name, {key:len(data[key]) for key in fields})
