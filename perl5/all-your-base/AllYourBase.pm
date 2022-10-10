package AllYourBase;

use strict;
use warnings;
use feature qw<say>;
use List::Util qw(max);

use Exporter qw<import>;
our @EXPORT_OK = qw<rebase>;

my @errors = (
    'input base must be >= 2',
    'output base must be >= 2',
    'all digits must satisfy 0 <= d < input base',
);

sub rebase {
    my ($input) = @_;
    die $errors[0] unless $input->{'inputBase'} >= 2;
    die $errors[1] unless $input->{'outputBase'} >= 2;
    my $normValue = getDecValue($input->{'digits'}, $input->{'inputBase'});
    return valToNewBase($normValue, $input->{'outputBase'});
}

sub valToNewBase {
    my ($val, $base) = @_;
    my %digits = ();
    while($val > 0) {
        my $digitIndex = 0;
        while($base**$digitIndex < $val) {
            $digitIndex++;
        }
        $digitIndex-- if $base**$digitIndex > $val;
        my $digit = int($val / $base**$digitIndex);
        $val -= $digit * $base**$digitIndex;
        $digits{$digitIndex} = $digit;
    }
    my $maxDigitInsex = max(keys %digits);
    my @new = reverse map(exists $digits{$_} ? $digits{$_} : 0, (0 .. $maxDigitInsex));
    return \@new;
}

sub getDecValue {
    my ($number, $base) = @_;
    my $decVal = 0;
    #my @digits = reverse map(int($_), split(//, $number));
    my @digits = reverse @$number;
    foreach my $i (0 .. $#digits) {
        die $errors[2] unless 0 <= $digits[$i] && $digits[$i] < $base;
        $decVal += $digits[$i] * $base**$i
    }
    return $decVal;
}

1;
