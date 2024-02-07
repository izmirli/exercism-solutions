package Raindrops;

use v5.38;

use Exporter qw<import>;
our @EXPORT_OK = qw<raindrop>;

my $RAINDROPS = [
    {'factor' => 3, 'sound' => 'Pling'},
    {'factor' => 5, 'sound' => 'Plang'},
    {'factor' => 7, 'sound' => 'Plong'},
];

sub raindrop ($number) {
    my $result = '';
    for my $raindrop (@$RAINDROPS) {
        if ($number % $raindrop->{'factor'} == 0) {
            $result .= $raindrop->{'sound'};
        }
    }
    return $result || "$number";
}
