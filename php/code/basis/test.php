<?php
    // $a = "attwtb";
    // echo $a . "b\n";
    // echo strpos($a, 't');
    // echo strstr($a, 't');
    // $ccdbChannel = 's12;1;3';
    // $channelArr = explode(';',$ccdbChannel);
    // echo $channelArr[0];
    // $activatedAt = '2008-08-08 08:08:08';
    // $activatedAt = strtotime($activatedAt);
    // echo date(DATE_RFC3339, $activatedAt);
    $i = 2; 
    function callBack(&$i) {
        ++ $i;
    };
    function tt() {
        echo 'tt';
    }
    // callBack($i);
    // call_user_func('callBack', $i);
    function test($callBack, &$i) { 
        for($j = 0; $j < 100; $j ++) {
            if ($j % $i === 3) {
                $callBack($i);
            }
        }
    }
    test('callBack', $i);
    echo $i;
    // echo $i;
?>