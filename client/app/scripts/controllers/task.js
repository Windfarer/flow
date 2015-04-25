'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:TaskCtrl
 * @description
 * # TaskCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('TaskCtrl', function($scope, restAPI, $location, $routeParams) {
    switch ($routeParams.task_status) {
      case 'inbox':
            $scope.task_status = {"status": 0};
            break;
      case 'doing':
            $scope.task_status = {"status": 1};
            break;
      case "done":
            $scope.task_status = {"status": 2};
            break;
      default:
            console.log("default");
            $scope.task_status = {"status": 0};
    }
      $scope.task = new restAPI.tasks();
    $scope.tasks = restAPI.tasks.query();
    $scope.updateTask = function (task) {
      console.log(task);
      task.$update();
    };
    $scope.submitTask = function () {
      $scope.task.$save()
        .then(function(data) {
            $scope.task = new restAPI.tasks();
            $scope.tasks.push(data);
        })
    };

  });
