<?php
    const OPERATION_FORK = 'fork';
    const SLEEP_TIME = 100;
    const MAX_WAIT_TIME = 1000;
    function processHandler($operation, $callback, $args, &$pids=[], $pTime=SLEEP_TIME, $mTime=MAX_WAIT_TIME) {
        $sTime = time();
        while(1) {
            $eTime = time();
            if ($eTime - $sTime > $mTime) {
                exit(MAX_WAIT_TIME);
            }

            if ($operation === OPERATION_FORK) {
                $pid = pcntl_fork();
                if ($pid == -1) {
                    sleep($pTime);
                    continue;
                } else if ($pid == 0) {
                    call_user_func_array($callback, [$args]);
                    exit(0);
                } else {
                    array_push($pids, $pid);
                }
            } else {
                foreach ($pids as $pid) {
                    pcntl_waitpid($pid);
                }
            }
            exit(1);
        }
    }