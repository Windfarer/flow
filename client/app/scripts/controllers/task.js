'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:TaskCtrl
 * @description
 * # TaskCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('TaskCtrl', function($scope, restAPI, taskFilterOption) {
    $scope.task = new restAPI.tasks();
    $scope.tasks = restAPI.tasks.query();
    $scope.updateTask = function (task) {
      console.log(task.done);
      task.$update();
    };
    $scope.submitTask = function () {
      $scope.task.$save()
        .then(function(data) {
            $scope.task = new restAPI.tasks();
            $scope.tasks.push(data);
        })
    };
    $scope.task_filter_option = taskFilterOption;
    console.log($scope.task_filter_option);
  });
