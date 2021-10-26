<?php
  function a() {
      var_dump('-8-9');
  }
  function t() {
    return 'a';
  }
  $v = function () {
      return 'a';
  };
  $_v = function () {
      return function () {
          return '_v';
      };
  };
  t()();
  var_dump(t()());
  var_dump($v(1));
  var_dump($v()());
  var_dump($_v()());
?>