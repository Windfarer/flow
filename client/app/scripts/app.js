'use strict';

/**
 * @ngdoc overview
 * @name flowApp
 * @description
 * # flowApp
 *
 * Main module of the application.
 */
angular
  .module('flowApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'ngMaterial',
    'ngMessages'
  ])
  .config(function ($routeProvider, ACCESS_LEVELS) {
    $routeProvider
      //.when('/', {
      //  redirectTo: '/task/'
      //})
      .when('/login', {
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl',
        access_level: ACCESS_LEVELS.pub
      })
      .when('/register', {
        templateUrl: 'views/register.html',
        controller: 'RegisterCtrl',
        access_level: ACCESS_LEVELS.pub
      })
      .when('/project/:project_id/task/:task_status', {
        templateUrl: 'views/task.html',
        controller: 'TaskCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/task/:task_status', {
        templateUrl: 'views/task.html',
        controller: 'TaskCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/project/:project_id', {
        templateUrl: 'views/project.html',
        controller: 'ProjectCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/user', {
        templateUrl: 'views/user.html',
        controller: 'UserCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/landing', {
        templateUrl: 'views/landing.html',
        controller: 'LandingCtrl',
        access_level: ACCESS_LEVELS.pub
      })
      .otherwise({
        redirectTo: '/task/inbox'
      });
  });
