'use strict';
angular.module('flowApp')
  .run(function($rootScope, $location, Auth, ACCESS_LEVELS) {
    $rootScope.$on("$routeChangeStart", function(evt, next, curr) {
      if (Auth.isLoggedIn()) {
        if (next.$$route.access_level === ACCESS_LEVELS.pub || !Auth.isAuthoized(next.$$route.access_level)) {
          $location.path('/');
        }
      }
      else {
        if (next.$$route.access_level !== ACCESS_LEVELS.pub) {
          $location.path('/login');
        }
      }
    })
  });
