module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
    // 'vue/setup-compiler-macros': true,
  },
  parserOptions: {
    parser: '@babel/eslint-parser',
    requireConfigFile: false,
  },
  extends: ['@nuxtjs', 'plugin:nuxt/recommended', 'prettier'],
  // plugins: [],
  // add your custom rules here
  overrides: [
    {
      files: ['pages/**/*.vue', 'layouts/**/*.vue'],
      rules: { 'vue/multi-word-component-names': 'off' },
    },
  ],
}
