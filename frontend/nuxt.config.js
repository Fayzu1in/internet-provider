export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,
  server: {
    host: '0.0.0.0',
  },

  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'InternetBor',
    meta: [
      {
        name: 'google-site-verification',
        content: '0a76CzZjBr7v3xmjGOLGOs8Jo33YILh6k_BzV6FhUwU',
      },
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
      {
        name: 'facebook-domain-verification',
        content: 'bs9wgi0jk16c0fwcpv4oornl557m9e',
      },
    ],
    link: [
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap',
      },
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'preload',
        as: 'font',
        crossorigin: 'anonymous',
        type: 'font/ttf',
        href: '/fonts/LitteraTextLight.ttf',
      },
      {
        rel: 'preload',
        as: 'font',
        crossorigin: 'anonymous',
        type: 'font/ttf',
        href: '/fonts/LilitaOne-Regular.ttf',
      },
      // {
      //   rel: 'stylesheet',
      //   href: 'https://unpkg.com/@splidejs/splide@2.x/dist/css/splide.min.css',
      // },
    ],
    __dangerouslyDisableSanitizers: ['script'],
    script: [
      // {
      //   src: '//code.jivo.ru/widget/nDlol3Uq8s',
      //   async: true,
      // },
      {
        hid: 'call-tracking',
        src: 'https://cc.calltracking.ru/phone.e15e1.14025.async.js',
        async: true,
        defer: true,
        type: 'text/javascript',
        body: true,
      },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['@/assets/css/global.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '@/plugins/ymapPlugin.js', mode: 'client' },
    '~/plugins/glide.client.js',
    '~plugins/preloader.client.js',
    '~/plugins/maska.js',
    '~/plugins/i18n.js',
    '~/plugins/api.js',
    `~/plugins/facebookPixel.js`,

    // '~/plugins/splide.client.js',
    // '~/plugins/swiper.client.js',
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/axios',
    '@nuxtjs/i18n',
    '@nuxtjs/gtm',
  ],
  gtm: {
    // enabled: true,
    id: 'GTM-TQ2W9RP',
    pageTracking: true, // Enable page tracking
    scriptDefer: true, // Defer loading of GTM script
  },
  i18n: {
    locales: [
      {
        code: 'ru',
        file: 'ru.json',
        iso: 'ru-RU',
      },
      {
        code: 'uz',
        file: 'uz.json',
        iso: 'uz-UZ',
      },
      {
        code: 'en',
        file: 'en.json',
        iso: 'en-US',
      },
    ],
    langDir: 'lang/',
    defaultLocale: 'ru',
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en',
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
}
