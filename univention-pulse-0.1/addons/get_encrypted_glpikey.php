<?php
   function encrypt($string, $key) {

     $result = '';
     for($i=0 ; $i<strlen($string) ; $i++) {
       $char    = substr($string, $i, 1);
       $keychar = substr($key, ($i % strlen($key))-1, 1);
       $char    = chr(ord($char)+ord($keychar));
       $result .= $char;
     }

     return base64_encode($result);
   }

if (isset($argv[1])) echo encrypt($argv[1], $argv[2]);
?>
