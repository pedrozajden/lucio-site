"""Guarda textos originais para a revisão do redesign, sem alterar referências."""
from pathlib import Path
import json
from lxml import html

site = Path(__file__).resolve().parent.parent
records = json.loads((site.parent/'planejamento/evidencias/html-estruturado.json').read_text('utf-8'))
depression = next(r for r in records if r['arquivo'].endswith('/enfermidades/depressao.html'))
about = next(r for r in records if r['arquivo'].endswith('/sobre.html'))

def capture(record, identifier):
    block = next(b for b in record['blocks'] if b['id'] == identifier)
    return {'origem':record['arquivo'],'elemento':identifier,'html':block['html'],'texto':html.fromstring(block['html']).text_content()}

data = {
    'biografia':capture(depression, '1730812416'),
    'trajetoria':capture(about, '1988729254'),
    'clinico':{'origem':depression['arquivo'],'campos':{key:depression['dynamic'][key] for key in ['ID027','ID028','ID029','ID030']}}
}
target = site/'src/content/originais/fontes-redesign.json'
target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')
print('Biografia, trajetória e quatro campos clínicos originais guardados para revisão.')
