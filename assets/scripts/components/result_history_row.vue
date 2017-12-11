<template lang="pug">
  li
    div.uk-child-width-expand(uk-grid='')
      div.uk-width-1-6
        p.uk-text-center.team-result WIN
      div
        div(uk-grid='')
          div
            p ガチエリア
          div
            p ガンガゼ野外音楽堂
        div.uk-child-width-expand(uk-grid='')
          div
            p.result-count 60
          div.uk-text-right
            p.power-text 1809ガチパワー
        div
          progress.uk-progress(value="60" max="100")
      div.uk-width-1-6
        p S+
        p 11k(2) 3d 1s
</template>

<style lang="stylus" scoped>
  li
    border solid 1px gray
    border-radius 10px
    background-color white
    padding 10px
  .uk-progress
    height 3px
    margin 0
    text-align bold
  .result-count
    margin 0 0 0 0
  .team-result
   font-size 1.2em
  .power-text
   color gray
   font-size 0.8em

</style>

<script lang="coffee">
module.exports =
  data: ->
    message: ""
</script>
