<template lang="pug">
  div.uk-card.uk-card-body.uk-card-default
    div.uk-child-width-expand(uk-grid='')
      p.uk-text-bold 直近のバトル
      .uk-text-right
        p.uk-text-small 2017-12-01 12:00:00
    div.uk-child-width-expand(uk-grid='')
      div.uk-width-medium
        img(src='/static/img/gangaze.jpg')
      div
        div.uk-child-width-expand(uk-grid='')
          p.uk-text-large.text-ikamodoki ガチエリア
          p.uk-text-right 1930ガチパワー
        div
          p.uk-text-large モズク農園
        div.text-ikamodoki(uk-grid='')
          p.color-pinkred WIN!
          p.uk-width-expand.color-pinkred 60カウント
          p.uk-text-right.color-freshgreen 40カウント
        progress.uk-progress(value="60" max="100")
    div.uk-grid-divider(class='uk-child-width-expand@s' uk-grid='')
      div
        ul.uk-list(v-for='name in ["ぞうさん", "てぃけパパ", "チャンコーリー", "たきぽまる"]')
          li(uk-grid='')
            p.uk-width-auto.text-ikamodoki.uk-text-large S+
            p.uk-width-expand
              | {{ name }}
              span.color-lightgray.uk-text-small.uk-margin-small-left -2
            p.uk-text-right 5k(2) 3d
      div
        ul.uk-list(v-for='name in ["ばむ", "フクク", "ほのお", "ひざ"]')
          li(uk-grid='')
            p.uk-width-auto.text-ikamodoki.uk-text-large S+
            p.uk-width-expand {{ name }}(sort)
            p.uk-text-right 5k(2) 3d
</template>

<style lang="stylus">
  li
    line-height 50px
  .uk-list
    margin 0
</style>

<script lang="coffee">
module.exports =
  data: ->
    message: ""
</script>
