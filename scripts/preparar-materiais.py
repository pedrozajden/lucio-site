"""Lê referências e escreve apenas derivados locais em site-novo."""
from pathlib import Path
import json, re, shutil
from lxml import html, etree
from PIL import Image, ImageOps

SITE = Path(__file__).resolve().parent.parent
ROOT = SITE.parent
REF = ROOT / 'referencia-site-antigo/Site antigo - Save all Resources'
SOURCE = REF / 'www.drluciomoreira.com.br/enfermidades/depressao.html'
record = next(x for x in json.loads((ROOT/'planejamento/evidencias/html-estruturado.json').read_text('utf-8')) if x['arquivo'].endswith('/enfermidades/depressao.html'))
def normalize(s): return re.sub(r'\s+', ' ', s).strip()
def safe_html(e):
    # Only semantic paragraph/list/emphasis tags. No platform styles or scripts.
    allowed = {'p','ul','ol','li','strong','em','b','i','br'}
    def render(n):
        import html as escape
        children = escape.escape(n.text or '')
        for c in n:
            children += render(c) + escape.escape(c.tail or '')
        if n.tag not in allowed: return children
        if n.tag == 'br': return '<br>'
        return f'<{n.tag}>{children}</{n.tag}>'
    return render(e)
def blocks(field):
    d=html.fragment_fromstring(record['dynamic'][field],create_parent='div')
    return [safe_html(e) for e in d if normalize(e.text_content())]

data = {'origem': str(SOURCE.relative_to(ROOT)).replace('\\','/'), 'versao':'Dados dinâmicos ID027–ID030; palavras e espaços internos originais.', 'oQueE':blocks('ID027'), 'sintomasDiagnostico':blocks('ID028'), 'tratamento':blocks('ID029'), 'atendimento':blocks('ID030')}
bio = next(x for x in record['blocks'] if x['id']=='1730812416')
full_bio = normalize(html.fromstring(bio['html']).text_content())
sentences = [
    'Ao longo de sua carreira, Dr. Lúcio ampliou seus conhecimentos como residente externo no Instituto de Psiquiatria do Hospital das Clínicas da Faculdade de Medicina da Universidade de São Paulo (IPq HC-FMUSP).',
    'Dr. Lúcio é comprometido com a atualização contínua, participando regularmente de congressos, simpósios e jornadas de psiquiatria.',
    'Ele acredita que cada paciente é único e merece um atendimento personalizado, focado no bem-estar e na recuperação.',
]
for sentence in sentences: assert sentence in full_bio, sentence
data['biografiaCurta']=sentences
target=SITE/'src/content/depressao.json';target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')

assets=SITE/'public/assets';assets.mkdir(parents=True,exist_ok=True)
shutil.copyfile(REF/'irp.cdn-website.com/050761bd/dms3rep/multi/logo-h.svg',assets/'logo-horizontal.svg')
shutil.copyfile(REF/'irp.cdn-website.com/050761bd/dms3rep/multi/sub.svg',assets/'monograma.svg')
font_sources = {
    'gotu-regular.ttf':'irp.cdn-website.com/050761bd/fonts/Gotu-Regular-186c_400.ttf',
    'belanosima-regular.ttf':'irp.cdn-website.com/050761bd/fonts/Belanosima-Regular-9299_400.ttf',
    'montserrat-regular.woff2':'irp.cdn-website.com/fonts/s/montserrat/v31/JTUSjIg1_i6t8kCHKm459Wlhyw.woff2',
}
for name,path in font_sources.items():shutil.copyfile(REF/path,assets/name)
photo=ROOT/'Arquivos para site novo - Fotos e Logo/Fotos Site/Foto perfil Lucio (1).jpg'
with Image.open(photo) as original:
    im=ImageOps.exif_transpose(original).convert('RGB')
    for width in [480,800,1200]:
        im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS).save(assets/f'dr-lucio-{width}.webp',quality=86,method=6)
print('Quatro blocos clínicos e três frases da biografia extraídos; marca, fontes e uma foto real preparadas localmente.')
