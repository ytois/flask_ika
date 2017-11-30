gulp        = require 'gulp'
browserify  = require 'browserify'
source      = require 'vinyl-source-stream'
stylus      = require 'gulp-stylus'


gulp.task 'coffee', ->
  browserify
    entries: ['./assets/scripts/entry.js.coffee']
    extensions: ['.coffee']
  .bundle()
  .pipe source('bundle.js')
  .pipe gulp.dest('./static/js/')

gulp.task 'stylus', ->
  gulp.src ['./assets/styles/**/*.styl', '!./**/_*.styl']
    .pipe stylus()
    .pipe gulp.dest('./static/css/')

gulp.task 'watch', ->
  gulp.watch ['./assets/scripts/**/*.coffee'], ['coffee']
  gulp.watch ['./assets/styles/**/*.styl'], ['stylus']

gulp.task 'build', ['coffee', 'stylus']
gulp.task 'default', ['build', 'watch']
