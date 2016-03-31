module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		sass: {
			dist: {
				options : {
					style: 'compressed'
				},
				files: {
					'static/css/index.css' : 'static/scss/index.scss',
					'static/css/herstory.css' : 'static/scss/herstory.scss',
					'static/css/lawn.css' : 'static/scss/lawn.scss',
					'static/css/rush.css' : 'static/scss/rush.scss',
					'static/css/teh.css' : 'static/scss/teh.scss'
				}
			}
		},
		watch: {
			css: {
				files: 'static/scss/*.scss',
				tasks: ['sass']
			}
		}
	});
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');

	grunt.registerTask('default', ['sass', 'watch']);
};