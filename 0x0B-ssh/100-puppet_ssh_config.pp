# ensuring ssh config maintains state

file {'/etc/ssh/ssh_config':
  ensure => present
}

file_line {'identity files':
  path   => '/etc/ssh/ssh_config',
  ensure => present,
  line   => '    IdentityFile ~/.ssh/school',
}

file_line {'password auth':
  path   => '/etc/ssh/ssh_config',
  ensure => present,
  line   => '    PasswordAuthentication no'
}
