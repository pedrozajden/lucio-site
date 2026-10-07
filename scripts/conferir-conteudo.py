"""Confere originais, trechos mantidos e limites do piloto; não substitui revisão médica."""
from pathlib import Path
import hashlib, json, re
from lxml import html

SITE = Path(__file__).resolve().parent.parent
ROOT = SITE.parent
page = html.fromstring((SITE/'dist/enfermidades/depressao/index.html').read_text('utf-8'))
original = json.loads((SITE/'src/content/depressao.json').read_text('utf-8'))
copy = json.loads((SITE/'src/content/redesign.json').read_text('utf-8'))
saved = json.loads((SITE/'src/content/originais/fontes-redesign.json').read_text('utf-8'))

def norm(text): return re.sub(r'\s+', ' ', text).strip()
def plain(fragment):
    root = html.fragment_fromstring(fragment, create_parent='div')
    return norm(' '.join(e.text_content() for e in root))
def selected(attribute, key):
    return page.xpath(f'//*[@{attribute}="{key}"]')[0]
def paragraphs(node):
    return norm(' '.join(p.text_content() for p in node.xpath('.//p')))

mapping = {'oQueE':'ID027','sintomasDiagnostico':'ID028','tratamento':'ID029','atendimento':'ID030'}
for key, field in mapping.items():
    assert plain(' '.join(original[key])) == plain(saved['clinico']['campos'][field]), f'Original alterado: {key}'
retained = ['oQueE.0','sintomasDiagnostico.0','tratamento.0','tratamento.6']
for key in retained:
    field, index = key.split('.')
    assert norm(selected('data-original',key).text_content()) == plain(original[field][int(index)])
assert paragraphs(selected('data-original','diagnosis')) == norm(' '.join(plain(p) for p in original['sintomasDiagnostico'][2:]))
source_items = html.fromstring(original['sintomasDiagnostico'][1]).xpath('//li')
rendered_items = selected('data-original','symptoms').xpath('./li')
assert len(rendered_items) == 7
assert [norm(li.text_content()) for li in rendered_items] == [norm(li.text_content()) for li in source_items[:7]]
warning = norm(selected('data-copy','emergency').text_content())
assert warning == copy['emergency']
for phrase in ['Em casos graves','ideias de morte','pensamentos suicidas','atenção médica imediata']:
    assert phrase in warning and phrase in source_items[7].text_content()
for key in ['careIntro','experience','treatmentNote','treatmentScope','psychotherapy']:
    assert norm(selected('data-copy',key).text_content()) == norm(copy[key])
for i, step in enumerate(copy['careSteps']):
    assert norm(selected('data-copy',f'careSteps.{i}').text_content()) == step['text']
assert paragraphs(selected('data-copy','medication')) == ' '.join(copy['medication'])
source_trajectory = norm(saved['trajetoria']['texto'])
source_bio = norm(saved['biografia']['texto'])
assert copy['experience'].split('inclui ')[1].rstrip('.') in source_bio
for i, item in enumerate(copy['experienceDetails']):
    row = selected('data-experience', str(i))
    assert norm(row.xpath('./p')[1].text_content()) == item['text']
assert all(term in source_trajectory for term in ['Raposos e Nova Lima','CAPS AD','Instituto Assistencial André Luiz','Clínica Novos Rumos'])
assert page.xpath('//*[@class="experience-block"]/following-sibling::*[@class="formation-block"]')
assert not page.xpath('//*[contains(@class,"brand-curve")]')
assert page.xpath('//*[@data-copy="treatmentNote"]//strong')
for i, item in enumerate(copy['profile']):
    row = selected('data-profile',str(i))
    assert norm(row.xpath('./p')[0].text_content()) == item['text']
    assert item['text'].rstrip('.') in source_trajectory
    if 'detail' in item:
        assert item['detail'] in source_trajectory
assert len(page.xpath('//h1')) == 1
assert norm(page.xpath('//h1')[0].text_content()) == copy['heroTitle']
assert not page.xpath('//main//script | //iframe | //form')
assert len(page.xpath('//header[contains(@class,"shared-header")]')) == 1
assert len(page.xpath('//script')) == 1  # Somente o menu compartilhado local.
assert all(not src or src.startswith('/_astro/') for src in page.xpath('//script/@src'))
assert len(page.xpath('//main//img')) == 2
assert not any('composicao-editorial' in src for src in page.xpath('//img/@src'))
assert page.xpath('//meta[@name="robots"]/@content') == ['noindex, nofollow']
assert all(url.startswith('#') for url in page.xpath('//main//a/@href'))
for url in page.xpath('//a/@href'):
    path, _, fragment = url.partition('#')
    if not path:
        target_page = page
    else:
        assert path in ['/', '/enfermidades/depressao/'], f'Destino não implementado: {url}'
        target_path = SITE/'dist'/path.strip('/')/'index.html'
        target_page = html.fromstring(target_path.read_text('utf-8'))
    if fragment:
        assert target_page.xpath(f'//*[@id="{fragment}"]'), f'Âncora inexistente: {url}'
ctas = page.xpath('//a[contains(string(.),"Agende uma consulta")]')
assert len(ctas) == 4 and all(x.get('href') == '#contato' for x in ctas)
assert not any(term in html.tostring(page,encoding='unicode') for term in ['wa.me','tintim.link','98998-0356','9541-0374'])

manifest = json.loads((ROOT/'planejamento/evidencias/manifesto-referencias.json').read_text('utf-8'))
for item in manifest:
    path = ROOT/item['arquivo']
    assert path.is_file()
    assert path.stat().st_size == item['bytes']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], f'Referência alterada: {path}'

report = {
    'originaisClinicosPreservados':list(mapping),
    'trechosMantidosConferidos':retained+['diagnóstico integral','7 itens da lista de sintomas'],
    'atencaoMedicaImediata':warning,
    'formacaoConferidaNaFonte':'sobre.html, elemento 1988729254',
    'experienciaClinicaConferida':'biografia e trajetória; apresentada antes da formação',
    'fotosReaisNaPagina':2,
    'botoesContato':len(ctas),
    'scriptsLocaisDeNavegacao':len(page.xpath('//script')),
    'formulariosIframes':0,
    'linksExternos':0,
    'referenciasInalteradas':len(manifest),
    'revisaoMedicaDosResumos':'pendente; alterações e omissões registradas separadamente'
}
target = SITE/'validacao/conteudo.json'
target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

