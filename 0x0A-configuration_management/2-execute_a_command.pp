# kills a process
exec {'pkill -f killmenow':
  path    => ['/bin', 'usr/bin'],
  onlyif  => 'pgrep -f killmenow',
  returns => '0'
}
