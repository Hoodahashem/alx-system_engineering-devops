# Puppet manifest to install Flask version 2.1.0 on Ubuntu 20.04 LTS

package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'werkzeug':
    ensure   => '2.1.0',
    provider => 'pip',
    require  => package['python3-pip'],
}
