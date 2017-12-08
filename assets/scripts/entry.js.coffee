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

