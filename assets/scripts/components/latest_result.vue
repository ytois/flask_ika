<template lang="pug">
  div.uk-card.uk-card-body.uk-card-default
    div(class='uk-child-width-expand@s' uk-grid='')
      h2 latest
      .uk-text-right
        p 2017-12-01 12:00:00
    div(uk-grid='')
      div.uk-width-medium
        img(src='/static/img/gangaze.jpg')
      div
        p ナワバリバトル
        p モズク農園
        p WIN! 60%
    progress.uk-progress(value="60" max="100")
    div.uk-grid-divider(class='uk-child-width-expand@s' uk-grid='')
      div
        p S+ weapon   ぞうさん(sort)      5k(2) 3d
        p S+ てぃけぽまる
        p S+ チャンコーリー
        p S+ たきぽまる
      div
        p ほのお
        p ひざ
        p take
        p ひげなっくる
</template>

<style lang="stylus">
</style>

<script lang="coffee">
module.exports =
  data: ->
    message: ""
</script>
