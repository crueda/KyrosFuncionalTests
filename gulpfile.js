var gulp = require('gulp');
var rsync = require("rsyncwrapper");
var gutil = require('gulp-util');


gulp.task('default', function() {
  // place code for your default task here
});

// --------------------------------------------------------------------------------
// Actualizar 
// --------------------------------------------------------------------------------
gulp.task('pro', ['upload-dist'], function() {
  console.log('Actualizado el entorno de producción!');
});


// --------------------------------------------------------------------------------

// --------------------------------------------------------------------------------
// Subir ficheros a demos
// --------------------------------------------------------------------------------
gulp.task('upload-dist', function() {
  rsync({
    ssh: true,
    src: '/Users/Carlos/Workspace/Kyros/KyrosFuncionalTests/*.py',
    dest: 'root@172.26.30.234:/opt/KyrosFuncionalTests',
    recursive: true,
    syncDest: true,
    args: ['--verbose']
  }, function(error, stdout, stderr, cmd) {
      gutil.log(stdout);
  });
});




// --------------------------------------------------------------------------------

