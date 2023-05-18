# Puppet file to edit /etc/default/nginx
exec { 'editlimits':
        command => 'sed -i "s/15/4096/g" /etc/default/nginx',
        path    => '/usr/local/bin/:/bin/'
}
exec { 'restart_nginx':
        command => 'nginx restart',
        path    => 'etc/init.d',
        require => Exec['editlimits']
}
