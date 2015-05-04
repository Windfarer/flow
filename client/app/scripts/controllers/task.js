'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:TaskCtrl
 * @description
 * # TaskCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('TaskCtrl', function($scope, $routeParams, restAPI, $timeout, $q) {
    var project_id = $routeParams.project_id;
    if (project_id) {
      $scope.project = restAPI.projects.get({project_id: project_id});
    }

    $scope.task_status = {"status": 0};
    $scope.task = new restAPI.tasks();
    $scope.tasks = {
      inbox: restAPI.tasks.query({status:0, project:project_id}),
      doing: restAPI.tasks.query({status:1, project:project_id}),
      done: restAPI.tasks.query({status:2, project:project_id})
    };
    $scope.changeStatusFilter = function(status) {
      console.log("change to:"+status);
      $scope.task_status = {"status": status};
    };
    $scope.updateTask = function (task) {
      console.log(task);
      task.$update();
    };
    $scope.deleteTask = function (task) {
      task.$delete();
    };
    $scope.submitTask = function () {
      $scope.task.$save({project:project_id})
        .then(function(data) {
            $scope.task = new restAPI.tasks({project:project_id});
            $scope.tasks.inbox.push(data);
        })
    };

    $scope.AddSubTask = function (task) {
      if (!task.sub_tasks){
        task.sub_tasks = [];
      }
      task.sub_tasks.push({title:task.newsubtask.title, status:0});
      task.newsubtask.title = "";
    };

    var createFilterFor = function (query) {
      var lowercaseQuery = angular.lowercase(query);

      return function filterFn(contact) {
        console.log(contact);
        return (contact.nickname.indexOf(lowercaseQuery) != -1);
      };
    };
    $scope.querySearch = function (query) {
      var results = query ? $scope.project.members.filter(createFilterFor(query)) : [];
      console.log(results);
      return results;
    };
  });
