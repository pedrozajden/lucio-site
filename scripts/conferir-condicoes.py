"""Confere as páginas de condição feitas sobre o template (exceto o piloto de Depressão, que tem conferência própria).

Para cada página: originais iguais à captura do site antigo, trechos marcados com data-original idênticos ao original,
textos com data-copy iguais aos registrados, ausência de telefones e formulários, agendamento só pelo link informado
e links internos válidos. Não substitui revisão médica.
"""
from pathlib import Path
import json, re
from lxml import html

SITE = Path(__file__).resolve().parent.parent
SCHEDULE = 'https://api.cqc.onpromedia.com.br/t/2F04D22F'
PAGES = {
    'tag': ('transtorno-de-ansiedade-generalizada-tag', 'Avaliação psiquiátrica da ansiedade generalizada'),
    'tdah': ('transtorno-de-deficit-de-atencao-e-hiperatividade-tdah', 'Avaliação psiquiátrica do TDAH'),
    'bipolar': ('transtorno-afetivo-bipolar', 'Avaliação psiquiátrica do transtorno bipolar'),
    'borderline': ('transtorno-de-personalidade-borderline', 'Avaliação psiquiátrica do transtorno de personalidade borderline'),
    'esquizofrenia': ('esquizofrenia', 'Avaliação psiquiátrica da esquizofrenia'),
}
FIELDS = {'oQueE': 'ID027', 'sintomasDiagnostico': 'ID028', 'tratamento': 'ID029', 'atendimento': 'ID030'}
records = json.loads((SITE.parent/'planejamento/evidencias/html-estruturado.json').read_text('utf-8'))
shared = json.loads((SITE/'src/content/redesign.json').read_text('utf-8'))

def bare(text): return re.sub(r'\s+', '', text)
def plain(fragment): return html.fragment_fromstring(fragment, create_parent='div').text_content()

report = {}
for name, (slug, h1) in PAGES.items():
    page = html.fromstring((SITE/f'dist/enfermidades/{slug}/index.html').read_text('utf-8'))
    original = json.loads((SITE/f'src/content/originais/{name}.json').read_text('utf-8'))
    copy = json.loads((SITE/f'src/content/{name}.json').read_text('utf-8'))
    record = next(r for r in records if r['arquivo'].endswith(f'/enfermidades/{slug}.html'))
    for key, field in FIELDS.items():
        assert bare(plain(''.join(original[key]))) == bare(plain(record['dynamic'][field])), f'{name}: original alterado em {key}'
    literal = page.xpath('//*[@data-original]')
    for node in literal:
        field, indexes = node.get('data-original').split('.')
        expected = ''.join(plain(original[field][int(i)]) for i in indexes.split('+'))
        assert bare(node.text_content()) == bare(expected), f'{name}: trecho literal diferente em {node.get("data-original")}'
    copied = page.xpath('//*[@data-copy]')
    for node in copied:
        key = node.get('data-copy')
        if key.startswith('careSteps.'):
            value = copy['careSteps'][int(key.split('.')[1])]['text']
        else:
            value = copy.get(key, shared.get(key))
        assert value is not None, f'{name}: texto sem registro: {key}'
        assert bare(node.text_content()) == bare(' '.join(value) if isinstance(value, list) else value), f'{name}: texto diferente em {key}'
    markup = html.tostring(page, encoding='unicode')
    assert re.sub(r'\s+', ' ', page.xpath('//h1')[0].text_content()).strip() == h1, name
    assert page.xpath('//meta[@name="robots"]/@content') == ['noindex, nofollow']
    assert not page.xpath('//main//script | //iframe | //form')
    assert len(page.xpath('//script')) == 2 and len(page.xpath('//main//img')) == 2
    assert not any(term in markup for term in ['wa.me', 'tintim.link', '98998-0356', '9541-0374'])
    assert not [u for u in page.xpath('//a/@href') if u.startswith('http') and u != SCHEDULE], f'{name}: link externo inesperado'
    ctas = page.xpath('//a[contains(string(.),"Agende uma consulta") or contains(string(.),"Agende uma avaliação")]')
    assert len(ctas) == 6 and all(a.get('href') == SCHEDULE for a in ctas), f'{name}: botões de agendamento'
    assert page.xpath(f'//a[contains(@class,"cond-whatsapp")][@href="{SCHEDULE}"]')
    for url in page.xpath('//a/@href'):
        if url == SCHEDULE: continue
        path, _, fragment = url.partition('#')
        target = page
        if path:
            file = SITE/'dist/index.html' if path == '/' else SITE/'dist'/path.strip('/')/'index.html'
            assert file.is_file(), f'{name}: destino inexistente {url}'
            target = html.fromstring(file.read_text('utf-8'))
        if fragment:
            assert target.xpath(f'//*[@id="{fragment}"]'), f'{name}: âncora inexistente {url}'
    report[name] = {'trechosLiterais': len(literal), 'textosRegistrados': len(copied), 'botoesAgendamento': len(ctas)}

# Dúvidas frequentes: mesmas perguntas e respostas registradas em faq.json, em todas as páginas de condição e na Home.
faq = json.loads((SITE/'src/content/faq.json').read_text('utf-8'))
for file in [SITE/'dist/index.html'] + [SITE/f'dist/enfermidades/{slug}/index.html' for slug, _ in PAGES.values()] + [SITE/'dist/enfermidades/depressao/index.html']:
    doc = html.fromstring(file.read_text('utf-8'))
    items = doc.xpath('//section[@id="duvidas"]//details')
    assert len(items) == len(faq), f'{file}: FAQ ausente'
    for node, item in zip(items, faq):
        assert bare(node.xpath('./summary')[0].text_content()) == bare(item['question'])
        assert bare(node.xpath('.//div[contains(@class,"faq-answer")]')[0].text_content()) == bare(''.join(item['answer']))
    assert 'mesma qualidade' not in doc.text_content()

# Restrições específicas pedidas pelo usuário.
tdah = (SITE/'dist/enfermidades/transtorno-de-deficit-de-atencao-e-hiperatividade-tdah/index.html').read_text('utf-8').lower()
assert 'crianças' not in tdah and 'adolescentes' not in tdah, 'TDAH: menção a crianças ou adolescentes'
for name in PAGES:
    text = html.fromstring((SITE/f'dist/enfermidades/{PAGES[name][0]}/index.html').read_text('utf-8')).text_content().lower()
    for promise in ['é possível controlar a doença', 'ampla experiência', 'ampla atuação', 'garantem segurança']:
        assert promise not in text, f'{name}: {promise}'
print(json.dumps(report, ensure_ascii=False, indent=2))
