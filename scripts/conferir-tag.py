"""Confere a página de TAG: originais preservados, trechos literais, ressalvas e limites do piloto; não substitui revisão médica."""
from pathlib import Path
import json, re
from lxml import html

SITE = Path(__file__).resolve().parent.parent
page = html.fromstring((SITE/'dist/enfermidades/transtorno-de-ansiedade-generalizada-tag/index.html').read_text('utf-8'))
original = json.loads((SITE/'src/content/originais/tag.json').read_text('utf-8'))
copy = json.loads((SITE/'src/content/tag.json').read_text('utf-8'))
records = json.loads((SITE.parent/'planejamento/evidencias/html-estruturado.json').read_text('utf-8'))
record = next(r for r in records if r['arquivo'].endswith('/enfermidades/transtorno-de-ansiedade-generalizada-tag.html'))

def norm(text): return re.sub(r'\s+', ' ', text).strip()
def plain(fragment): return norm(html.fragment_fromstring(fragment, create_parent='div').text_content())
def selected(attribute, key):
    found = page.xpath(f'//*[@{attribute}="{key}"]')
    assert len(found) == 1, f'{attribute}={key}: {len(found)}'
    return found[0]

# Originais guardados batem com a captura do site antigo.
for key, field in {'oQueE':'ID027','sintomasDiagnostico':'ID028','tratamento':'ID029','atendimento':'ID030'}.items():
    assert plain(''.join(original[key])) == plain(record['dynamic'][field]), f'Original alterado: {key}'
# Trechos literais.
for key in ['oQueE.0','sintomasDiagnostico.0','sintomasDiagnostico.3','sintomasDiagnostico.4','tratamento.0','tratamento.9','tratamento.11']:
    field, index = key.split('.')
    assert norm(selected('data-original', key).text_content()) == plain(original[field][int(index)]), key
items = selected('data-original','sintomasDiagnostico.1').xpath('./li')
assert [norm(li.text_content()) for li in items] == [norm(li.text_content()) for li in html.fromstring(original['sintomasDiagnostico'][1]).xpath('//li')]
# Textos condensados exibidos como registrados.
assert norm(selected('data-copy','heroLead').text_content()) == copy['heroLead']
assert norm(selected('data-copy','psychotherapy').text_content()) == copy['psychotherapy']
assert norm(' '.join(p.text_content() for p in selected('data-copy','medication').xpath('.//p'))) == ' '.join(copy['medication'])
for i, step in enumerate(copy['careSteps']):
    assert norm(selected('data-copy', f'careSteps.{i}').text_content()) == step['text']
# Ressalvas e sentido preservados.
source_medication = plain(original['tratamento'][3])
for sentence in copy['medication']:
    assert sentence.rstrip('.') in source_medication, sentence  # A pedido do usuário, a 2ª frase termina em "rigoroso" (ver ALTERACOES-DE-TEXTO.md).
for term in ['ansiolíticos de curta duração', 'acompanhamento médico rigoroso']:
    assert term in ' '.join(copy['medication'])
assert not selected('data-copy','medication').xpath('.//strong')
assert copy['psychotherapy'] in plain(original['tratamento'][6])
# Limites do piloto.
markup = html.tostring(page, encoding='unicode')
assert norm(page.xpath('//h1')[0].text_content()) == 'Avaliação psiquiátrica da ansiedade generalizada'
assert page.xpath('//meta[@name="robots"]/@content') == ['noindex, nofollow']
assert not page.xpath('//main//script | //iframe | //form')
assert len(page.xpath('//script')) == 2
assert len(page.xpath('//main//img')) == 2
assert not page.xpath('//*[contains(@class,"cond-emergency")]')
assert not any(term in markup for term in ['wa.me','tintim.link','98998-0356','9541-0374'])
SCHEDULE = 'https://api.cqc.onpromedia.com.br/t/2F04D22F'
ctas = page.xpath('//a[contains(string(.),"Agende uma consulta")]')
assert len(ctas) == 5 and all(a.get('href') == SCHEDULE for a in ctas)
assert not [u for u in page.xpath('//a/@href') if u.startswith('http') and u != SCHEDULE]
for url in page.xpath('//a/@href'):
    if url == SCHEDULE: continue
    path, _, fragment = url.partition('#')
    target = page
    if path:
        file = SITE/'dist'/path.strip('/')/'index.html' if path != '/' else SITE/'dist/index.html'
        assert file.is_file(), f'Destino inexistente: {url}'
        target = html.fromstring(file.read_text('utf-8'))
    if fragment:
        assert target.xpath(f'//*[@id="{fragment}"]'), f'Âncora inexistente: {url}'
print(json.dumps({'trechosLiterais':7,'sintomas':len(items),'condensados':['heroLead','medication','psychotherapy','careSteps'],'ressalvaAnsioliticos':'acompanhamento médico rigoroso (risco de dependência retirado a pedido do usuário)','avisoDeEmergencia':'ausente, como no original','linksConferidos':len(page.xpath('//a/@href'))}, ensure_ascii=False, indent=2))
