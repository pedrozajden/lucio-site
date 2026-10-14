// Páginas de condição publicadas. `area` é a posição do item em home.json → areas.
export const conditionPages = [
  { key: 'depressao', area: 0, href: '/enfermidades/depressao/', label: 'Depressão', cta: 'Conheça o tratamento para depressão' },
  { key: 'tag', area: 1, href: '/enfermidades/transtorno-de-ansiedade-generalizada-tag/', label: 'Ansiedade generalizada (TAG)', cta: 'Conheça o tratamento para ansiedade' },
  { key: 'tdah', area: 2, href: '/enfermidades/transtorno-de-deficit-de-atencao-e-hiperatividade-tdah/', label: 'TDAH', cta: 'Conheça o tratamento para TDAH' },
  { key: 'bipolar', area: 3, href: '/enfermidades/transtorno-afetivo-bipolar/', label: 'Transtorno bipolar', cta: 'Conheça o tratamento para transtorno bipolar' },
  { key: 'borderline', area: 4, href: '/enfermidades/transtorno-de-personalidade-borderline/', label: 'Transtorno borderline', cta: 'Conheça o tratamento para borderline' },
  { key: 'esquizofrenia', area: 5, href: '/enfermidades/esquizofrenia/', label: 'Esquizofrenia', cta: 'Conheça o tratamento para esquizofrenia' },
] as const;

export type ConditionKey = (typeof conditionPages)[number]['key'];

export const pageForArea = (area: number) => conditionPages.find(page => page.area === area);

// Destino de todos os botões de agendamento das páginas de condição e do WhatsApp flutuante (informado pelo usuário em 13/10/2026).
export const scheduleUrl = 'https://api.cqc.onpromedia.com.br/t/2F04D22F';

// Ordem de exibição das áreas (posições em home.json → areas) no menu e nos cartões da Home: TDAH primeiro.
export const areaOrder = [2, 0, 1, 3, 4, 5];
