'use strict';

describe('Filter: inboxTask', function () {

  // load the filter's module
  beforeEach(module('flowApp'));

  // initialize a new instance of the filter before each test
  var inboxTask;
  beforeEach(inject(function ($filter) {
    inboxTask = $filter('inboxTask');
  }));

  it('should return the input prefixed with "inboxTask filter:"', function () {
    var text = 'angularjs';
    expect(inboxTask(text)).toBe('inboxTask filter: ' + text);
  });

});
