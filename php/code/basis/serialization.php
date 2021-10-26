<?php
    class SerializeClass {
        public $a = 'qwe';
        public $b = 'qvad';
        public function printf() {
            echo $this->a . PHP_EOL;
        }
    }
    // $s = serialize(new SerializeClass);
    // file_put_contents('store', $s);
    $s = file_get_contents('store');
    $us = unserialize($s);
    $us->printf();
    var_export($us);
?>