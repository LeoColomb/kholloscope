module.exports = function (grunt) {
  'use strict';
  grunt.initConfig({
    bottleVer : '0.12.7',
    bower: {
      up: {
        options: {
          targetDir: './assets',
          layout: function (type, component) {
            return type;
          }
        }
      }
    },
    curl: {
      bootle: {
        src: 'https://raw.githubusercontent.com/defnull/bottle/<%= bottleVer %>/bottle.py',
        dest: 'bottle.py'
      }
    }
  });

  grunt.loadNpmTasks('grunt-curl');
  grunt.loadNpmTasks('grunt-bower-task');

  grunt.registerTask('default', ['bower', 'curl']);
};
