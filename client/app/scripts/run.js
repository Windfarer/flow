angular.module('flowApp')
  .run(function($rootScope, $location, Auth, ACCESS_LEVELS) {
    $rootScope.$on("$routeChangeStart", function(evt, next, curr) {
      console.log(next);
      if (!Auth.isAuthoized(next.$$route.access_level)) {
        console.log("not loggin==================");
        if (Auth.isLoggedIn()) {
          $location.path('/');
        }
        else {

          $location.path('/login');
        }
      }
      else if (next.$$route.access_level === ACCESS_LEVELS.pub) {
          $location.path('/');
      }
    })
  });
