# Increase the number of open files for the users
exec { 'maxfilesopen':
  environment => ['DIR=/etc/security/limits.conf',
                  'OLD=hard nofile 5',
                  'NEW=hard nofile 50000',
                  'OLD2=soft nofile 4',
                  'NEW2=soft nofile 40000'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR; sudo sed -i "s/$OLD2/$NEW2/" $DIR',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
