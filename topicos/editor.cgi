#!/usr/local/bin/perl


print "Content-Type: text/html\n\n"; # cabecalho

# converte uma string URL encoded
sub URL2text {
  local($texto) = @_;
  $texto =~ s/\+/ /g;
  while($texto =~ /\%(\S\S)/) {
    $temp1 = $1;
    $char = pack("c",hex($1));
    $texto =~ s/\%$1/$char/;
  }
  return $texto;
}

$ENV{PATH} = "$ENV{PATH}:/usr/local/bin:/usr/local/netpbm";

if($ENV{QUERY_STRING} =~ /body=(.*)/) {
  $texto = URL2text($1);
}
open(OUT,"|/usr/local/bin/tth -i -e2") || die "Could not open the pipe to
tth\n";
print OUT "\\def\\href#1#2{\\special{html:<a ";
print OUT "href=\"#1\">}{#2}\special{html:</a>}}";
print OUT $texto;

