# use trace then automate it with pp

exec { 'fix_typo':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  =>  "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  provider =>  'shell'}
