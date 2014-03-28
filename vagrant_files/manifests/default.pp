exec { "apt-get update":
	path => "/usr/bin",
}

package { "build-essential":
	ensure => present,
	require => Exec["apt-get update"],
}

package { "git":
	ensure => present,
	require => Exec["apt-get update"],
}

package { "python":
	ensure => present,
	require => Exec["apt-get update"],
}

package { "python-dev":
	ensure => present,
	require => Exec["apt-get update"],
}

package { "python-pip":
	ensure => present,
	require => Exec["apt-get update"],
}