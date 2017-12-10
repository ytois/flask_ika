window.UIkit = require('uikit')
window.UIkitIcons = require 'uikit/dist/js/uikit-icons'

Vue = require 'vue'
latest_result= require './components/latest_result.vue'
result_history = require './components/result_history.vue'

new Vue(
  el: '#latest_result'
  components:
    'latest-result': latest_result
    'result-history': result_history
)
