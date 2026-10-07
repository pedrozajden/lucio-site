# Dr. Lúcio Moreira — Home e piloto de Depressão

Site em Astro com saída estática. Home em `/` e piloto em `/enfermidades/depressao/`. Scripts locais cuidam apenas de navegação, animações e carrossel. Sem rastreamento ou integração de contato; o formulário da Home está desabilitado. `noindex, nofollow` está presente durante a revisão.

Repositório: https://github.com/pedrozajden/lucio-site. Somente a implementação está versionada; referências, dependências, capturas de conferência e arquivos temporários permanecem fora do Git. O envio ao GitHub não ativa automaticamente uma hospedagem.

Configuração para a conexão existente na Cloudflare: branch `main`, diretório raiz do repositório, comando `pnpm build` e diretório de saída `dist`. Node 24 e pnpm 11.19.0 são as versões indicadas nos arquivos do projeto. Formulário e rastreamento continuam desativados na prévia web.

Para Cloudflare **Workers Builds** (o projeto atual), use build `pnpm build` e deploy `pnpm exec wrangler deploy`. O arquivo `wrangler.jsonc` publica apenas os arquivos estáticos de `dist`, sem código de servidor. O comando `pnpm run deploy` pode ser usado para compilar e publicar em uma única etapa. A dependência `workerd` tem seu script de instalação permitido explicitamente em `pnpm-workspace.yaml`.

```sh
pnpm install
pnpm dev
pnpm build
pnpm preview
```

Os textos clínicos originais estão preservados em `src/content/depressao.json`. `src/content/originais/fontes-redesign.json` guarda também a biografia e a trajetória acadêmica com suas origens. O redesign utiliza trechos originais e textos condensados separados em `src/content/redesign.json`. As referências permanecem somente para leitura.

Alterações e omissões para revisão médica estão em `ALTERACOES-DE-TEXTO.md`. A versão anterior do piloto está guardada em `historico/piloto-v1`. A composição atual usa duas fotografias reais; a imagem de IA do vaso está fora da página. Os canais de contato precisam ser confirmados antes de qualquer integração ou publicação.

`scripts/conferir-conteudo.py` verifica a preservação dos originais, os trechos mantidos, a orientação de atenção imediata e os limites do contato provisório. A revisão médica do sentido dos resumos permanece humana.
