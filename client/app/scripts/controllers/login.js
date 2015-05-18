'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('LoginCtrl', function ($location, $scope, restAPI, Auth, $cookieStore, $mdToast) {
    $scope.user = new restAPI.login();
    $scope.goToRegister = function () {
      $location.path("/register");
    };
    $scope.submit = function () {
      $scope.user.$save()
        .then(function (data){
          Auth.setUser(data);
          console.log("login success");

          $location.path('/')
        }, function (err) {
          var msg = err.data.message ? err.data.message : "login failed";
          $mdToast.showSimple(msg);
          console.log("login failed");
          console.log(err);
        })
    }
  });
