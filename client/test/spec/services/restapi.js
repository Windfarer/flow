'use strict';

describe('Service: restAPI', function () {

  // load the service's module
  beforeEach(module('flowApp'));

  // instantiate service
  var restAPI;
  beforeEach(inject(function (_restAPI_) {
    restAPI = _restAPI_;
  }));

  it('should do something', function () {
    expect(!!restAPI).toBe(true);
  });

});
