<?php
$str = <<<ETO
using heredoc
ETO;
class foo {
    var $foo;
    var $bar;
    function foo() {
        $this->foo = 'foo';
        $this->bar = ['bar1', 'bar2'];
    }
}
$foo = new foo();
$tt = ["a" => "a", "v" => "v", "foo" => $foo];
$juices = array("apple", "orange", "koolaid1" => "purple");
// $foo["tt"] = "tt";
// $name = $foo['foo'];
// $value = $foo['bar'][0];
// $str1 = <<<ETO
// the class is "$foo", the value is "$value"
// ETO;
var_dump(null??null??3);
$value = @$cache;
var_dump($value);
var_dump(1 . 3 . 1.3);
$array1 = ['a' => '1', 'b' => '2'];
$array2['d'] = '5';
$array2 = ['b' => '3', 'c' => '4'];
var_dump($array2);
var_dump($array1 + $array2);
$a = array (0 => "apple", 1 => "banana");
$b = array (1 => "banana", 0 => "apple");

var_dump($a === $b); // prints bool(false) as well

$b = array ("0" => "apple", "1" => "banana");

var_dump($a === $b); // prints bool(true)
?>