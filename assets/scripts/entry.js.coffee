window.UIkit = require 'uikit'
window.UIkitIcons = require 'uikit/dist/js/uikit-icons'
window.axios = require 'axios'
require './top_view'

body     = document.getElementsByTagName('body')[0]
endpoint = body.dataset.endpoint.split(':')
view     = endpoint[0]
action   = endpoint[1]

if view and window[view]
  klass = new window[view]
  if action && klass[action]
    klass[action]()

Vue = require 'vue'
latest_result= require './components/latest_result.vue'
result_history = require './components/result_history.vue'

new Vue(
  el: '#latest_result'
  components:
    'latest-result': latest_result
    'result-history': result_history
)
