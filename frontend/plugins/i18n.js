export default function ({ app }) {
  app.nuxt.defaultTransition.beforeEnter = () => {
    app.i18n.finalizePendingLocaleChange()
  }

  const { scrollBehavior } = app.router.options

  app.router.options.scrollBehavior = async (to, from, savedPosition) => {
    if (to.name !== from.name) {
      await app.i18n.waitForPendingLocaleChange()
    }
    return scrollBehavior(to, from, savedPosition)
  }

  app.i18n.onBeforeLanguageSwitch = (
    _oldLocale,
    newLocale,
    _isInitial,
    context
  ) => {
    context.$api.instance.defaults.headers.common['Accept-Language'] = newLocale

    // Remove the conditional check for context.store.state.auth.user
    context.$api.postLocale(newLocale)
  }
}
