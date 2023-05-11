// plugins/axios-csrf.js
export default function ({ $axios, app }) {
  $axios.onRequest((config) => {
    const csrfToken = app.$cookies.get('csrfToken') // Adjust based on how you retrieve the CSRF token

    if (csrfToken) {
      config.headers['X-CSRF-Token'] = csrfToken
    }

    return config
  })
}
