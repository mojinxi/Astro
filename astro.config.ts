import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import compress from 'astro-compress';
import rehautolinkheadings from 'rehype-autolink-headings';
import rehypeSlug from 'rehype-slug';

// https://astro.build/config
export default defineConfig({
  site: 'https://astro.pages.dev', // 你的博客线上地址，可以暂时留空或改成你的 Cloudflare 域名
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
    sitemap(),
    compress(),
  ],
  markdown: {
    rehypePlugins: [
      rehypeSlug,
      [
        rehautolinkheadings,
        {
          behavior: 'wrap',
          properties: { class: 'anchor' },
        },
      ],
    ],
  },
  output: 'static',
  build: {
    inlineStylesheets: 'auto',
  },
});