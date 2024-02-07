package RomanNumerals;

use v5.38;

use Exporter qw<import>;
our @EXPORT_OK = qw<to_roman>;

my @ROMAN_NUMERALS = (
  [1000, 'M'],
  [900, 'CM'],
  [500, 'D'],
  [400, 'CD'],
  [100, 'C'],
  [90, 'XC'],
  [50, 'L'],
  [40, 'XL'],
  [10, 'X'],
  [9, 'IX'],
  [5, 'V'],
  [4, 'IV'],
  [1, 'I']
);

sub to_roman ($number) {
    return '' if $number <= 0;
    my ($digit_val, $rom) = @{(grep {$_->[0] <= $number} @ROMAN_NUMERALS)[0]};
    return $rom . to_roman($number - $digit_val);
}
