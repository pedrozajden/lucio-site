# Alterações e omissões para revisão médica — redesign

Situação: cortes e reescritas autorizados pelo usuário; revisão médica das formulações abaixo pendente. Originais clínicos em src/content/depressao.json; biografia, trajetória e campos HTML em src/content/originais/fontes-redesign.json. Redação proposta em src/content/redesign.json.

- **Abertura e títulos:** “Depressão” → “Avaliação psiquiátrica da depressão”, conforme pedido. “Como é o atendimento?” passa a rótulo de “Cuidado individualizado, com escuta e acompanhamento.”; “O que é?” → “O que é a depressão?”; “Sintomas e Diagnóstico” → “Sintomas e diagnóstico”; “Tratamento” → “Abordagens de tratamento”. Novos rótulos: “O atendimento”, “O médico”, “Formação e trajetória”, “Entenda a depressão”, “Sinais e avaliação”, “Informações gerais” e “Consultório em Nova Lima”. “Medicamentoso” e “Complementares” passam a minúsculas nos subtítulos.

- **Atendimento — ID030:** primeira frase mantida; demais parágrafos condensados em três aspectos. “O psiquiatra realiza uma avaliação completa, identificando…” → “são avaliados…”, mantendo sintomas, fatores desencadeantes e impacto na rotina e nas relações. “Com base nessa análise” → “Com base na avaliação”; “prescrição de medicamentos” → “medicamentos”. Menção à psicoterapia retirada da descrição do consultório e mantida no conteúdo geral de tratamento, para não apresentar oferta local não confirmada. Confiança e empatia condensadas em “O acompanhamento se apoia em uma relação terapêutica baseada na confiança e na empatia, para que o paciente se sinta ouvido, acolhido e compreendido.” Omitidos objetivos de redução/prevenção/bem-estar e o parágrafo final de perspectivas de recuperação.

- **Apresentação do médico:** as três frases da biografia do primeiro piloto foram substituídas por formação e experiência factual. Graduação em Medicina, UniBH, 2019; Residência Médica em Psiquiatria, IPSEMG, 2023; e atuação como residente externo, IPq HC-FMUSP, vêm de sobre.html, elemento 1988729254. Itens separados em título, instituição e ano, sem novos dados. “Com mais de cinco anos de experiência, ele se destaca por sua atuação em diversos níveis de assistência, incluindo…” → “Sua experiência inclui…”, retirando contagem e “se destaca”. “Ele também atuou em instituições renomadas, como…” → “Atuou no Instituto Assistencial André Luiz e na Clínica Novos Rumos.” (biografia, elemento 1730812416). Omitidos superlativos, outros vínculos, atualização/congressos, pesquisa e frases promocionais. Preservada a condição de **residente externo**.

- **Definição — ID027:** primeiro parágrafo integral. Omitidos o parágrafo de apresentação/formação do médico e o parágrafo sobre controle de sintomas e recuperação de motivação, energia e prazer em viver.

- **Sintomas — ID028:** introdução e sete primeiros itens integrais. O oitavo item virou orientação destacada: “Em casos graves, ideias de morte ou pensamentos suicidas, que exigem atenção médica imediata.” → “Em casos graves, ideias de morte ou pensamentos suicidas exigem atenção médica imediata.” Retirados somente “, que”, mantendo gravidade e orientação. Diagnóstico integral, sob “O diagnóstico é clínico”.

- **Medicamentos — ID029:** explicação condensada em três parágrafos, mantendo neurotransmissores cerebrais, serotonina/noradrenalina/dopamina, classes mais prescritas, nomes completos e siglas ISRS/IRSN e acompanhamento regular indispensável para doses, resposta e efeitos adversos. Omitidas “ajudando a restabelecer o equilíbrio químico e reduzir os sintomas” e “garantindo segurança e eficácia”. “As classes mais prescritas incluem” → “Entre as classes mais prescritas estão”; retirada a repetição de “os” antes do segundo grupo de inibidores. Travessões dos exemplos de neurotransmissores substituídos por vírgula.

- **Psicoterapia e complementares — ID029:** primeira frase da psicoterapia integral, incluindo Terapia Cognitivo-Comportamental (TCC) e padrões de pensamento. Omitida a segunda frase, sobre habilidades, autoestima e relacionamentos. Parágrafo de recursos complementares integral, incluindo mindfulness e terapia ocupacional. Omitido o parágrafo final sobre recuperação emocional/funcional, trabalho, relações e atividades. Introdução integral, incluindo “sempre individualizado”, “depende” e “em alguns casos”.

- **Escopo do atendimento:** nova nota “As informações abaixo descrevem abordagens gerais de tratamento. O atendimento apresentado nesta página é a consulta e o acompanhamento psiquiátrico.” Esclarece o escopo sem afirmar oferta local de psicoterapia ou recursos complementares.

- **Localização e contato:** identificação regional separada em “Psiquiatra em Belo Horizonte e Nova Lima” e “Presencial e online”, a partir das informações existentes. Endereço e registros mantidos. “Contato” é o rótulo curto do botão no celular. “Informações de contato em atualização.” permanece. Números divergentes, WhatsApp, formulário, FAQ e depoimentos continuam omitidos. A legenda do vaso foi retirada junto da imagem; legendas atuais identificam somente o médico e registros existentes.

## Refinamento solicitado em 06/10/2026

As entradas acima documentam o primeiro redesign. Esta revisão altera somente os pontos abaixo; a versão anterior está em `historico/redesign-v1`. Revisão médica pendente.

- **Experiência antes da formação:** a frase “Atuou no Instituto Assistencial André Luiz e na Clínica Novos Rumos.” passa a um item próprio, sob “Psiquiatra assistente”. Acrescentados, a partir de sobre.html, elemento 1988729254: “Trabalho em ambulatórios dos municípios de Raposos e Nova Lima.” (original: “Trabalho em ambulatórios municipais: Municípios de Raposos e Nova Lima.”) e “Atuação no tratamento da dependência química no Centro de Atenção Psicossocial Álcool e Drogas (CAPS AD) de Nova Lima-MG.” (original separado em título e instituição). São informações de trajetória, sem afirmar oferta desses serviços no consultório. A lista de plantões e os demais trechos antes omitidos continuam fora do piloto.
- **Títulos:** “Formação e trajetória” → “Experiência e formação”; adicionado “Formação e trajetória acadêmica” sobre os três itens existentes, e “Sintomas mais comuns” acima da introdução e lista. Dados acadêmicos, sintomas e diagnóstico permanecem com as mesmas palavras.
- **Escopo da consulta:** substituída a nota “As informações abaixo descrevem abordagens gerais de tratamento. O atendimento apresentado nesta página é a consulta e o acompanhamento psiquiátrico.” por “Na consulta com o Dr. Lúcio, é realizada uma avaliação para o diagnóstico psiquiátrico e a elaboração de um plano terapêutico individualizado. Ele também pode orientar tratamentos complementares, conforme as necessidades de cada paciente.”, sob “Na consulta com o Dr. Lúcio”. A primeira frase se apoia em ID030 (avaliação completa e plano personalizado); a possibilidade de orientação complementar foi expressamente solicitada pelo usuário e se relaciona às explicações de ID029. Mantida separadamente a frase “As informações abaixo descrevem abordagens gerais de tratamento.” Não se afirma oferta de psicoterapia ou dos recursos complementares pelo médico.

Os novos negritos são marcação visual de trechos literais. Não alteram palavras ou ressalvas; a orientação de atenção médica imediata permanece integral.

## Nova ordem e redução de elementos auxiliares — 06/10/2026

- Omitidos os rótulos acima dos títulos: “Atendimento psiquiátrico”, “Como é o atendimento?”, “Experiência e formação”, “Entenda a depressão”, “Sinais e avaliação” e “Informações gerais”. Retirados também “Modalidades” e o rótulo repetido “Atendimento presencial e online” no encerramento; modalidades e atendimento psiquiátrico continuam identificados nos textos existentes. Nenhum trecho clínico foi omitido ou reescrito nesta revisão.
- Retirados os números 01, 02 e 03 dos aspectos do atendimento. Os títulos e textos desses aspectos foram mantidos.

A versão anterior está guardada em `historico/refinamento-v2`. Mudanças de ordem, espaçamento e composição não alteraram a redação clínica.


## Ajuste das fotografias e ação do hero — 06/10/2026

- Retirado o link auxiliar “Conheça o atendimento” da abertura, conforme pedido do usuário. O conteúdo e o botão de agendamento do atendimento permanecem. Nenhuma mudança na redação clínica. Composição anterior guardada em `historico/fotos-v5`.
