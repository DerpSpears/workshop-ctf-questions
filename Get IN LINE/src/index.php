<?php

highlight_file(__FILE__);
echo "<hr>";


if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    $blacklist = [
        'cat', 'head', 'tail', 'more', 'less', 'awk', 'sed', 'grep', 
        'nl', 'od', 'vi', 'vim', 'nano', 'sort', 'uniq', 'tac', 
        'base64', 'xxd', 'hexdump', 'strings', 'cp', 'mv', 'dd', 'php', 'echo','rm'
    ];
    $bad_chars = [' ', ';', '|', '&', '`', '$('];


    foreach ($blacklist as $bad) {
        if (stripos($cmd, $bad) !== false) {
            die("<br> <strong>DIE!</strong> '$bad' not allowerd");
        }
    }
    
    foreach ($bad_chars as $char) {
        if (strpos($cmd, $char) !== false) {
            die("<br><strong>NO!</strong> '$char' not allowed");
        }
    }


    
    echo "<pre>";
    system($cmd); 
    echo "</pre>";
}
?>
