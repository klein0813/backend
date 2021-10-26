<?php
    class Func{
        public $bar;
        public $value = '23';
        public function __construct()
        {
            $this->bar = function ()
            {
                return 32;
            };
        }
    }

    $funcName = 'Func';
    $func = new $funcName();
    var_dump(($func->bar)()) . PHP_EOL;
    var_dump(Func::class) . PHP_EOL;
    var_dump($func -> value) . PHP_EOL;
    class Outer
    {
        private $prop = 1;
        protected $prop2 = 2;
    
        protected function func1()
        {
            return 3;
        }
    
        public function func2()
        {
            return new class($this->prop) extends Outer {
                private $prop3;
    
                public function __construct($prop)
                {
                    $this->prop3 = $prop;
                }
    
                public function func3()
                {
                    return $this->prop2 + $this->prop3 + $this->func1();
                }
            };
        }
    }
    
    echo (new Outer)->func2()->func3() . PHP_EOL;

    function anonymous_class()
    {
        return new class {};
    }
    
    if (get_class(anonymous_class()) === get_class(anonymous_class())) {
        echo 'same class' . PHP_EOL;
    } else {
        echo 'different class' . PHP_EOL;
    }
?>