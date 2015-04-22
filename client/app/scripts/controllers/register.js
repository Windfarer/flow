'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:RegisterCtrl
 * @description
 * # RegisterCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('RegisterCtrl', function ($location, $scope, restAPI) {
    $scope.user = new restAPI.register();
    $scope.submit = function () {
      $scope.user.$save()
        .then(function (data){
          console.log("register success");
          console.log(data);
          $location.path('/login')
        }, function (err) {
          console.log("register failed");
          console.log(err);
        })
    }
  });
