<?php
//只起到了监听效果
// $flag = false;
// pcntl_signal(SIGALRM, function () {
//     global $flag;
//     $flag = true;
//     echo "Received an alarm signal !$flag" . PHP_EOL;
// }, false);
// function t() {
//     sleep(3000);
//     var_dump('timeout');
// }

// pcntl_alarm(1);
// $i = 1000000000;
// while($i > 0) {
//     $i = $i - 1;
// };
// pcntl_signal_dispatch();
// var_dump($flag);
pcntl_async_signals(true);
$flag = false;
pcntl_signal(SIGALRM, function () {
    global $flag;
    $flag = true;
    echo "Received an alarm signal !$flag" . PHP_EOL;
}, false);
function t() {
    sleep(3000);
    var_dump('timeout');
}

pcntl_alarm(1);
// $i = 1000000000;
// while($i > 0) {
//     $i = $i - 1;
// };
pcntl_signal_dispatch();
var_dump($flag);
?>