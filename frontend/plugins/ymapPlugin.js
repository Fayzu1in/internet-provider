import Vue from 'vue'
import YmapPlugin from 'vue-yandex-maps'

const settings = {
  apiKey: 'ae67d8b1-fa31-44d0-94c2-6a583d082d64',
  lang: 'ru_RU',
  coordorder: 'latlong',
  enterprise: false,
  version: '2.1',
} // настройки плагина

Vue.use(YmapPlugin, settings)
