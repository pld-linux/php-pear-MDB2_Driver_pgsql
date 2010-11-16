%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	MDB2_Driver_pgsql
%define		subver	b3
%define		rel		1
Summary:	%{_pearname} - pgsql MDB2 driver
Summary(pl.UTF-8):	%{_pearname} - sterownik pgsql dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	0.%{subver}.%{rel}
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	3d5caa6ef480fb75862e87aef0282229
URL:		http://pear.php.net/package/MDB2_Driver_pgsql/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.5.0-0.b2
Requires:	php-pgsql
Obsoletes:	php-pear-MDB2_Driver_pgsql-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the PostgreSQL MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Sterownik PostgreSQL dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# tests should not be packaged
%{__rm} -r $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/pgsql.php
%{php_pear_dir}/MDB2/Driver/Manager/pgsql.php
%{php_pear_dir}/MDB2/Driver/Native/pgsql.php
%{php_pear_dir}/MDB2/Driver/Reverse/pgsql.php
%{php_pear_dir}/MDB2/Driver/pgsql.php
%{php_pear_dir}/MDB2/Driver/Function/pgsql.php
%{php_pear_dir}/data/MDB2_Driver_pgsql
