// Páginas de condição publicadas. `area` é a posição do item em home.json → areas.
export const conditionPages = [
  { key: 'depressao', area: 0, href: '/enfermidades/depressao/', label: 'Depressão', cta: 'Conheça a página sobre depressão' },
  { key: 'tag', area: 1, href: '/enfermidades/transtorno-de-ansiedade-generalizada-tag/', label: 'Ansiedade generalizada (TAG)', cta: 'Conheça a página sobre ansiedade' },
] as const;

export type ConditionKey = (typeof conditionPages)[number]['key'];

export const pageForArea = (area: number) => conditionPages.find(page => page.area === area);

// Destino de todos os botões de agendamento das páginas de condição e do WhatsApp flutuante (informado pelo usuário em 13/10/2026).
export const scheduleUrl = 'https://api.cqc.onpromedia.com.br/t/2F04D22F';
