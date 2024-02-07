<?php
/*
 * Raindrops.
 */

declare(strict_types=1);

function raindrops(int $number): string
{
    $drops = [
        ['factor' => 3, 'sound' => 'Pling'],
        ['factor' => 5, 'sound' => 'Plang'],
        ['factor' => 7, 'sound' => 'Plong'],
    ];
    $result = '';
    for($i = 0; $i < count($drops); ++$i) {
        if ($number % $drops[$i]['factor'] == 0)
            $result .= $drops[$i]['sound'];
    }
    return $result != '' ? $result : strval($number);
}
