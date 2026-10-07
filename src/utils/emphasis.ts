// Destaca trechos literais sem mudar palavras ou permitir HTML no texto-base.
const escapeHtml = (text: string) => text.replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]!));
const escapeRegex = (text: string) => text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

export function emphasize(text: string, phrases: string[] = []): string {
  const escaped = escapeHtml(text);
  if (!phrases.length) return escaped;
  const pattern = phrases.map(phrase => escapeRegex(escapeHtml(phrase))).join('|');
  return escaped.replace(new RegExp(pattern, 'g'), match => `<strong>${match}</strong>`);
}
