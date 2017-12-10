<template lang="pug">
  ul.uk-list
    history-row
    history-row
    history-row
    history-row
</template>

<style lang="stylus" scoped>
  ul
    background-color gray
    padding 10px
</style>

<script lang="coffee">
history_row = require './result_history_row.vue'

module.exports =
  data: ->
    history: []
  components:
    'history-row': history_row
</script>
