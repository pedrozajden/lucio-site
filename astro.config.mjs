import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://psiquiatra.drluciomoreira.com.br',
  output: 'static',
  devToolbar: { enabled: false },
  // CSS embutido na página: evita um arquivo separado bloqueando a primeira exibição.
  build: { inlineStylesheets: 'always' },
});
