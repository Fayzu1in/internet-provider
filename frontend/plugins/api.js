// import axios from 'axios'

export default ({ $axios, i18n }, inject) => {
  const $api = $axios.create({
    baseURL: 'https://internetbor.uz/api/v1/',
    headers: {
      common: {
        Accept: 'application/json',
        'Accept-Language': i18n.locale,
      },
    },
  })

  const apiMethods = {
    // api client instance for custom requests
    instance: $api,

    // error handler
    // errorHandler(error) {
    //   console.log('Request canceled', error.message)
    // },

    postCallBack: (name, phone, preferrableTime) =>
      $api.$post(`/quick/`, {
        name,
        phone,
        preferrable_time: preferrableTime,
      }),
  }

  inject('api', apiMethods)
}
