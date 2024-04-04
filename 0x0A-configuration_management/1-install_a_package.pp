# install flask from pip3.

# epython
package { 'python3.8':
  ensure => present,
}

# pip presnting
package { 'python3-pip':
  ensure => present,
}

# flask install
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# package
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
