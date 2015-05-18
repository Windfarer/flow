'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:RegisterCtrl
 * @description
 * # RegisterCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('RegisterCtrl', function ($location, $scope, restAPI, $mdToast) {
    $scope.user = new restAPI.register();
    $scope.goToLogin = function () {
      $location.path("/login");
    };
    $scope.submit = function () {
      $scope.user.$save()
        .then(function (data){
          console.log("register success");
          console.log(data);
          $mdToast.showSimple("register success");
          $location.path('/login')
        }, function (err) {
          var msg = err.data.message ? err.data.message : "register failed";
          $mdToast.showSimple(msg);
          console.log("register failed");
          console.log(err);
        })
    }
  });
