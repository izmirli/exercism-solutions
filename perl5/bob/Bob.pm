# Declare package 'Bob'
package Bob;

use strict;
use warnings;
use feature qw<say>;

use Exporter qw<import>;
our @EXPORT_OK = qw<hey>;

=pod

=head1 DESCRIPTION

Bob - a lackadaisical teenager answering bot.
 
Answers:
 - 'Sure.' if questioned, such as "How are you?".
 - 'Whoa, chill out!' if YELLED AT (in all capitals).
 - 'Calm down, I know what I'm doing!' if yelled a question.
 - 'Fine. Be that way!' if not saying anything.
 - 'Whatever.' otherwise.

=item hey()

Answer according to given prompt.
$msg: the prompt bob should answer

=cut

sub hey {
    my ($msg) = @_;
    $msg =~ s/^\s+|\s+$//g;
    return 'Fine. Be that way!' unless $msg;

    my $question = $msg =~ /\?$/ ? 1 : 0;
    my $yell = $msg =~ /[A-Z]/ && $msg !~ /[a-z]/ ? 1 : 0;
    return "Calm down, I know what I'm doing!" if $question && $yell;
    return 'Sure.'                             if $question;
    return 'Whoa, chill out!'                  if $yell;
    return 'Whatever.';
}

1;

