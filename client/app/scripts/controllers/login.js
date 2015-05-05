'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('LoginCtrl', function ($location, $scope, restAPI, Auth, $cookieStore) {
    $scope.user = new restAPI.login();
    $scope.goToRegister = function () {
      $location.path("/register");
    };
    $scope.submit = function () {
      $scope.user.$save()
        .then(function (data){
          //Auth.setUser(data);
          //console.log("login success");
          console.log(data);
          $location.path('/')
        }, function (err) {
          console.log("login failed");
          console.log(err);
        })
    }
  });
