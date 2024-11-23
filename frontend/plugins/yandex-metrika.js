/* eslint-disable no-unused-expressions */
export default () => {
  if (process.client) {
    // Check if the script is already present
    if (
      document.querySelector(
        `script[src="https://mc.yandex.ru/metrika/tag.js"]`
      )
    )
      return // Dynamically create the script tag
    ;(function (m, e, t, r, i, k, a) {
      m[i] =
        m[i] ||
        function () {
          ;(m[i].a = m[i].a || []).push(arguments)
        }
      m[i].l = 1 * new Date()
      // eslint-disable-next-line no-sequences
      ;(k = e.createElement(t)), (a = e.getElementsByTagName(t)[0])
      k.async = 1
      k.src = r
      a.parentNode.insertBefore(k, a)
    })(window, document, 'script', 'https://mc.yandex.ru/metrika/tag.js', 'ym')

    // Initialize Yandex Metrika
    window.ym(99013673, 'init', {
      clickmap: true,
      trackLinks: true,
      accurateTrackBounce: true,
      webvisor: true,
    })

    // Add noscript fallback
    const noscript = document.createElement('noscript')
    noscript.innerHTML = `
        <div>
          <img src="https://mc.yandex.ru/watch/99013673" style="position:absolute; left:-9999px;" alt="" />
        </div>
      `
    document.body.appendChild(noscript)
  }
}
