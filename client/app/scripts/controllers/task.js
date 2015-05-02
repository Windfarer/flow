'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:TaskCtrl
 * @description
 * # TaskCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('TaskCtrl', function($scope, restAPI) {
    $scope.isActive = 'test1';
    $('ul.tabs').tabs();
    $scope.changeActive = function (option) {
      $scope.isActive = option;
      $('ul.tabs').tabs('select_tab', option);
    };

    $scope.task_status = {"status": 0};
    $scope.task = new restAPI.tasks();
    $scope.tasks = restAPI.tasks.query();
    //$scope.tasks = [{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'},{title: 'aaaaa',description:'bbbbb'}];

    $scope.changeStatusFilter = function(status) {
      console.log("change to:"+status);
      $scope.task_status = {"status": status};
    };
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
