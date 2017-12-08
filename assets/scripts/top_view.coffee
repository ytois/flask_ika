Vue = require 'vue'

class window.TopView
  dashboard: ->
    console.log 'do dashboard'
    result_li = Vue.extend(
      props: ['resultData']
      template: """
        <li class="uk-grid">
            <div class="uk-width-1-3">
                {{ resultData.result }}
                {{ resultData.start_time }}
            </div>
            <div class="uk-width-1-3">
                {{ resultData.stage }}
                {{ resultData.rule }}
                {{ resultData.udemae }}
                {{ resultData.player.nickname }}
                ({{ resultData.player.sort_score }})
            </div>
            <div class="uk-width-1-3">
                {{ resultData.player.player_rank }}
                {{ resultData.player.kill_count }}k
                ({{ resultData.player.assist_count }})
                {{ resultData.player.death_count }}d
                {{ resultData.player.special_count }}
            </div>
        </li>
      """
      data: ->
        {}
    )

    window.vm = new Vue(
      el: '#results'
      data:
        results: []
      methods:
        fetch: ->
          self = @
          axios.get(Flask.url_for('ApiView:results')).then( (res) ->
            self.results = res.data
          )
      created: ->
        @fetch()
      components:
        'result-li': result_li
    )
