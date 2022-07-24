<?php
    // Если кнопка нажата, то выполняет тело условия
    header("Content-Type: image/jpeg");
    $im = @imagecreate($_POST['width'], $_POST['height'])
    or die("Невозможно создать поток изображения");
    $background_color = imagecolorallocate($im, 255, 255, 255);
    $text_color = imagecolorallocate($im, 0, 0, 0);
    imagestring($im, 10, $_POST['width'] / 2 - 10, $_POST['height'] / 2,  $_POST['text_php'], $text_color);
    imagepng($im);
    imagedestroy($im);

?>

