# ensuring ssh config maintains state

file {'/etc/ssh/ssh_config':
  ensure => present
}

file_line {'identity files':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}

file_line {'password auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}
