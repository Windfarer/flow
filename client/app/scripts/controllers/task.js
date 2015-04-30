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
    $('.collapsible').collapsible({
      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });

    $scope.isActive = 'test1';
    $('ul.tabs').tabs();
    $scope.changeActive = function (option) {
      $scope.isActive = option;
      $('ul.tabs').tabs('select_tab', option);
    };



    $scope.task_status = {"status": 0};
    $scope.task = new restAPI.tasks();
    //$scope.tasks = restAPI.tasks.query();
    restAPI.tasks.query().$promise.then(function(data){
      console.log(data);
      $scope.tasks=data;
    });
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
