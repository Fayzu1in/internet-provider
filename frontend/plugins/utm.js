import { getUTMParameters } from '~/utils'

export default ({ app }, inject) => {
  const storedUTM = JSON.parse(localStorage.getItem('utm_params'))
  const urlUTM = getUTMParameters()

  if (Object.keys(urlUTM).length) {
    localStorage.setItem('utm_params', JSON.stringify(urlUTM))
    inject('utm', urlUTM)
  } else if (storedUTM) {
    inject('utm', storedUTM)
  } else {
    inject('utm', {})
  }
}
